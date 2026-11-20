# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2406 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-19T23:14:57-05:00 (137.1s) | last risk tick 2026-11-19T23:15:24-05:00 (60 ms) | risk ticks 5667
Scan loops 118 | last scan: discovered 437 tokens, 437 pairs, 23 in Scout range
Evaluations 542 | unique tokens evaluated 36 | RugCheck ok/fail 132/0 | API errors 1792
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 3, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 7, 'ds-search': 6, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 13, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                       8/65              3/70
Evaluations killed                         469               469
Closed trades                                4                 3
Win rate                                  0.0%              0.0%
Avg win %                                  n/a               n/a
Avg loss %                               -9.12            -24.11
Realized P&L $                          -28.86            -17.97
Equity $ (MTM)                          971.14            982.03
Total P&L $                             -28.86            -17.97
Cash $                                  971.14            982.03
Open positions                               0                 0
Daily-loss halt                              -                 -

Kills by PRIMARY reason:
  bundled>10%(proxy:insider_networks)                 27      27
  liquidity<40k                                      327     327
  mint_authority_not_revoked                          24      24
  pumped>80%_1h                                       25      25
  top10>25%                                            8       8
  vol1h<50k                                           58      58

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                 51      51
  freeze_authority_not_revoked                        24      24
  honeypot/token2022_transfer_restriction              0      24
  liquidity<40k                                      327     327
  lp_not_burned_or_locked                             24      24
  mint_authority_not_revoked                          24      24
  pumped>80%_1h                                       32      32
  top10>25%                                           32      32
  unknown:price_change_1h                            326     326
  vol1h<50k                                          380     380
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=73, median 52.7, max 85.0): {'40-44': 4, '45-49': 14, '50-54': 29, '55-59': 9, '60-64': 4, '65-69': 5, '70-74': 5, '75-79': 1, '80-84': 1, '85-89': 1}

[original] entry blocks: {'cooldown_4h_after_loss': 4}
  CLOSED OGTA         -7.51%  $-6.01  stop  18:34:23 -> 18:35:24
  CLOSED AI           -9.62%  $-7.65  stop  18:58:26 -> 18:59:06
  CLOSED LOOSY       -11.06%  $-8.73  stop  21:58:13 -> 22:00:54
  CLOSED iAgent       -8.28%  $-6.47  stop  23:12:35 -> 23:15:00
  stop exits: fill vs stop level median -1.40%, worst -3.17% (n=4)
  buys: 4 (4 filled at Jupiter quote), fill vs fast mid median +1.78%, round-trip executable cost median 2.79%

[adjusted] entry blocks: -
  CLOSED AI          -30.26%  $-7.56  stop  18:58:29 -> 19:02:42
  CLOSED OGTA        -21.49%  $-5.33  stop  19:58:11 -> 20:01:36
  CLOSED LOOSY       -20.57%  $-5.08  stop  21:58:16 -> 22:18:00
  stop exits: fill vs stop level median -2.99%, worst -6.10% (n=3)
  buys: 3 (3 filled at Jupiter quote), fill vs fast mid median +1.68%, round-trip executable cost median 2.67%

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n=  4587 median      33  p95     115  max    1135
  http:lite-api.jup.ag/price n=  5788 median      41  p95     125  max    2199
  http:api.geckoterminal.com n=  1399 median      35  p95     350  max    1397
  http:api.rugcheck.xyz      n=   132 median     369  p95     895  max    2075
  http:lite-api.jup.ag/quote n=    21 median      37  p95     104  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=972: median |div| 1.17%, max |div| 50.82%, |div|>2.6% costs: 262, fast BELOW slow by >2.6%: 170
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=59: median |div| 2.12%, max |div| 11.58%, |div|>2.6% costs: 22, fast BELOW slow by >2.6%: 17
```
