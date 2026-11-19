#!/usr/bin/env python3
"""MemeDesk v2 — PAPER TRADING ONLY. No wallets, no keys, no signing, no real orders. Quotes are read-only.
Scout -> Filter -> Analyst (shared) ; Executor -> Risk -> Logger per variant ('original', 'adjusted').
Slow/reference feed: DexScreener. Fast feed: Jupiter Price API v3 (lite-api.jup.ag, no key).
Executable fills: Jupiter Quote API (read-only quote for the exact simulated size) + latency/priority buffer.

Operational clocks (strategy rules are unchanged):
  MEMEDESK_END_AT       ISO-8601. Default 2026-11-20 09:00 America/Panama (14:00 UTC).
                        Reaching this marks open positions to market and stops.
  MEMEDESK_CHUNK_UNTIL  optional ISO-8601, earlier than END_AT. Exits and saves state
                        without closing positions so the next process can resume."""
import json, os, re, time, csv, traceback, threading, subprocess, statistics, faulthandler, signal, sys
import datetime as dt
from zoneinfo import ZoneInfo

faulthandler.register(signal.SIGUSR1, file=sys.stderr, all_threads=True)   # watchdog dumps stacks before killing
BASE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(BASE, "logs")
TZ = ZoneInfo("America/Panama")

def _parse_iso(raw, what):
    s = raw.strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    try:
        d = dt.datetime.fromisoformat(s)
    except Exception as e:
        raise SystemExit("bad %s %r (%s)" % (what, raw, e))
    if d.tzinfo is None:
        d = d.replace(tzinfo=dt.timezone.utc)
    return d.astimezone(TZ)

def _end_at():
    raw = os.environ.get("MEMEDESK_END_AT", "").strip()
    if not raw:
        return dt.datetime(2026, 11, 20, 9, 0, tzinfo=TZ)
    return _parse_iso(raw, "MEMEDESK_END_AT")

def _chunk_until(end_at):
    raw = os.environ.get("MEMEDESK_CHUNK_UNTIL", "").strip()
    if not raw:
        return None
    d = _parse_iso(raw, "MEMEDESK_CHUNK_UNTIL")
    # A deadline at or after the strategy end is not a chunk boundary: run through
    # END_AT so open positions are marked to market.
    if d >= end_at:
        return None
    return d

END_AT = _end_at()
CHUNK_UNTIL = _chunk_until(END_AT)

def keep_running():
    t = now()
    if t >= END_AT:
        return False
    if CHUNK_UNTIL is not None and t >= CHUNK_UNTIL:
        return False
    return True
DS = "https://api.dexscreener.com"
GT = "https://api.geckoterminal.com/api/v2/networks/solana"
JUP_PRICE = "https://lite-api.jup.ag/price/v3?ids="
JUP_QUOTE = "https://lite-api.jup.ag/swap/v1/quote"
RC = "https://api.rugcheck.xyz/v1/tokens/{}/report"
RPC = "https://api.mainnet-beta.solana.com"
SOL = "So11111111111111111111111111111111111111112"
START_EQUITY = 1000.0
# costs
FALLBACK_SLIP, FALLBACK_FEE = 0.01, 0.003   # used only when no Jupiter quote: 1% slippage + 0.3% fee per side
QUOTE_EXTRA = 0.004                          # on top of Jupiter quote per side: 0.1% network/priority fee + 0.3% execution-latency buffer
COST_RT_FLAT = 2 * (FALLBACK_SLIP + FALLBACK_FEE)   # 2.6% round trip, divergence comparison threshold
SCAN_EVERY = 90
RISK_EVERY = 3        # s, fast-feed stop checks
SLOW_REF_EVERY = 30   # s, DexScreener reference price for open positions
REEVAL_AFTER = 600
RC_CACHE = 600
LP_LOCK_MIN = 90.0
SMART_WALLET_NEUTRAL = 50
COOLDOWN_AFTER_LOSS_H = 4
MAX_ENTRIES_PER_TOKEN_DAY = 2
EXCHANGE_PAT = re.compile(r"binance|coinbase|okx|bybit|kraken|kucoin|gate|mexc|bitget|htx|huobi|crypto\.com|exchange|cex", re.I)

def now(): return dt.datetime.now(TZ)
def iso(): return now().isoformat(timespec="seconds")
_wl = threading.Lock()
def jl(name, obj):
    obj = {"ts": iso(), **obj}
    with _wl, open(os.path.join(LOG, name), "a") as f: f.write(json.dumps(obj, default=str) + "\n")

_last = {}; _tl = threading.Lock()
def throttle(key, gap):
    with _tl:
        t = max(_last.get(key, 0) + gap, time.time()); _last[key] = t
    w = t - time.time()
    if w > 0: time.sleep(w)

def http(url, key="x", gap=0.0, timeout=6, retries=2, data=None):
    """curl subprocess: hard wall-clock timeout; retries with backoff on 429/network errors. Returns (json|None, ms)."""
    throttle(key, gap)
    ms = None
    for i in range(retries + 1):
        t0 = time.time()
        cmd = ["curl", "-s", "-L", "--max-time", str(timeout), "--connect-timeout", "4", "-A", "memedesk-paper/2.0", "-w", "\n%{http_code}"]
        if data is not None: cmd += ["-H", "content-type: application/json", "-d", data]
        try:
            r = subprocess.run(cmd + [url], capture_output=True, text=True, timeout=timeout + 3)
            body, _, code = r.stdout.rpartition("\n"); code = int(code or 0)
        except Exception as e:
            body, code = "", 0
        ms = round((time.time() - t0) * 1000)
        jl("latency.jsonl", {"src": "http:" + url.split("/")[2] + ("/quote" if "/quote" in url else "/price" if "/price" in url else ""),
                             "ms": ms, "status": code})
        if code != 200:
            jl("http.jsonl", {"url": url[:110], "status": code, "ms": ms, "try": i})
        if code == 200:
            try: return json.loads(body), ms
            except Exception: return None, ms
        if code in (429, 0) or code >= 500:
            time.sleep(0.5 * (3 ** i)); continue
        return None, ms
    return None, ms

def get(url, key, gap, timeout=6): return http(url, key, gap, timeout)[0]

STATS = {"started": iso(), "scan_loops": 0, "evaluations": 0, "unique_tokens": set(), "scout_in_range": 0,
         "discovered_by_source": {}, "kills_primary": {}, "kills_any": {}, "kills_only_unknown": {},
         "analyst_pass": {}, "analyst_fail": {}, "api_errors": 0, "rugcheck_ok": 0, "rugcheck_fail": 0, "rpc_fallback": 0,
         "last_loop": None, "last_risk_tick": None, "risk_ticks": 0, "pauses": 0, "paused_secs": 0}

# ---------------- Scout ----------------
GT_PATHS = (["new_pools?page=%d" % i for i in (1, 2, 3, 4, 5)] +
            ["trending_pools?duration=%s&page=%d" % (d, p) for d in ("5m", "1h", "6h", "24h") for p in (1, 2)] +
            ["pools?sort=h24_tx_count_desc&page=%d" % i for i in (1, 2, 3)] +
            ["dexes/%s/pools?sort=h24_tx_count_desc" % d for d in ("pumpswap", "raydium", "raydium-launchlab",
             "meteora", "meteora-damm-v2", "meteora-dbc", "pump-fun", "letsbonk-fun", "bags-fm", "orca", "raydium-clmm")])
SEARCH_Q = ("pump", "solana", "SOL meme", "pumpswap", "raydium", "meteora", "bonk", "AI", "cat", "dog", "pepe", "trump",
            "moon", "inu", "coin", "GTA", "king", "launchlab", "bags")
def scout():
    src = {}
    def add(m, s):
        if m and m != SOL and m not in src: src[m] = s
    for path in ("/token-profiles/latest/v1", "/token-boosts/latest/v1", "/token-boosts/top/v1", "/community-takeovers/latest/v1"):
        d = get(DS + path, "dsslow", 1.1)
        if d is None: STATS["api_errors"] += 1
        for x in d if isinstance(d, list) else []:
            if x.get("chainId") == "solana": add(x.get("tokenAddress"), "ds" + path.split("/")[1])
    for path in GT_PATHS:   # GeckoTerminal free tier ~30 req/min -> 2.2 s gap
        d = get(GT + "/" + path, "gt", 2.2)
        if d is None: STATS["api_errors"] += 1
        for x in (d or {}).get("data") or []:
            try: add(x["relationships"]["base_token"]["data"]["id"].split("_", 1)[1], "gt:" + path.split("?")[0])
            except Exception: pass
    pairs = []
    for q in SEARCH_Q:
        d = get(DS + "/latest/dex/search?q=" + q.replace(" ", "%20"), "dsfast", 0.25)
        for p in (d or {}).get("pairs") or []:
            if p.get("chainId") == "solana": add(p["baseToken"]["address"], "ds-search"); pairs.append(p)
    ms = list(src)
    for i in range(0, len(ms), 30):
        d = get(DS + "/tokens/v1/solana/" + ",".join(ms[i:i+30]), "dsfast", 0.25)
        if isinstance(d, list): pairs += d
        else: STATS["api_errors"] += 1
    best = {}
    for p in pairs:
        if p.get("chainId") != "solana": continue
        m = p["baseToken"]["address"]
        if m == SOL: continue
        liq = (p.get("liquidity") or {}).get("usd") or 0
        if m not in best or liq > ((best[m].get("liquidity") or {}).get("usd") or 0): best[m] = p
    STATS["last_discovered"] = len(src); STATS["last_pairs"] = len(best)
    return list(best.values()), src

def scout_in_range(p):
    created = p.get("pairCreatedAt"); mc = p.get("marketCap") or p.get("fdv")
    if not created or not mc: return False, None, None
    age_h = (time.time() * 1000 - created) / 3.6e6
    return (0.5 <= age_h <= 72 and 300_000 <= mc <= 20_000_000), age_h, mc

# ---------------- Filter data ----------------
_rc_cache = {}
def rugcheck(mint):
    c = _rc_cache.get(mint)
    if c and time.time() - c[0] < RC_CACHE: return c[1]
    d = get(RC.format(mint), "rc", 1.2, timeout=8)
    if isinstance(d, dict) and d.get("token"): STATS["rugcheck_ok"] += 1
    else: STATS["rugcheck_fail"] += 1; d = None
    _rc_cache[mint] = (time.time(), d); return d

def rpc_authorities(mint):
    try:
        throttle("rpc", 0.5)
        r = json.loads(subprocess.run(["curl", "-s", "--max-time", "6", "-H", "content-type: application/json", "-d",
                               json.dumps({"jsonrpc": "2.0", "id": 1, "method": "getAccountInfo",
                               "params": [mint, {"encoding": "jsonParsed"}]}), RPC], capture_output=True, text=True, timeout=10).stdout)
        info = r["result"]["value"]["data"]["parsed"]["info"]
        STATS["rpc_fallback"] += 1
        return info.get("mintAuthority"), info.get("freezeAuthority")
    except Exception:
        return "unknown", "unknown"

def onchain_facts(mint, pair):
    """Returns dict of facts; value 'unknown' where not obtainable."""
    U = "unknown"
    f = {"src": "rugcheck"}
    rc = rugcheck(mint)
    if not rc:
        ma, fa = rpc_authorities(mint)
        f.update(src="rpc_only", mint_auth=ma, freeze_auth=fa, lp_locked_pct=U, top10_pct_orig=U,
                 top10_pct_adj=U, dev_pct=U, past_rug=U, bundle_pct=U, honeypot=U, holders=U)
        return f
    tok = rc.get("token") or {}
    supply = tok.get("supply") or 0
    f["mint_auth"] = tok.get("mintAuthority"); f["freeze_auth"] = tok.get("freezeAuthority")
    # LP: market matching the DexScreener pair, else the largest one
    mk = rc.get("markets") or []
    m = next((x for x in mk if x.get("pubkey") == pair.get("pairAddress")), None)
    if m is None and mk: m = max(mk, key=lambda x: ((x.get("lp") or {}).get("quoteUSD") or 0))
    f["lp_market"] = (m or {}).get("marketType")
    f["lp_locked_pct"] = ((m or {}).get("lp") or {}).get("lpLockedPct", U) if m else U
    # top holders: exclude pool/AMM vaults (+ lockers); adjusted also excludes exchange wallets
    known = rc.get("knownAccounts") or {}
    pool_addrs = set()
    for x in mk:
        pool_addrs |= {x.get("pubkey"), x.get("liquidityA"), x.get("liquidityB")}
    th = rc.get("topHolders")
    if th is None or not supply:
        f["top10_pct_orig"] = f["top10_pct_adj"] = U
    else:
        def is_pool(h):
            for a in (h.get("owner"), h.get("address")):
                if a in pool_addrs: return True
                k = known.get(a)
                if k and k.get("type") in ("AMM", "LOCKER"): return True
            return False
        def is_cex(h):
            for a in (h.get("owner"), h.get("address")):
                k = known.get(a)
                if k and (k.get("type") not in ("AMM", "LOCKER", "CREATOR") or EXCHANGE_PAT.search(k.get("name", ""))): return True
            return False
        o = [h for h in th if not is_pool(h)]
        a = [h for h in o if not is_cex(h)]
        f["top10_pct_orig"] = round(sum(h.get("pct", 0) for h in o[:10]), 2)
        f["top10_pct_adj"] = round(sum(h.get("pct", 0) for h in a[:10]), 2)
    # dev %
    creator = rc.get("creator")
    cb = rc.get("creatorBalance")
    dev = None
    if cb is not None and supply: dev = cb / supply * 100
    if th and creator:
        dh = sum(h.get("pct", 0) for h in th if h.get("owner") == creator)
        dev = max(dev or 0, dh)
    f["dev_pct"] = round(dev, 3) if dev is not None else U
    risks = rc.get("risks") or []
    f["risk_names"] = [r.get("name") for r in risks]
    f["past_rug"] = bool(rc.get("rugged")) or any(re.search(r"rug", r.get("name", ""), re.I) for r in risks)
    # bundled launch: no free bundle API -> PROXY = RugCheck insider-network current holdings % of supply
    nets = rc.get("insiderNetworks")
    if nets is None:
        f["bundle_pct"] = 0.0 if rc.get("graphInsidersDetected") == 0 else U
    elif supply:
        f["bundle_pct"] = round(sum(n.get("currentHolding", 0) or 0 for n in nets) / supply * 100, 2)
    else: f["bundle_pct"] = U
    # honeypot / Token-2022 transfer fee / hook (adjusted only)
    ext = rc.get("token_extensions") or {}
    tf = rc.get("transferFee") or {}
    hp = []
    if (tf.get("pct") or 0) > 0: hp.append("transfer_fee")
    for k in ("transferHook", "permanentDelegate", "transferFeeConfig"):
        if ext.get(k): hp.append(k)
    if ext.get("nonTransferable"): hp.append("nonTransferable")
    das = ext.get("defaultAccountState")
    if das and "frozen" in json.dumps(das).lower(): hp.append("defaultFrozen")
    if any(re.search(r"honeypot|transfer fee|transfer hook|non.?transferable|permanent delegate", n or "", re.I) for n in f["risk_names"]): hp.append("rugcheck_risk")
    f["honeypot"] = hp
    f["holders"] = rc.get("totalHolders") if rc.get("totalHolders") is not None else U
    return f

# ---------------- Filter ----------------
def market_kills(p):
    k = []
    liq = (p.get("liquidity") or {}).get("usd") or 0
    v1 = (p.get("volume") or {}).get("h1") or 0
    c1 = (p.get("priceChange") or {}).get("h1")
    if liq < 40_000: k.append("liquidity<40k")
    if v1 < 50_000: k.append("vol1h<50k")
    if c1 is None: k.append("unknown:price_change_1h")
    elif c1 > 80: k.append("pumped>80%_1h")
    return k

def onchain_kills(f, variant):
    U = "unknown"; k = []
    def chk(val, bad, name):
        if val == U: k.append("unknown:" + name)
        elif bad(val): k.append(name)
    chk(f["mint_auth"], lambda v: v is not None, "mint_authority_not_revoked")
    chk(f["freeze_auth"], lambda v: v is not None, "freeze_authority_not_revoked")
    chk(f["lp_locked_pct"], lambda v: (v or 0) < LP_LOCK_MIN, "lp_not_burned_or_locked")
    chk(f["top10_pct_orig" if variant == "original" else "top10_pct_adj"], lambda v: v > 25, "top10>25%")
    chk(f["dev_pct"], lambda v: v > 3, "dev>3%")
    chk(f["past_rug"], lambda v: v, "past_rugs")
    chk(f["bundle_pct"], lambda v: v > 10, "bundled>10%(proxy:insider_networks)")
    if variant == "adjusted": chk(f["honeypot"], lambda v: len(v) > 0, "honeypot/token2022_transfer_restriction")
    return k

# ---------------- Analyst ----------------
_holder_hist = {}
def analyst(p, f, age_h):
    tx = (p.get("txns") or {}).get("h1") or {}
    b, s = tx.get("buys") or 0, tx.get("sells") or 0
    c1 = (p.get("priceChange") or {}).get("h1") or 0
    c5 = (p.get("priceChange") or {}).get("m5") or 0
    liq = (p.get("liquidity") or {}).get("usd") or 0
    mc = p.get("marketCap") or p.get("fdv") or 1
    clamp = lambda x: max(0.0, min(100.0, x))
    comp = {}
    comp["momentum"] = clamp(50 + 1.25 * c1 * 0.7 + 1.25 * c5 * 0.3 * 4)   # +40% h1 ~ 100
    comp["unique_buyers(proxy:h1_buy_txns)"] = clamp(b / 5)                   # 500 buys/h = 100
    comp["buy_sell_ratio"] = clamp((b / s if s else (2 if b else 0)) * 50)    # 2:1 = 100
    h = f.get("holders"); mint = p["baseToken"]["address"]
    if isinstance(h, int):
        prev = _holder_hist.get(mint)
        if prev and time.time() - prev[0] > 300:
            rate = (h - prev[1]) / ((time.time() - prev[0]) / 3600)          # holders/hour measured by us
            comp["holder_growth(measured)"] = clamp(rate / 2)                 # +200/h = 100
        else:
            comp["holder_growth(holders/age_h)"] = clamp(h / max(age_h, 0.5) / 2)
        if not prev or time.time() - prev[0] > 3600: _holder_hist[mint] = (time.time(), h)
    else:
        comp["holder_growth(unknown->0)"] = 0
    comp["liq_mcap"] = clamp(liq / mc * 500)                                  # 20% = 100
    comp["smart_wallets(neutral,no_free_data)"] = SMART_WALLET_NEUTRAL
    score = sum(comp.values()) / 6.0                                            # equal weights 1/6
    return round(score, 1), {k: round(v, 1) for k, v in comp.items()}


# ---------------- Fast layer (Jupiter) ----------------
DEC = {}           # mint -> decimals
LAT = {"jup_price": [], "jup_quote": [], "dexscreener": [], "rugcheck": []}
def lat(src, ms):
    if ms is None: return
    L = LAT[src]; L.append(ms)
    if len(L) > 5000: del L[:1000]

def jup_prices(mints):
    out = {}; ms_all = []
    mints = list(dict.fromkeys(list(mints) + [SOL]))
    for i in range(0, len(mints), 50):
        d, ms = http(JUP_PRICE + ",".join(mints[i:i+50]), "jup", 0.3, timeout=5, retries=1)
        lat("jup_price", ms); ms_all.append(ms or 0)
        for m, v in (d or {}).items():
            if isinstance(v, dict) and v.get("usdPrice"):
                out[m] = float(v["usdPrice"])
                if v.get("decimals") is not None: DEC[m] = int(v["decimals"])
    return out, max(ms_all) if ms_all else None

def quote(inp, outp, amount_raw):
    d, ms = http(f"{JUP_QUOTE}?inputMint={inp}&outputMint={outp}&amount={int(amount_raw)}&slippageBps=1000",
                 "jup", 0.3, timeout=5, retries=1)
    lat("jup_quote", ms)
    if not d or not d.get("outAmount"): return None, ms
    return d, ms

def quote_buy(mint, usd, solp):
    """USD -> tokens via SOL route. Returns dict or None."""
    if not solp or mint not in DEC: return None
    d, ms = quote(SOL, mint, usd / solp * 1e9)
    if not d: return None
    tokens = int(d["outAmount"]) / 10 ** DEC[mint] * (1 - QUOTE_EXTRA)
    return {"tokens": tokens, "fill": usd / tokens, "impact_pct": float(d.get("priceImpactPct") or 0) * 100, "ms": ms,
            "route": "+".join(r["swapInfo"].get("label", "?") for r in d.get("routePlan", []))}

def quote_sell(mint, tokens, solp):
    if not solp or mint not in DEC: return None
    d, ms = quote(mint, SOL, tokens * 10 ** DEC[mint])
    if not d: return None
    usd = int(d["outAmount"]) / 1e9 * solp * (1 - QUOTE_EXTRA)
    return {"usd": usd, "fill": usd / tokens, "impact_pct": float(d.get("priceImpactPct") or 0) * 100, "ms": ms}

FAST = {"prices": {}, "sol": None, "ts": 0}

# ---------------- Executor / Risk per variant ----------------
LOCK = threading.RLock()
class Book:
    def __init__(s, name, cfg):
        s.name, s.cfg = name, cfg
        os.makedirs(os.path.join(LOG, name), exist_ok=True)
        s.cash = START_EQUITY; s.pos = {}; s.closed = []
        s.day = str(now().date()); s.day_start_eq = START_EQUITY; s.halted_day = None
        s.last_loss_exit = {}; s.entries_day = {}
    def px(s, ps): return FAST["prices"].get(ps["mint"]) or ps.get("last_mid") or ps["entry_mid"]
    def equity(s):
        return s.cash + sum(p["qty"] * s.px(p) * (1 - FALLBACK_SLIP - FALLBACK_FEE) for p in s.pos.values())
    def log(s, kind, obj): jl(f"{s.name}/{kind}.jsonl", {"variant": s.name, **obj})
    def block_reason(s, mint):
        if mint in s.pos: return "already_open"
        if s.cfg.get("max_open") and len(s.pos) >= s.cfg["max_open"]: return "max_open_positions"
        if s.cfg.get("daily_loss") and s.halted_day == str(now().date()): return "daily_loss_limit_halt"
        t = s.last_loss_exit.get(mint)
        if t and time.time() - t < COOLDOWN_AFTER_LOSS_H * 3600: return "cooldown_4h_after_loss"
        if s.entries_day.get(str(now().date()) + mint, 0) >= MAX_ENTRIES_PER_TOKEN_DAY: return "max_2_entries_per_token_day"
        return None
    def enter(s, p, score, ds_ms):
        mint = p["baseToken"]["address"]; sym = p["baseToken"].get("symbol")
        with LOCK:
            why = s.block_reason(mint)
            usd = s.equity() * s.cfg["size"]
            if not why and usd > s.cash: why = "insufficient_cash"
        if why: s.log("skips", {"mint": mint, "symbol": sym, "reason": why, "score": score}); return
        fp, fms = jup_prices([mint]); solp = fp.get(SOL) or FAST["sol"]
        mid_fast = fp.get(mint); mid_slow = float(p.get("priceUsd") or 0)
        mid = mid_fast or mid_slow
        if not mid: return
        q = quote_buy(mint, usd, solp)
        if q:
            tokens, fill, src = q["tokens"], q["fill"], "jupiter_quote"
            rt = quote_sell(mint, tokens, solp)       # round-trip executable cost right now
            rt_cost = (1 - rt["usd"] / usd) * 100 if rt else None
        else:
            fill = mid * (1 + FALLBACK_SLIP); tokens = usd * (1 - FALLBACK_FEE) / fill; src = "fallback_flat"; rt_cost = None
        with LOCK:
            if s.block_reason(mint): return
            s.cash -= usd
            stop = mid * (1 + s.cfg["stop"])     # stop set BEFORE entry, on fast mid
            s.pos[mint] = dict(mint=mint, symbol=sym, pair=p["pairAddress"], entry_mid=mid, fill=fill, qty=tokens, qty0=tokens,
                               cost=usd, stop=stop, peak=mid, trail_on=False, tp_done=0, opened=time.time(), opened_iso=iso(),
                               realized=0.0, score=score, last_mid=mid)
            k = str(now().date()) + mint; s.entries_day[k] = s.entries_day.get(k, 0) + 1
        s.log("trades", {"action": "BUY", "mint": mint, "symbol": sym, "mid_fast": mid_fast, "mid_slow_dexscreener": mid_slow,
                         "fill": fill, "fill_src": src, "fill_vs_mid_pct": round((fill / mid - 1) * 100, 3),
                         "impact_pct": q and round(q["impact_pct"], 3), "roundtrip_cost_pct_now": rt_cost and round(rt_cost, 3),
                         "route": q and q["route"], "usd": round(usd, 2), "qty": tokens, "stop": stop, "score": score,
                         "lat_ms": {"jup_price": fms, "jup_quote": q and q["ms"], "dexscreener": ds_ms}})
    def sell(s, ps, qty, mid, reason):
        q = quote_sell(ps["mint"], qty, FAST["sol"])
        if q: proceeds, fill, src = q["usd"], q["fill"], "jupiter_quote"
        else:
            fill = mid * (1 - FALLBACK_SLIP); proceeds = qty * fill * (1 - FALLBACK_FEE); src = "fallback_flat"
        s.cash += proceeds; ps["qty"] -= qty; ps["realized"] += proceeds
        s.log("trades", {"action": "SELL", "reason": reason, "mint": ps["mint"], "symbol": ps["symbol"], "mid_fast": mid,
                         "stop": ps["stop"], "fill": fill, "fill_src": src, "qty": qty, "proceeds": round(proceeds, 4),
                         "mid_vs_entry_pct": round((mid / ps["entry_mid"] - 1) * 100, 2),
                         "fill_vs_entry_mid_pct": round((fill / ps["entry_mid"] - 1) * 100, 2),
                         "stop_slippage_pct": round((fill / ps["stop"] - 1) * 100, 2) if reason in ("stop", "trailing_stop") else None})
        if reason in ("stop", "trailing_stop", "max_hold", "end_of_run") or ps["qty"] <= ps["qty0"] * 1e-9:
            pnl = ps["realized"] - ps["cost"]
            rec = {"mint": ps["mint"], "symbol": ps["symbol"], "opened": ps["opened_iso"], "closed": iso(),
                   "cost": round(ps["cost"], 4), "proceeds": round(ps["realized"], 4), "pnl": round(pnl, 4),
                   "pnl_pct": round(pnl / ps["cost"] * 100, 2), "exit_reason": reason, "score": ps["score"]}
            s.closed.append(rec); s.log("closed", rec); del s.pos[ps["mint"]]
            if pnl < 0: s.last_loss_exit[ps["mint"]] = time.time()
    def mark(s, mint, mid):
        ps = s.pos.get(mint)
        if not ps: return
        ps["last_mid"] = mid; ps["peak"] = max(ps["peak"], mid); e = ps["entry_mid"]; c = s.cfg
        if s.name == "adjusted":
            if ps["tp_done"] < 1 and mid >= e * 1.30: s.sell(ps, ps["qty0"] / 3, mid, "tp1_+30%"); ps["tp_done"] = 1
            if ps["tp_done"] < 2 and mid >= e * 1.60: s.sell(ps, ps["qty0"] / 3, mid, "tp2_+60%"); ps["tp_done"] = 2
        if not ps["trail_on"] and (ps["peak"] >= e * 1.12 or ps["tp_done"] >= 1):
            ps["trail_on"] = True; s.log("events", {"event": "trail_on", "mint": mint, "symbol": ps["symbol"], "peak": ps["peak"]})
        if ps["trail_on"]: ps["stop"] = max(ps["stop"], ps["peak"] * (1 - c["trail"]))
        if mid <= ps["stop"]: s.sell(ps, ps["qty"], mid, "trailing_stop" if ps["trail_on"] else "stop")
        elif c.get("max_hold_h") and time.time() - ps["opened"] > c["max_hold_h"] * 3600: s.sell(ps, ps["qty"], mid, "max_hold")
    def day_check(s):
        d = str(now().date())
        if d != s.day: s.day = d; s.day_start_eq = s.equity()
        if s.cfg.get("daily_loss") and s.halted_day != d and s.equity() <= s.day_start_eq * (1 - s.cfg["daily_loss"]):
            s.halted_day = d; s.log("events", {"event": "daily_loss_limit_hit", "equity": s.equity()})
    def snapshot(s):
        p = os.path.join(LOG, s.name, "equity.csv"); new = not os.path.exists(p)
        with open(p, "a", newline="") as fh:
            w = csv.writer(fh)
            if new: w.writerow(["ts", "equity", "cash", "open_positions"])
            w.writerow([iso(), round(s.equity(), 4), round(s.cash, 4), len(s.pos)])
    def state(s):
        return {"cash": s.cash, "equity": s.equity(), "open": s.pos, "closed": s.closed, "day": s.day,
                "day_start_eq": s.day_start_eq, "halted_day": s.halted_day, "last_loss_exit": s.last_loss_exit,
                "entries_day": s.entries_day}

BOOKS = [Book("original", {"size": 0.08, "stop": -0.06, "trail": 0.06, "threshold": 70}),
         Book("adjusted", {"size": 0.025, "stop": -0.18, "trail": 0.10, "max_open": 3, "daily_loss": 0.10, "max_hold_h": 6, "threshold": 75})]

# ---------------- divergence fast vs slow ----------------
DIV = []   # (abs_div_pct, fast_below_slow_by_more_than_costs)
def record_div(mint, sym, fast, slow, fms, sms, ctx):
    if not fast or not slow: return
    dv = (fast / slow - 1) * 100
    DIV.append(dv)
    if len(DIV) > 20000: del DIV[:5000]
    jl("divergence.jsonl", {"ctx": ctx, "mint": mint, "symbol": sym, "fast_jup": fast, "slow_ds": slow,
                            "div_pct": round(dv, 3), "jup_ms": fms, "ds_ms": sms, "gt_costs": abs(dv) > COST_RT_FLAT * 100})

def save_state():
    st = {k: (len(v) if isinstance(v, set) else v) for k, v in STATS.items()}
    st["unique_token_list"] = sorted(STATS["unique_tokens"])
    with LOCK: st["books"] = json.loads(json.dumps({b.name: b.state() for b in BOOKS}, default=str))
    st["fast_prices_age_s"] = round(time.time() - FAST["ts"], 1) if FAST["ts"] else None
    st["config"] = {"start_equity": START_EQUITY, "fallback_slip": FALLBACK_SLIP, "fallback_fee": FALLBACK_FEE,
                    "quote_extra": QUOTE_EXTRA, "cost_rt_flat_pct": COST_RT_FLAT * 100, "end_at": END_AT.isoformat(), "pid": os.getpid()}
    tmp = os.path.join(BASE, "state.json.tmp")
    with open(tmp, "w") as fh: json.dump(st, fh, default=str)
    os.replace(tmp, os.path.join(BASE, "state.json"))

# ---------------- Risk thread (fast) ----------------
def risk_loop():
    last_slow = last_snap = 0
    prev = time.time()
    while keep_running():
        t0 = time.time()
        if t0 - prev > 20:
            STATS["pauses"] = STATS.get("pauses", 0) + 1; STATS["paused_secs"] = STATS.get("paused_secs", 0) + round(t0 - prev)
            jl("events.jsonl", {"event": "tick_gap_box_pause", "secs": round(t0 - prev, 1)})
        prev = t0
        try:
            with LOCK: mints = {m for b in BOOKS for m in b.pos}
            prices, fms = jup_prices(mints)
            if SOL in prices: FAST["sol"] = prices[SOL]
            FAST["prices"].update(prices); FAST["ts"] = time.time()
            if mints and time.time() - last_slow >= SLOW_REF_EVERY:
                last_slow = time.time()
                with LOCK: pairs = {b.pos[m]["pair"]: (m, b.pos[m]["symbol"]) for b in BOOKS for m in b.pos}
                d, sms = http(DS + "/latest/dex/pairs/solana/" + ",".join(list(pairs)[:30]), "dsfast", 0.25, timeout=6, retries=1)
                lat("dexscreener", sms)
                for pp in (d or {}).get("pairs") or []:
                    m, sym = pairs.get(pp.get("pairAddress"), (None, None))
                    if m:
                        slow = float(pp.get("priceUsd") or 0)
                        record_div(m, sym, prices.get(m), slow, fms, sms, "open_position")
                        if m not in prices and slow: FAST["prices"][m] = slow   # fast feed missing -> use slow
            with LOCK:
                for b in BOOKS:
                    for m in list(b.pos):
                        px = FAST["prices"].get(m)
                        if px: b.mark(m, px)
                    b.day_check()
                if time.time() - last_snap >= 30:
                    last_snap = time.time()
                    for b in BOOKS: b.snapshot()
            STATS["risk_ticks"] += 1; STATS["last_risk_tick"] = iso(); STATS["last_risk_tick_ms"] = round((time.time() - t0) * 1000)
            save_state()
        except Exception as e:
            jl("events.jsonl", {"event": "risk_error", "err": repr(e), "tb": traceback.format_exc()[-1500:]})
        time.sleep(max(0.2, RISK_EVERY - (time.time() - t0)))

# ---------------- Scan thread (slow) ----------------
_last_eval = {}
def scan_once():
    t0 = time.time()
    pairs, src = scout(); STATS["scan_loops"] += 1
    ds_ms = round((time.time() - t0) * 1000)
    inr = []
    for p in pairs:
        ok, age_h, mc = scout_in_range(p)
        if ok: inr.append((p, age_h, mc))
    # fast vs slow divergence on every in-range candidate
    fp, fms = jup_prices([p["baseToken"]["address"] for p, _, _ in inr]) if inr else ({}, None)
    for p, _, _ in inr:
        record_div(p["baseToken"]["address"], p["baseToken"].get("symbol"), fp.get(p["baseToken"]["address"]),
                   float(p.get("priceUsd") or 0), fms, None, "scan_candidate")
    STATS["last_in_range"] = len(inr)
    for p, age_h, mc in inr:
        mint = p["baseToken"]["address"]
        if time.time() - _last_eval.get(mint, 0) < REEVAL_AFTER: continue
        _last_eval[mint] = time.time()
        s = src.get(mint, "?"); dbs = STATS["discovered_by_source"]
        if mint not in STATS["unique_tokens"]: dbs[s] = dbs.get(s, 0) + 1
        STATS["scout_in_range"] += 1; STATS["evaluations"] += 1; STATS["unique_tokens"].add(mint)
        base = {"mint": mint, "symbol": p["baseToken"].get("symbol"), "pair": p.get("pairAddress"), "dex": p.get("dexId"),
                "source": s, "age_h": round(age_h, 2), "mcap": mc, "liq": (p.get("liquidity") or {}).get("usd"),
                "vol1h": (p.get("volume") or {}).get("h1"), "chg1h": (p.get("priceChange") or {}).get("h1")}
        mk = market_kills(p); facts = None; per = {}
        if mk: per = {b.name: mk for b in BOOKS}
        else:
            t1 = time.time(); facts = onchain_facts(mint, p); lat("rugcheck", round((time.time() - t1) * 1000))
            per = {b.name: onchain_kills(facts, b.name) for b in BOOKS}
        for b in BOOKS:
            k = per[b.name]
            if not k: continue
            ks = STATS["kills_primary"].setdefault(b.name, {}); ks[k[0]] = ks.get(k[0], 0) + 1
            ka = STATS["kills_any"].setdefault(b.name, {})
            for r in k: ka[r] = ka.get(r, 0) + 1
            if all(r.startswith("unknown:") for r in k):
                STATS["kills_only_unknown"][b.name] = STATS["kills_only_unknown"].get(b.name, 0) + 1
            jl("kills.jsonl", {"variant": b.name, **base, "reasons": k, "facts": facts})
        surv = [b for b in BOOKS if not per[b.name]]
        if not surv: continue
        score, comp = analyst(p, facts, age_h)
        res = {}
        for b in surv:
            ok = score >= b.cfg["threshold"]; res[b.name] = ok
            d = STATS["analyst_pass" if ok else "analyst_fail"]; d[b.name] = d.get(b.name, 0) + 1
        jl("analyst.jsonl", {**base, "score": score, "components": comp, "pass": res, "facts": facts})
        for b in surv:
            if res[b.name]: b.enter(p, score, ds_ms)
    STATS["last_scan_secs"] = round(time.time() - t0, 1)

def resume():
    p = os.path.join(BASE, "state.json")
    if not os.path.exists(p): return
    st = json.load(open(p))
    for k in STATS:
        if k in st and k != "unique_tokens": STATS[k] = st[k]
    STATS["unique_tokens"] = set(st.get("unique_token_list", []))
    for b in BOOKS:
        bs = st["books"][b.name]
        for k in ("cash", "closed", "day", "day_start_eq", "halted_day", "last_loss_exit", "entries_day"): setattr(b, k, bs[k])
        b.pos = bs["open"]
    jl("events.jsonl", {"event": "resumed", "open": {b.name: len(b.pos) for b in BOOKS}})

def main():
    os.makedirs(LOG, exist_ok=True)
    resume()
    jl("events.jsonl", {"event": "start", "pid": os.getpid(), "end_at": END_AT.isoformat(),
                        "chunk_until": CHUNK_UNTIL.isoformat() if CHUNK_UNTIL else None})
    th = threading.Thread(target=risk_loop, daemon=True, name="risk"); th.start()
    while keep_running():
        t0 = time.time()
        try:
            scan_once(); STATS["last_loop"] = iso()
            if time.time() - t0 > 240: jl("events.jsonl", {"event": "slow_scan", "secs": round(time.time() - t0, 1)})
        except Exception as e:
            jl("events.jsonl", {"event": "scan_error", "err": repr(e), "tb": traceback.format_exc()[-1500:]})
        time.sleep(max(5, SCAN_EVERY - (time.time() - t0)))
    th.join(timeout=30)
    if now() >= END_AT:
        prices, _ = jup_prices({m for b in BOOKS for m in b.pos}); FAST["prices"].update(prices)
        with LOCK:
            for b in BOOKS:
                for ps in list(b.pos.values()): b.sell(ps, ps["qty"], b.px(ps), "end_of_run")
                b.snapshot()
        save_state(); jl("events.jsonl", {"event": "end"})
    else:
        with LOCK:
            for b in BOOKS: b.snapshot()
        save_state(); jl("events.jsonl", {"event": "chunk_end",
                                         "chunk_until": CHUNK_UNTIL.isoformat() if CHUNK_UNTIL else None})

if __name__ == "__main__": main()
