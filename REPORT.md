# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 3039 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-20T07:14:30-05:00 (144.2s) | last risk tick 2026-11-20T07:15:07-05:00 (47 ms) | risk ticks 15210
Scan loops 316 | last scan: discovered 443 tokens, 409 pairs, 8 in Scout range
Evaluations 1471 | unique tokens evaluated 48 | RugCheck ok/fail 355/0 | API errors 4841
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 5, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 10, 'ds-search': 8, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 18, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                     53/165            19/199
Evaluations killed                        1253              1253
Closed trades                                9                 8
Win rate                                 22.2%             25.0%
Avg win %                                +3.46             +9.55
Avg loss %                               -9.00            -20.07
Realized P&L $                          -44.04            -25.10
Equity $ (MTM)                          958.74            975.81
Total P&L $                             -41.26            -24.19
Cash $                                  879.48            950.51
Open positions                               1                 1
Daily-loss halt                              -                 -

Kills by PRIMARY reason:
  bundled>10%(proxy:insider_networks)                 69      69
  liquidity<40k                                      899     899
  mint_authority_not_revoked                          61      61
  pumped>80%_1h                                       34      34
  top10>25%                                            8       8
  vol1h<50k                                          182     182

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                130     130
  freeze_authority_not_revoked                        61      61
  honeypot/token2022_transfer_restriction              0      61
  liquidity<40k                                      899     899
  lp_not_burned_or_locked                             61      61
  mint_authority_not_revoked                          61      61
  pumped>80%_1h                                       42      42
  top10>25%                                           69      69
  unknown:price_change_1h                            876     876
  vol1h<50k                                         1075    1075
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=218, median 57.6, max 85.0): {'40-44': 10, '45-49': 27, '50-54': 52, '55-59': 34, '60-64': 21, '65-69': 21, '70-74': 34, '75-79': 16, '80-84': 2, '85-89': 1}

[original] entry blocks: {'cooldown_4h_after_loss': 32, 'already_open': 7, 'max_2_entries_per_token_day': 4}
  OPEN LOOSY      entry 0.00167833 last 0.00178277 (+6.2%) stop 0.00157763 trail off cost $76.48 since 2026-11-20T06:41:47-05:00
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
  buys: 10 (10 filled at Jupiter quote), fill vs fast mid median +1.18%, round-trip executable cost median 2.84%

[adjusted] entry blocks: {'cooldown_4h_after_loss': 9, 'already_open': 1}
  OPEN LOOSY      entry 0.001705 last 0.00178277 (+4.6%) stop 0.0013981 trail off cost $24.39 since 2026-11-20T06:41:50-05:00
  CLOSED AI          -30.26%  $-7.56  stop  18:58:29 -> 19:02:42
  CLOSED OGTA        -21.49%  $-5.33  stop  19:58:11 -> 20:01:36
  CLOSED LOOSY       -20.57%  $-5.08  stop  21:58:16 -> 22:18:00
  CLOSED iAgent      -22.75%  $-5.59  stop  23:48:37 -> 00:00:09
  CLOSED OGTA        -21.08%  $-5.14  stop  02:15:36 -> 02:24:47
  CLOSED iAgent       +2.90%  $+0.70  trailing_stop  05:51:37 -> 06:10:25
  CLOSED LOOSY       +16.20%  $+3.94  trailing_stop  05:56:47 -> 06:30:10
  CLOSED OGTA         -4.28%  $-1.04  trailing_stop  06:39:13 -> 06:48:28
  stop exits: fill vs stop level median -5.37%, worst -9.06% (n=8)
  buys: 9 (9 filled at Jupiter quote), fill vs fast mid median +1.32%, round-trip executable cost median 2.67%

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n= 12521 median      38  p95     113  max    1135
  http:lite-api.jup.ag/price n= 15527 median      43  p95     126  max    2737
  http:api.geckoterminal.com n=  3698 median      39  p95     340  max    1397
  http:api.rugcheck.xyz      n=   355 median     377  p95     609  max    2075
  http:lite-api.jup.ag/quote n=    56 median      37  p95     128  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=2627: median |div| 1.04%, max |div| 50.82%, |div|>2.6% costs: 589, fast BELOW slow by >2.6%: 404
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=455: median |div| 1.33%, max |div| 11.58%, |div|>2.6% costs: 109, fast BELOW slow by >2.6%: 66
```
