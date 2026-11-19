# MemeDesk paper-trading data

This branch is written by the `memedesk` GitHub Actions workflow. It is the live state of a **simulation**. There are no wallets, keys, or orders here.

- [`REPORT.md`](REPORT.md) — both variants side by side
- `state.json` — equity, open positions, and scan counters (the resume file)
- `logs/` — trades, skips, latency, supervisor
- `chunk.json` — which Actions run last wrote this commit

Do not edit this branch by hand. The next snapshot overwrites these files from the runner.
