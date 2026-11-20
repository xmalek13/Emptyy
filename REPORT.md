# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 3039 NOT RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-20T09:00:01-05:00 (137.4s) | last risk tick 2026-11-20T08:59:58-05:00 (22 ms) | risk ticks 17307
Scan loops 359 | last scan: discovered 461 tokens, 458 pairs, 21 in Scout range
Evaluations 1644 | unique tokens evaluated 51 | RugCheck ok/fail 397/0 | API errors 5529
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 5, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 11, 'ds-search': 8, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 20, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                     61/184            22/223
Evaluations killed                        1399              1399
Closed trades                               13                10
Win rate                                 30.8%             30.0%
Avg win %                                +7.96             +8.67
Avg loss %                               -8.52            -18.35
Realized P&L $                          -35.55            -25.38
Equity $ (MTM)                          964.45            974.62
Total P&L $                             -35.55            -25.38
Cash $                                  964.45            974.62
Open positions                               0                 0
Daily-loss halt                              -                 -

Kills by PRIMARY reason:
  bundled>10%(proxy:insider_networks)                 76      76
  liquidity<40k                                     1009    1009
  mint_authority_not_revoked                          69      69
  pumped>80%_1h                                       34      34
  top10>25%                                            8       8
  vol1h<50k                                          203     203

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                145     145
  freeze_authority_not_revoked                        69      69
  honeypot/token2022_transfer_restriction              0      69
  liquidity<40k                                     1009    1009
  lp_not_burned_or_locked                             69      69
  mint_authority_not_revoked                          69      69
  pumped>80%_1h                                       42      42
  top10>25%                                           77      77
  unknown:price_change_1h                            984     984
  vol1h<50k                                         1206    1206
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=245, median 58.0, max 85.0): {'40-44': 10, '45-49': 27, '50-54': 60, '55-59': 38, '60-64': 23, '65-69': 26, '70-74': 39, '75-79': 18, '80-84': 3, '85-89': 1}

[original] entry blocks: {'cooldown_4h_after_loss': 33, 'already_open': 7, 'max_2_entries_per_token_day': 8}
  CLOSED OGTA         -7.51%  $-6.01  stop  18:34:23 -> 18:35:24
  CLOSED AI           -9.62%  $-7.65  stop  18:58:26 -> 18:59:06
  CLOSED LOOSY       -11.06%  $-8.73  stop  21:58:13 -> 22:00:54
  CLOSED iAgent       -8.28%  $-6.47  stop  23:12:35 -> 23:15:00
  CLOSED OGTA         +3.89%  $+3.02  trailing_stop  01:15:35 -> 01:33:14
  CLOSED OGTA         -7.96%  $-6.20  stop  01:39:36 -> 01:59:11
  CLOSED LOOSY        -8.33%  $-6.45  stop  02:03:37 -> 02:35:20
  CLOSED iAgent       +3.04%  $+2.34  trailing_stop  03:15:33 -> 03:40:17
  CLOSED iAgent      -10.24%  $-7.89  stop  03:51:36 -> 03:52:29
  CLOSED LOOSY       +12.05%  $+9.22  trailing_stop  06:41:47 -> 07:20:37
  CLOSED Leonida     +12.84%  $+9.92  trailing_stop  08:35:27 -> 08:42:20
  CLOSED Leonida     -10.14%  $-7.91  stop  08:45:33 -> 08:47:20
  CLOSED SHIT         -3.53%  $-2.73  end_of_run  08:50:27 -> 09:00:06
  stop exits: fill vs stop level median -1.98%, worst -3.60% (n=12)
  buys: 13 (13 filled at Jupiter quote), fill vs fast mid median +1.23%, round-trip executable cost median 2.91%

[adjusted] entry blocks: {'cooldown_4h_after_loss': 11, 'already_open': 1}
  CLOSED AI          -30.26%  $-7.56  stop  18:58:29 -> 19:02:42
  CLOSED OGTA        -21.49%  $-5.33  stop  19:58:11 -> 20:01:36
  CLOSED LOOSY       -20.57%  $-5.08  stop  21:58:16 -> 22:18:00
  CLOSED iAgent      -22.75%  $-5.59  stop  23:48:37 -> 00:00:09
  CLOSED OGTA        -21.08%  $-5.14  stop  02:15:36 -> 02:24:47
  CLOSED iAgent       +2.90%  $+0.70  trailing_stop  05:51:37 -> 06:10:25
  CLOSED LOOSY       +16.20%  $+3.94  trailing_stop  05:56:47 -> 06:30:10
  CLOSED OGTA         -4.28%  $-1.04  trailing_stop  06:39:13 -> 06:48:28
  CLOSED LOOSY        +6.90%  $+1.68  trailing_stop  06:41:50 -> 07:21:25
  CLOSED Leonida      -8.02%  $-1.96  end_of_run  08:57:38 -> 09:00:06
  stop exits: fill vs stop level median -4.76%, worst -9.06% (n=9)
  buys: 10 (10 filled at Jupiter quote), fill vs fast mid median +1.32%, round-trip executable cost median 2.68%

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n= 14216 median      38  p95     114  max    1135
  http:lite-api.jup.ag/price n= 17672 median      39  p95     124  max    2737
  http:api.geckoterminal.com n=  4164 median      39  p95     343  max    1397
  http:api.rugcheck.xyz      n=   397 median     376  p95     609  max    2410
  http:lite-api.jup.ag/quote n=    70 median      34  p95     110  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=2914: median |div| 1.01%, max |div| 50.82%, |div|>2.6% costs: 630, fast BELOW slow by >2.6%: 433
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=509: median |div| 1.33%, max |div| 11.58%, |div|>2.6% costs: 121, fast BELOW slow by >2.6%: 69
```
