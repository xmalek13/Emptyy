#!/usr/bin/env python3
"""MemeDesk v2 report (PAPER ONLY): both variants side by side + fast/slow feed latency & divergence stats."""
import json, os, statistics as stt
B = os.path.dirname(os.path.abspath(__file__)); L = os.path.join(B, "logs")
st = json.load(open(os.path.join(B, "state.json")))
def jsonl(n):
    p = os.path.join(L, n)
    if not os.path.exists(p):
        return []
    out = []
    with open(p) as fh:
        for x in fh:
            x = x.strip()
            if not x:
                continue
            try:
                out.append(json.loads(x))
            except Exception:
                continue  # torn last line if the file was copied mid-append
    return out
pid = (st.get("config") or {}).get("pid")
alive = bool(pid) and os.path.exists(f"/proc/{pid}")
print(f"MemeDesk v2 PAPER TRADING (simulated) | started {st['started']} | ends {st['config']['end_at']} | pid {st['config']['pid']} {'RUNNING' if alive else 'NOT RUNNING'}")
print(f"Box pauses seen by risk thread: {st.get('pauses',0)} ({st.get('paused_secs',0)} s total)")
print(f"Last scan {st['last_loop']} ({st.get('last_scan_secs')}s) | last risk tick {st['last_risk_tick']} ({st.get('last_risk_tick_ms')} ms) | risk ticks {st['risk_ticks']}")
print(f"Scan loops {st['scan_loops']} | last scan: discovered {st.get('last_discovered')} tokens, {st.get('last_pairs')} pairs, {st.get('last_in_range')} in Scout range")
print(f"Evaluations {st['evaluations']} | unique tokens evaluated {st['unique_tokens']} | RugCheck ok/fail {st['rugcheck_ok']}/{st['rugcheck_fail']} | API errors {st['api_errors']}")
print("Unique evaluated tokens by discovery source:", st.get("discovered_by_source"))
names = ["original", "adjusted"]
def stats(n):
    b = st["books"][n]; c = b["closed"]; w = [x for x in c if x["pnl"] > 0]; l = [x for x in c if x["pnl"] <= 0]
    avg = lambda xs: sum(x["pnl_pct"] for x in xs) / len(xs) if xs else 0
    return {"Analyst pass / fail": f"{st['analyst_pass'].get(n,0)}/{st['analyst_fail'].get(n,0)}",
            "Evaluations killed": sum(st["kills_primary"].get(n, {}).values()),
            "Closed trades": len(c), "Win rate": f"{len(w)/len(c)*100:.1f}%" if c else "n/a",
            "Avg win %": f"{avg(w):+.2f}" if w else "n/a", "Avg loss %": f"{avg(l):+.2f}" if l else "n/a",
            "Realized P&L $": f"{sum(x['pnl'] for x in c):+.2f}", "Equity $ (MTM)": f"{b['equity']:.2f}",
            "Total P&L $": f"{b['equity']-st['config']['start_equity']:+.2f}", "Cash $": f"{b['cash']:.2f}",
            "Open positions": len(b["open"]), "Daily-loss halt": b.get("halted_day") or "-"}
rows = {n: stats(n) for n in names}
print(f"\n{'':28}{'ORIGINAL (>=70)':>18}{'ADJUSTED (>=75)':>18}")
for k in rows["original"]: print(f"{k:28}{str(rows['original'][k]):>18}{str(rows['adjusted'][k]):>18}")
for title, key in (("Kills by PRIMARY reason", "kills_primary"), ("Kills by ANY reason", "kills_any")):
    print(f"\n{title}:"); allr = sorted(set().union(*[st[key].get(n, {}).keys() for n in names]))
    for r in allr: print(f"  {r:46}{st[key].get('original',{}).get(r,0):>8}{st[key].get('adjusted',{}).get(r,0):>8}")
ku = st.get("kills_only_unknown", {})
print(f"  {'(kills caused ONLY by unknown data)':46}{ku.get('original',0):>8}{ku.get('adjusted',0):>8}")
an = jsonl("analyst.jsonl"); sc = [a["score"] for a in an]
if sc:
    bk = {}
    for s in sc: k = f"{int(s//5*5)}-{int(s//5*5)+4}"; bk[k] = bk.get(k, 0) + 1
    print(f"\nAnalyst score distribution (n={len(sc)}, median {stt.median(sc):.1f}, max {max(sc)}):", dict(sorted(bk.items())))
for n in names:
    skips = jsonl(f"{n}/skips.jsonl"); sk = {}
    for s in skips: sk[s["reason"]] = sk.get(s["reason"], 0) + 1
    print(f"\n[{n}] entry blocks: {sk or '-'}")
    for p in st["books"][n]["open"].values():
        lm = p.get("last_mid") or p["entry_mid"]
        print(f"  OPEN {p['symbol']:10} entry {p['entry_mid']:.6g} last {lm:.6g} ({(lm/p['entry_mid']-1)*100:+.1f}%) stop {p['stop']:.6g} trail {'on' if p['trail_on'] else 'off'} cost ${p['cost']:.2f} since {p['opened_iso']}")
    for c in st["books"][n]["closed"][-15:]:
        print(f"  CLOSED {c['symbol']:10} {c['pnl_pct']:+7.2f}%  ${c['pnl']:+.2f}  {c['exit_reason']}  {c['opened'][11:19]} -> {c['closed'][11:19]}")
    sells = [t for t in jsonl(f"{n}/trades.jsonl") if t["action"] == "SELL" and t.get("stop_slippage_pct") is not None]
    if sells: print(f"  stop exits: fill vs stop level median {stt.median(t['stop_slippage_pct'] for t in sells):+.2f}%, worst {min(t['stop_slippage_pct'] for t in sells):+.2f}% (n={len(sells)})")
    buys = [t for t in jsonl(f"{n}/trades.jsonl") if t["action"] == "BUY"]
    q = [t for t in buys if t["fill_src"] == "jupiter_quote"]
    if buys: print(f"  buys: {len(buys)} ({len(q)} filled at Jupiter quote)" + (f", fill vs fast mid median {stt.median(t['fill_vs_mid_pct'] for t in q):+.2f}%, round-trip executable cost median {stt.median([t['roundtrip_cost_pct_now'] for t in q if t['roundtrip_cost_pct_now'] is not None] or [0]):.2f}%" if q else ""))
# latency / divergence
lat = {}
for x in jsonl("latency.jsonl"):
    if x.get("status", 200) == 200: lat.setdefault(x["src"], []).append(x["ms"])
def pct(v, p): v = sorted(v); return v[min(len(v) - 1, int(len(v) * p))]
print("\nLatency per source (ms, every HTTP call incl. retries; status 200 only):")
for k, v in lat.items():
    v = [x for x in v if x is not None]
    if v: print(f"  {k:26} n={len(v):6} median {stt.median(v):7.0f}  p95 {pct(v, .95):7.0f}  max {max(v):7.0f}")
dv = jsonl("divergence.jsonl"); thr = st["config"]["cost_rt_flat_pct"]
for ctx in ("scan_candidate", "open_position"):
    d = [x["div_pct"] for x in dv if x["ctx"] == ctx]
    if d:
        a = [abs(x) for x in d]
        print(f"Divergence fast(Jupiter) vs slow(DexScreener) [{ctx}] n={len(d)}: median |div| {stt.median(a):.2f}%, max |div| {max(a):.2f}%, "
              f"|div|>{thr:.1f}% costs: {sum(x > thr for x in a)}, fast BELOW slow by >{thr:.1f}%: {sum(x < -thr for x in d)}")
