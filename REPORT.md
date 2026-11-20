# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2252 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-20T05:22:49-05:00 (141.9s) | last risk tick 2026-11-20T05:24:45-05:00 (160 ms) | risk ticks 13028
Scan loops 271 | last scan: discovered 436 tokens, 436 pairs, 19 in Scout range
Evaluations 1252 | unique tokens evaluated 43 | RugCheck ok/fail 290/0 | API errors 4121
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 5, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 9, 'ds-search': 8, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 14, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                     40/134            10/164
Evaluations killed                        1078              1078
Closed trades                                9                 5
Win rate                                 22.2%              0.0%
Avg win %                                +3.46               n/a
Avg loss %                               -9.00            -23.23
Realized P&L $                          -44.04            -28.70
Equity $ (MTM)                          955.96            971.30
Total P&L $                             -44.04            -28.70
Cash $                                  955.96            971.30
Open positions                               0                 0
Daily-loss halt                              -                 -

Kills by PRIMARY reason:
  bundled>10%(proxy:insider_networks)                 58      58
  liquidity<40k                                      778     778
  mint_authority_not_revoked                          50      50
  pumped>80%_1h                                       30      30
  top10>25%                                            8       8
  vol1h<50k                                          154     154

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                108     108
  freeze_authority_not_revoked                        50      50
  honeypot/token2022_transfer_restriction              0      50
  liquidity<40k                                      778     778
  lp_not_burned_or_locked                             50      50
  mint_authority_not_revoked                          50      50
  pumped>80%_1h                                       38      38
  top10>25%                                           58      58
  unknown:price_change_1h                            754     754
  vol1h<50k                                          926     926
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=174, median 56.6, max 85.0): {'40-44': 7, '45-49': 22, '50-54': 46, '55-59': 23, '60-64': 16, '65-69': 20, '70-74': 30, '75-79': 8, '80-84': 1, '85-89': 1}

[original] entry blocks: {'cooldown_4h_after_loss': 26, 'already_open': 5}
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

[adjusted] entry blocks: {'cooldown_4h_after_loss': 5}
  CLOSED AI          -30.26%  $-7.56  stop  18:58:29 -> 19:02:42
  CLOSED OGTA        -21.49%  $-5.33  stop  19:58:11 -> 20:01:36
  CLOSED LOOSY       -20.57%  $-5.08  stop  21:58:16 -> 22:18:00
  CLOSED iAgent      -22.75%  $-5.59  stop  23:48:37 -> 00:00:09
  CLOSED OGTA        -21.08%  $-5.14  stop  02:15:36 -> 02:24:47
  stop exits: fill vs stop level median -2.99%, worst -6.10% (n=5)
  buys: 5 (5 filled at Jupiter quote), fill vs fast mid median +1.68%, round-trip executable cost median 2.67%

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n= 10670 median      38  p95     114  max    1135
  http:lite-api.jup.ag/price n= 13303 median      46  p95     128  max    2737
  http:api.geckoterminal.com n=  3219 median      39  p95     340  max    1397
  http:api.rugcheck.xyz      n=   290 median     377  p95     556  max    2075
  http:lite-api.jup.ag/quote n=    42 median      42  p95     128  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=2259: median |div| 1.05%, max |div| 50.82%, |div|>2.6% costs: 508, fast BELOW slow by >2.6%: 350
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=277: median |div| 1.40%, max |div| 11.58%, |div|>2.6% costs: 68, fast BELOW slow by >2.6%: 47
```
