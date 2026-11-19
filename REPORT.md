# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2406 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan None (Nones) | last risk tick 2026-11-19T18:34:24-05:00 (502 ms) | risk ticks 47
Scan loops 1 | last scan: discovered 460 tokens, 459 pairs, 19 in Scout range
Evaluations 2 | unique tokens evaluated 2 | RugCheck ok/fail 1/0 | API errors 15
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                        1/0               0/1
Evaluations killed                           0                 0
Closed trades                                0                 0
Win rate                                   n/a               n/a
Avg win %                                  n/a               n/a
Avg loss %                                 n/a               n/a
Realized P&L $                           +0.00             +0.00
Equity $ (MTM)                          998.21           1000.00
Total P&L $                              -1.79             +0.00
Cash $                                  920.00           1000.00
Open positions                               1                 0
Daily-loss halt                              -                 -

Kills by PRIMARY reason:

Kills by ANY reason:
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=3, median 65.2, max 70.8): {'50-54': 1, '65-69': 1, '70-74': 1}

[original] entry blocks: -
  OPEN OGTA       entry 0.000911889 last 0.000911889 (+0.0%) stop 0.000857176 trail off cost $80.00 since 2026-11-19T18:34:23-05:00
  buys: 1 (1 filled at Jupiter quote), fill vs fast mid median +0.96%, round-trip executable cost median 3.09%

[adjusted] entry blocks: -

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n=    39 median      32  p95     145  max     422
  http:lite-api.jup.ag/price n=    49 median      35  p95     132  max     214
  http:api.geckoterminal.com n=    12 median      32  p95     287  max     287
  http:api.rugcheck.xyz      n=     4 median     376  p95     382  max     382
  http:lite-api.jup.ag/quote n=     2 median      30  p95      30  max      30
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=6: median |div| 0.40%, max |div| 7.05%, |div|>2.6% costs: 2, fast BELOW slow by >2.6%: 2
```
