# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2406 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-19T23:34:15-05:00 (143.0s) | last risk tick 2026-11-19T23:35:30-05:00 (35 ms) | risk ticks 6069
Scan loops 126 | last scan: discovered 462 tokens, 461 pairs, 12 in Scout range
Evaluations 582 | unique tokens evaluated 36 | RugCheck ok/fail 143/0 | API errors 1919
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 3, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 7, 'ds-search': 6, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 13, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                       9/71              4/76
Evaluations killed                         502               502
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
  bundled>10%(proxy:insider_networks)                 29      29
  liquidity<40k                                      352     352
  mint_authority_not_revoked                          26      26
  pumped>80%_1h                                       25      25
  top10>25%                                            8       8
  vol1h<50k                                           62      62

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                 55      55
  freeze_authority_not_revoked                        26      26
  honeypot/token2022_transfer_restriction              0      26
  liquidity<40k                                      352     352
  lp_not_burned_or_locked                             26      26
  mint_authority_not_revoked                          26      26
  pumped>80%_1h                                       32      32
  top10>25%                                           34      34
  unknown:price_change_1h                            347     347
  vol1h<50k                                          409     409
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=80, median 53.0, max 85.0): {'40-44': 4, '45-49': 14, '50-54': 33, '55-59': 11, '60-64': 4, '65-69': 5, '70-74': 5, '75-79': 2, '80-84': 1, '85-89': 1}

[original] entry blocks: {'cooldown_4h_after_loss': 5}
  CLOSED OGTA         -7.51%  $-6.01  stop  18:34:23 -> 18:35:24
  CLOSED AI           -9.62%  $-7.65  stop  18:58:26 -> 18:59:06
  CLOSED LOOSY       -11.06%  $-8.73  stop  21:58:13 -> 22:00:54
  CLOSED iAgent       -8.28%  $-6.47  stop  23:12:35 -> 23:15:00
  stop exits: fill vs stop level median -1.40%, worst -3.17% (n=4)
  buys: 4 (4 filled at Jupiter quote), fill vs fast mid median +1.78%, round-trip executable cost median 2.79%

[adjusted] entry blocks: {'cooldown_4h_after_loss': 1}
  CLOSED AI          -30.26%  $-7.56  stop  18:58:29 -> 19:02:42
  CLOSED OGTA        -21.49%  $-5.33  stop  19:58:11 -> 20:01:36
  CLOSED LOOSY       -20.57%  $-5.08  stop  21:58:16 -> 22:18:00
  stop exits: fill vs stop level median -2.99%, worst -6.10% (n=3)
  buys: 3 (3 filled at Jupiter quote), fill vs fast mid median +1.68%, round-trip executable cost median 2.67%

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n=  4894 median      33  p95     115  max    1135
  http:lite-api.jup.ag/price n=  6198 median      40  p95     125  max    2199
  http:api.geckoterminal.com n=  1498 median      35  p95     345  max    1397
  http:api.rugcheck.xyz      n=   143 median     368  p95     880  max    2075
  http:lite-api.jup.ag/quote n=    21 median      37  p95     104  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=1044: median |div| 1.18%, max |div| 50.82%, |div|>2.6% costs: 278, fast BELOW slow by >2.6%: 182
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=59: median |div| 2.12%, max |div| 11.58%, |div|>2.6% costs: 22, fast BELOW slow by >2.6%: 17
```
