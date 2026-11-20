# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2252 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-20T00:12:38-05:00 (Nones) | last risk tick 2026-11-20T00:13:29-05:00 (72 ms) | risk ticks 6807
Scan loops 142 | last scan: discovered None tokens, None pairs, None in Scout range
Evaluations 657 | unique tokens evaluated 36 | RugCheck ok/fail 159/0 | API errors 2155
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 3, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 7, 'ds-search': 6, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 13, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                      14/76              5/85
Evaluations killed                         567               567
Closed trades                                4                 4
Win rate                                  0.0%              0.0%
Avg win %                                  n/a               n/a
Avg loss %                               -9.12            -23.77
Realized P&L $                          -28.86            -23.56
Equity $ (MTM)                          971.14            976.44
Total P&L $                             -28.86            -23.56
Cash $                                  971.14            976.44
Open positions                               0                 0
Daily-loss halt                              -                 -

Kills by PRIMARY reason:
  bundled>10%(proxy:insider_networks)                 32      32
  liquidity<40k                                      401     401
  mint_authority_not_revoked                          29      29
  pumped>80%_1h                                       25      25
  top10>25%                                            8       8
  vol1h<50k                                           72      72

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                 61      61
  freeze_authority_not_revoked                        29      29
  honeypot/token2022_transfer_restriction              0      29
  liquidity<40k                                      401     401
  lp_not_burned_or_locked                             29      29
  mint_authority_not_revoked                          29      29
  pumped>80%_1h                                       32      32
  top10>25%                                           37      37
  unknown:price_change_1h                            393     393
  vol1h<50k                                          468     468
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=90, median 53.7, max 85.0): {'40-44': 4, '45-49': 14, '50-54': 34, '55-59': 13, '60-64': 5, '65-69': 6, '70-74': 9, '75-79': 3, '80-84': 1, '85-89': 1}

[original] entry blocks: {'cooldown_4h_after_loss': 10}
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
  CLOSED iAgent      -22.75%  $-5.59  stop  23:48:37 -> 00:00:09
  stop exits: fill vs stop level median -3.88%, worst -6.10% (n=4)
  buys: 4 (4 filled at Jupiter quote), fill vs fast mid median +1.50%, round-trip executable cost median 2.56%

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n=  5532 median      33  p95     113  max    1135
  http:lite-api.jup.ag/price n=  6953 median      40  p95     125  max    2737
  http:api.geckoterminal.com n=  1684 median      34  p95     340  max    1397
  http:api.rugcheck.xyz      n=   159 median     367  p95     895  max    2075
  http:lite-api.jup.ag/quote n=    24 median      36  p95     104  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=1184: median |div| 1.16%, max |div| 50.82%, |div|>2.6% costs: 304, fast BELOW slow by >2.6%: 200
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=81: median |div| 2.12%, max |div| 11.58%, |div|>2.6% costs: 32, fast BELOW slow by >2.6%: 26
```
