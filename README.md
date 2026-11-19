# MemeDesk — paper trading on GitHub Actions

Simulation only. No wallets, no private keys, no signing, no real orders. Jupiter quotes are read-only. Each variant (`original` and `adjusted`) starts with $1,000 of simulated equity.

The strategy loop is `desk.py`. It runs on GitHub Actions because a long-lived machine pauses when idle. A single Actions job cannot run past 6 hours, so the work is split into chunks of about 5 hours 40 minutes. Each chunk resumes from the last snapshot and, before it exits, starts the next one.

## How a chunk hands off

Workflow: [`.github/workflows/memedesk.yml`](.github/workflows/memedesk.yml).

1. The job checks out `main` (the strategy) and restores `state.json` plus `logs/` from the [`data`](../../tree/data) branch.
2. `run.sh` starts `desk.py` and restarts it if it crashes or if `state.json` stops updating. Open positions, equity, and counters resume from `state.json`.
3. About every 10 minutes, and once more when the chunk stops, the job commits `state.json`, `logs/`, `chunk.json`, and `REPORT.md` to `data`.
4. If the strategy end time is still in the future, the job calls `workflow_dispatch` on this workflow (the `GITHUB_TOKEN` has `contents: write` and `actions: write`). The new run waits on the `memedesk-paper` concurrency group, so it starts as this job exits and does not overlap it.
5. A cron every 30 minutes starts a chunk only when none is running (same concurrency group, `cancel-in-progress: false`). That covers a chunk that dies before it can hand off.

`REPORT.md` on the `data` branch is the text report from `report.py`, with both variants side by side.

## When it stops

Default end: **2026-11-20 14:00 UTC** (09:00 America/Panama).

- A manual run can pass a different `end_at` (ISO-8601 UTC) and `chunk_minutes`. Later chunks keep that end time.
- The backup cron keeps the end time stored in `data`/`chunk.json`.
- After the end time, new chunks do not start. If anything is still open, one short run marks those positions to market (`end_of_run`) using the same read-only quotes as the rest of the simulator.
- The 30-minute cron keeps firing after that and exits immediately while nothing is open. Disable the workflow in the Actions tab once the run is finished if you do not want those empty checks.

## Strategy (unchanged)

Scout sources: DexScreener token-profiles/boosts (latest, top) / community-takeovers plus 19 search queries. GeckoTerminal is address discovery only: new pools pages 1–5, trending 5m/1h/6h/24h pages 1–2, top pools by transactions pages 1–3, and per-DEX top pools (pumpswap, raydium, raydium-launchlab, meteora, meteora-damm-v2, meteora-dbc, pump-fun, letsbonk-fun, bags-fm, orca, raydium-clmm). pump.fun's own API is not used. Metrics and filters use DexScreener pair data and RugCheck.

Thresholds: original 70, adjusted 75. Fast prices: Jupiter Price API v3 (`lite-api.jup.ag/price/v3`). Fills: Jupiter Quote API for the simulated size, plus 0.4% per side (0.1% network/priority + 0.3% latency). If a quote is missing: 1% slippage + 0.3% fee per side. Both variants skip re-entry for 4 hours after a losing exit and allow at most 2 entries per token per day.

`original`: 8% per trade, stop −6%, trailing 6% from the peak after +12%. `adjusted`: 2.5% per trade, max 3 open, daily loss 10%, stop −18%, take profit 1/3 at +30% and 1/3 at +60%, trailing 10% from the peak after +12% (or after the first take-profit), max hold 6 hours.

Public APIs only: DexScreener, GeckoTerminal, RugCheck, Jupiter price/quote, and the public Solana RPC. No API keys.

## Files

| Path | Role |
| --- | --- |
| `desk.py` | Simulator. `MEMEDESK_END_AT` / `MEMEDESK_CHUNK_UNTIL` only change when it stops. |
| `run.sh` | Restarts `desk.py` inside one chunk. |
| `report.py` | Side-by-side report. |
| `scripts/actions_chunk.sh` | Restore, run, snapshot, hand off. |
| `data` branch | Live `state.json`, `logs/`, `REPORT.md`. Not on `main`. |
