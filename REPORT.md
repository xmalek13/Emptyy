# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2406 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-19T22:02:58-05:00 (137.5s) | last risk tick 2026-11-19T22:05:09-05:00 (39 ms) | risk ticks 4262
Scan loops 88 | last scan: discovered 443 tokens, 442 pairs, 23 in Scout range
Evaluations 398 | unique tokens evaluated 34 | RugCheck ok/fail 89/0 | API errors 1348
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 2, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 7, 'ds-search': 6, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 12, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                       7/44              3/48
Evaluations killed                         347               347
Closed trades                                3                 2
Win rate                                  0.0%              0.0%
Avg win %                                  n/a               n/a
Avg loss %                               -9.40            -25.88
Realized P&L $                          -22.38            -12.90
Equity $ (MTM)                          977.62            985.65
Total P&L $                             -22.38            -14.35
Cash $                                  977.62            962.43
Open positions                               0                 1
Daily-loss halt                              -                 -

Kills by PRIMARY reason:
  bundled>10%(proxy:insider_networks)                 17      17
  liquidity<40k                                      238     238
  mint_authority_not_revoked                          18      18
  pumped>80%_1h                                       25      25
  top10>25%                                            3       3
  vol1h<50k                                           46      46

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                 35      35
  freeze_authority_not_revoked                        18      18
  honeypot/token2022_transfer_restriction              0      18
  liquidity<40k                                      238     238
  lp_not_burned_or_locked                             18      18
  mint_authority_not_revoked                          18      18
  pumped>80%_1h                                       31      31
  top10>25%                                           21      21
  unknown:price_change_1h                            241     241
  vol1h<50k                                          280     280
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=51, median 52.7, max 85.0): {'40-44': 3, '45-49': 9, '50-54': 21, '55-59': 4, '60-64': 3, '65-69': 4, '70-74': 4, '75-79': 1, '80-84': 1, '85-89': 1}

[original] entry blocks: {'cooldown_4h_after_loss': 4}
  CLOSED OGTA         -7.51%  $-6.01  stop  18:34:23 -> 18:35:24
  CLOSED AI           -9.62%  $-7.65  stop  18:58:26 -> 18:59:06
  CLOSED LOOSY       -11.06%  $-8.73  stop  21:58:13 -> 22:00:54
  stop exits: fill vs stop level median -1.56%, worst -3.17% (n=3)
  buys: 3 (3 filled at Jupiter quote), fill vs fast mid median +2.33%, round-trip executable cost median 2.91%

[adjusted] entry blocks: -
  OPEN LOOSY      entry 0.001427 last 0.00138341 (-3.1%) stop 0.00117014 trail off cost $24.68 since 2026-11-19T21:58:16-05:00
  CLOSED AI          -30.26%  $-7.56  stop  18:58:29 -> 19:02:42
  CLOSED OGTA        -21.49%  $-5.33  stop  19:58:11 -> 20:01:36
  stop exits: fill vs stop level median -4.54%, worst -6.10% (n=2)
  buys: 3 (3 filled at Jupiter quote), fill vs fast mid median +1.68%, round-trip executable cost median 2.67%

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n=  3408 median      33  p95     117  max    1135
  http:lite-api.jup.ag/price n=  4352 median      42  p95     126  max    2199
  http:api.geckoterminal.com n=  1054 median      35  p95     350  max     913
  http:api.rugcheck.xyz      n=    89 median     369  p95     895  max    2075
  http:lite-api.jup.ag/quote n=    17 median      37  p95     160  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=711: median |div| 1.25%, max |div| 50.82%, |div|>2.6% costs: 204, fast BELOW slow by >2.6%: 124
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=30: median |div| 2.37%, max |div| 7.06%, |div|>2.6% costs: 12, fast BELOW slow by >2.6%: 9
```
