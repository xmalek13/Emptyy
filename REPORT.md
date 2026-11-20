# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2406 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-19T22:43:47-05:00 (137.6s) | last risk tick 2026-11-19T22:45:18-05:00 (39 ms) | risk ticks 5065
Scan loops 105 | last scan: discovered 456 tokens, 455 pairs, 23 in Scout range
Evaluations 475 | unique tokens evaluated 34 | RugCheck ok/fail 114/0 | API errors 1603
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 2, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 7, 'ds-search': 6, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 12, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                       7/56              3/60
Evaluations killed                         412               412
Closed trades                                3                 3
Win rate                                  0.0%              0.0%
Avg win %                                  n/a               n/a
Avg loss %                               -9.40            -24.11
Realized P&L $                          -22.38            -17.97
Equity $ (MTM)                          977.62            982.03
Total P&L $                             -22.38            -17.97
Cash $                                  977.62            982.03
Open positions                               0                 0
Daily-loss halt                              -                 -

Kills by PRIMARY reason:
  bundled>10%(proxy:insider_networks)                 24      24
  liquidity<40k                                      284     284
  mint_authority_not_revoked                          21      21
  pumped>80%_1h                                       25      25
  top10>25%                                            6       6
  vol1h<50k                                           52      52

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                 45      45
  freeze_authority_not_revoked                        21      21
  honeypot/token2022_transfer_restriction              0      21
  liquidity<40k                                      284     284
  lp_not_burned_or_locked                             21      21
  mint_authority_not_revoked                          21      21
  pumped>80%_1h                                       31      31
  top10>25%                                           27      27
  unknown:price_change_1h                            288     288
  vol1h<50k                                          332     332
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=63, median 52.6, max 85.0): {'40-44': 3, '45-49': 12, '50-54': 26, '55-59': 6, '60-64': 4, '65-69': 5, '70-74': 4, '75-79': 1, '80-84': 1, '85-89': 1}

[original] entry blocks: {'cooldown_4h_after_loss': 4}
  CLOSED OGTA         -7.51%  $-6.01  stop  18:34:23 -> 18:35:24
  CLOSED AI           -9.62%  $-7.65  stop  18:58:26 -> 18:59:06
  CLOSED LOOSY       -11.06%  $-8.73  stop  21:58:13 -> 22:00:54
  stop exits: fill vs stop level median -1.56%, worst -3.17% (n=3)
  buys: 3 (3 filled at Jupiter quote), fill vs fast mid median +2.33%, round-trip executable cost median 2.91%

[adjusted] entry blocks: -
  CLOSED AI          -30.26%  $-7.56  stop  18:58:29 -> 19:02:42
  CLOSED OGTA        -21.49%  $-5.33  stop  19:58:11 -> 20:01:36
  CLOSED LOOSY       -20.57%  $-5.08  stop  21:58:16 -> 22:18:00
  stop exits: fill vs stop level median -2.99%, worst -6.10% (n=3)
  buys: 3 (3 filled at Jupiter quote), fill vs fast mid median +1.68%, round-trip executable cost median 2.67%

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n=  4084 median      33  p95     117  max    1135
  http:lite-api.jup.ag/price n=  5172 median      41  p95     126  max    2199
  http:api.geckoterminal.com n=  1250 median      35  p95     347  max     913
  http:api.rugcheck.xyz      n=   114 median     368  p95    1052  max    2075
  http:lite-api.jup.ag/quote n=    18 median      40  p95     160  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=864: median |div| 1.19%, max |div| 50.82%, |div|>2.6% costs: 239, fast BELOW slow by >2.6%: 149
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=54: median |div| 1.69%, max |div| 7.26%, |div|>2.6% costs: 17, fast BELOW slow by >2.6%: 13
```
