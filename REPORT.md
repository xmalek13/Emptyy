# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2252 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-20T02:22:48-05:00 (141.6s) | last risk tick 2026-11-20T02:23:59-05:00 (105 ms) | risk ticks 9416
Scan loops 196 | last scan: discovered 442 tokens, 442 pairs, 21 in Scout range
Evaluations 926 | unique tokens evaluated 40 | RugCheck ok/fail 219/0 | API errors 2980
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 4, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 8, 'ds-search': 8, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 13, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                     27/105             6/126
Evaluations killed                         794               794
Closed trades                                6                 4
Win rate                                 16.7%              0.0%
Avg win %                                +3.89               n/a
Avg loss %                               -8.89            -23.77
Realized P&L $                          -32.04            -23.56
Equity $ (MTM)                          965.41            972.39
Total P&L $                             -34.59            -27.61
Cash $                                  890.53            952.03
Open positions                               1                 1
Daily-loss halt                              -                 -

Kills by PRIMARY reason:
  bundled>10%(proxy:insider_networks)                 43      43
  liquidity<40k                                      578     578
  mint_authority_not_revoked                          36      36
  pumped>80%_1h                                       29      29
  top10>25%                                            8       8
  vol1h<50k                                          100     100

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                 79      79
  freeze_authority_not_revoked                        36      36
  honeypot/token2022_transfer_restriction              0      36
  liquidity<40k                                      578     578
  lp_not_burned_or_locked                             36      36
  mint_authority_not_revoked                          36      36
  pumped>80%_1h                                       36      36
  top10>25%                                           44      44
  unknown:price_change_1h                            560     560
  vol1h<50k                                          673     673
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=132, median 55.0, max 85.0): {'40-44': 5, '45-49': 17, '50-54': 42, '55-59': 20, '60-64': 10, '65-69': 11, '70-74': 21, '75-79': 4, '80-84': 1, '85-89': 1}

[original] entry blocks: {'cooldown_4h_after_loss': 17, 'already_open': 3}
  OPEN LOOSY      entry 0.00115441 last 0.00114406 (-0.9%) stop 0.00108515 trail off cost $77.44 since 2026-11-20T02:03:37-05:00
  CLOSED OGTA         -7.51%  $-6.01  stop  18:34:23 -> 18:35:24
  CLOSED AI           -9.62%  $-7.65  stop  18:58:26 -> 18:59:06
  CLOSED LOOSY       -11.06%  $-8.73  stop  21:58:13 -> 22:00:54
  CLOSED iAgent       -8.28%  $-6.47  stop  23:12:35 -> 23:15:00
  CLOSED OGTA         +3.89%  $+3.02  trailing_stop  01:15:35 -> 01:33:14
  CLOSED OGTA         -7.96%  $-6.20  stop  01:39:36 -> 01:59:11
  stop exits: fill vs stop level median -1.40%, worst -3.17% (n=6)
  buys: 7 (7 filled at Jupiter quote), fill vs fast mid median +1.21%, round-trip executable cost median 2.94%

[adjusted] entry blocks: {'cooldown_4h_after_loss': 1}
  OPEN OGTA       entry 0.000637588 last 0.000552765 (-13.3%) stop 0.000522822 trail off cost $24.41 since 2026-11-20T02:15:36-05:00
  CLOSED AI          -30.26%  $-7.56  stop  18:58:29 -> 19:02:42
  CLOSED OGTA        -21.49%  $-5.33  stop  19:58:11 -> 20:01:36
  CLOSED LOOSY       -20.57%  $-5.08  stop  21:58:16 -> 22:18:00
  CLOSED iAgent      -22.75%  $-5.59  stop  23:48:37 -> 00:00:09
  stop exits: fill vs stop level median -3.88%, worst -6.10% (n=4)
  buys: 5 (5 filled at Jupiter quote), fill vs fast mid median +1.68%, round-trip executable cost median 2.67%

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n=  7713 median      37  p95     114  max    1135
  http:lite-api.jup.ag/price n=  9617 median      44  p95     127  max    2737
  http:api.geckoterminal.com n=  2326 median      38  p95     341  max    1397
  http:api.rugcheck.xyz      n=   219 median     372  p95     691  max    2075
  http:lite-api.jup.ag/quote n=    34 median      40  p95     110  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=1645: median |div| 1.10%, max |div| 50.82%, |div|>2.6% costs: 393, fast BELOW slow by >2.6%: 265
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=205: median |div| 1.78%, max |div| 11.58%, |div|>2.6% costs: 63, fast BELOW slow by >2.6%: 44
```
