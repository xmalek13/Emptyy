# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 3039 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-20T06:04:10-05:00 (141.5s) | last risk tick 2026-11-20T06:04:49-05:00 (128 ms) | risk ticks 13804
Scan loops 288 | last scan: discovered 428 tokens, 426 pairs, 20 in Scout range
Evaluations 1336 | unique tokens evaluated 44 | RugCheck ok/fail 315/0 | API errors 4371
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 5, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 10, 'ds-search': 8, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 14, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                     47/144            15/176
Evaluations killed                        1145              1145
Closed trades                                9                 5
Win rate                                 22.2%              0.0%
Avg win %                                +3.46               n/a
Avg loss %                               -9.00            -23.23
Realized P&L $                          -44.04            -28.70
Equity $ (MTM)                          955.96            973.05
Total P&L $                             -44.04            -26.95
Cash $                                  955.96            922.69
Open positions                               0                 2
Daily-loss halt                              -                 -

Kills by PRIMARY reason:
  bundled>10%(proxy:insider_networks)                 62      62
  liquidity<40k                                      827     827
  mint_authority_not_revoked                          54      54
  pumped>80%_1h                                       32      32
  top10>25%                                            8       8
  vol1h<50k                                          162     162

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                116     116
  freeze_authority_not_revoked                        54      54
  honeypot/token2022_transfer_restriction              0      54
  liquidity<40k                                      827     827
  lp_not_burned_or_locked                             54      54
  mint_authority_not_revoked                          54      54
  pumped>80%_1h                                       40      40
  top10>25%                                           62      62
  unknown:price_change_1h                            805     805
  vol1h<50k                                          983     983
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=191, median 58.1, max 85.0): {'40-44': 7, '45-49': 25, '50-54': 47, '55-59': 25, '60-64': 20, '65-69': 20, '70-74': 32, '75-79': 13, '80-84': 1, '85-89': 1}

[original] entry blocks: {'cooldown_4h_after_loss': 32, 'already_open': 5, 'max_2_entries_per_token_day': 1}
  CLOSED OGTA         -7.51%  $-6.01  stop  18:34:23 -> 18:35:24
  CLOSED AI           -9.62%  $-7.65  stop  18:58:26 -> 18:59:06
  CLOSED LOOSY       -11.06%  $-8.73  stop  21:58:13 -> 22:00:54
  CLOSED iAgent       -8.28%  $-6.47  stop  23:12:35 -> 23:15:00
  CLOSED OGTA         +3.89%  $+3.02  trailing_stop  01:15:35 -> 01:33:14
  CLOSED OGTA         -7.96%  $-6.20  stop  01:39:36 -> 01:59:11
  CLOSED LOOSY        -8.33%  $-6.45  stop  02:03:37 -> 02:35:20
  CLOSED iAgent       +3.04%  $+2.34  trailing_stop  03:15:33 -> 03:40:17
  CLOSED iAgent      -10.24%  $-7.89  stop  03:51:36 -> 03:52:29
  stop exits: fill vs stop level median -1.56%, worst -3.60% (n=9)
  buys: 9 (9 filled at Jupiter quote), fill vs fast mid median +1.21%, round-trip executable cost median 2.91%

[adjusted] entry blocks: {'cooldown_4h_after_loss': 7, 'already_open': 1}
  OPEN iAgent     entry 0.000850756 last 0.00098616 (+15.9%) stop 0.000887993 trail on cost $24.28 since 2026-11-20T05:51:37-05:00
  OPEN LOOSY      entry 0.00136882 last 0.00133259 (-2.6%) stop 0.00112243 trail off cost $24.32 since 2026-11-20T05:56:47-05:00
  CLOSED AI          -30.26%  $-7.56  stop  18:58:29 -> 19:02:42
  CLOSED OGTA        -21.49%  $-5.33  stop  19:58:11 -> 20:01:36
  CLOSED LOOSY       -20.57%  $-5.08  stop  21:58:16 -> 22:18:00
  CLOSED iAgent      -22.75%  $-5.59  stop  23:48:37 -> 00:00:09
  CLOSED OGTA        -21.08%  $-5.14  stop  02:15:36 -> 02:24:47
  stop exits: fill vs stop level median -2.99%, worst -6.10% (n=5)
  buys: 7 (7 filled at Jupiter quote), fill vs fast mid median +1.68%, round-trip executable cost median 2.67%

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n= 11341 median      39  p95     114  max    1135
  http:lite-api.jup.ag/price n= 14095 median      45  p95     128  max    2737
  http:api.geckoterminal.com n=  3411 median      40  p95     340  max    1397
  http:api.rugcheck.xyz      n=   315 median     378  p95     609  max    2075
  http:lite-api.jup.ag/quote n=    46 median      41  p95     128  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=2395: median |div| 1.04%, max |div| 50.82%, |div|>2.6% costs: 533, fast BELOW slow by >2.6%: 365
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=312: median |div| 1.38%, max |div| 11.58%, |div|>2.6% costs: 75, fast BELOW slow by >2.6%: 49
```
