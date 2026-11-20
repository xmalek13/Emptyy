# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2252 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-20T01:51:39-05:00 (142.0s) | last risk tick 2026-11-20T01:53:53-05:00 (114 ms) | risk ticks 8814
Scan loops 183 | last scan: discovered 466 tokens, 464 pairs, 22 in Scout range
Evaluations 861 | unique tokens evaluated 38 | RugCheck ok/fail 204/0 | API errors 2791
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 4, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 7, 'ds-search': 7, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 13, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                      23/98             5/116
Evaluations killed                         740               740
Closed trades                                5                 4
Win rate                                 20.0%              0.0%
Avg win %                                +3.89               n/a
Avg loss %                               -9.12            -23.77
Realized P&L $                          -25.83            -23.56
Equity $ (MTM)                          973.57            976.44
Total P&L $                             -26.43            -23.56
Cash $                                  896.23            976.44
Open positions                               1                 0
Daily-loss halt                              -                 -

Kills by PRIMARY reason:
  bundled>10%(proxy:insider_networks)                 41      41
  liquidity<40k                                      534     534
  mint_authority_not_revoked                          34      34
  pumped>80%_1h                                       27      27
  top10>25%                                            8       8
  vol1h<50k                                           96      96

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                 75      75
  freeze_authority_not_revoked                        34      34
  honeypot/token2022_transfer_restriction              0      34
  liquidity<40k                                      534     534
  lp_not_burned_or_locked                             34      34
  mint_authority_not_revoked                          34      34
  pumped>80%_1h                                       34      34
  top10>25%                                           42      42
  unknown:price_change_1h                            517     517
  vol1h<50k                                          625     625
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=121, median 54.9, max 85.0): {'40-44': 5, '45-49': 16, '50-54': 40, '55-59': 18, '60-64': 9, '65-69': 10, '70-74': 18, '75-79': 3, '80-84': 1, '85-89': 1}

[original] entry blocks: {'cooldown_4h_after_loss': 15, 'already_open': 2}
  OPEN OGTA       entry 0.000583177 last 0.000593436 (+1.8%) stop 0.000548187 trail off cost $77.93 since 2026-11-20T01:39:36-05:00
  CLOSED OGTA         -7.51%  $-6.01  stop  18:34:23 -> 18:35:24
  CLOSED AI           -9.62%  $-7.65  stop  18:58:26 -> 18:59:06
  CLOSED LOOSY       -11.06%  $-8.73  stop  21:58:13 -> 22:00:54
  CLOSED iAgent       -8.28%  $-6.47  stop  23:12:35 -> 23:15:00
  CLOSED OGTA         +3.89%  $+3.02  trailing_stop  01:15:35 -> 01:33:14
  stop exits: fill vs stop level median -1.56%, worst -3.17% (n=5)
  buys: 6 (6 filled at Jupiter quote), fill vs fast mid median +1.22%, round-trip executable cost median 3.00%

[adjusted] entry blocks: {'cooldown_4h_after_loss': 1}
  CLOSED AI          -30.26%  $-7.56  stop  18:58:29 -> 19:02:42
  CLOSED OGTA        -21.49%  $-5.33  stop  19:58:11 -> 20:01:36
  CLOSED LOOSY       -20.57%  $-5.08  stop  21:58:16 -> 22:18:00
  CLOSED iAgent      -22.75%  $-5.59  stop  23:48:37 -> 00:00:09
  stop exits: fill vs stop level median -3.88%, worst -6.10% (n=4)
  buys: 4 (4 filled at Jupiter quote), fill vs fast mid median +1.50%, round-trip executable cost median 2.56%

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n=  7169 median      37  p95     114  max    1135
  http:lite-api.jup.ag/price n=  9002 median      43  p95     126  max    2737
  http:api.geckoterminal.com n=  2176 median      37  p95     340  max    1397
  http:api.rugcheck.xyz      n=   204 median     370  p95     691  max    2075
  http:lite-api.jup.ag/quote n=    29 median      37  p95     104  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=1528: median |div| 1.12%, max |div| 50.82%, |div|>2.6% costs: 367, fast BELOW slow by >2.6%: 245
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=141: median |div| 1.97%, max |div| 11.58%, |div|>2.6% costs: 50, fast BELOW slow by >2.6%: 34
```
