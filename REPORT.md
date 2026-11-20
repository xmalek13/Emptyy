# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2406 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-19T21:02:59-05:00 (137.5s) | last risk tick 2026-11-19T21:04:57-05:00 (55 ms) | risk ticks 3058
Scan loops 63 | last scan: discovered 454 tokens, 454 pairs, 27 in Scout range
Evaluations 266 | unique tokens evaluated 34 | RugCheck ok/fail 59/0 | API errors 969
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 2, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 7, 'ds-search': 6, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 12, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                       6/29              2/33
Evaluations killed                         231               231
Closed trades                                2                 2
Win rate                                  0.0%              0.0%
Avg win %                                  n/a               n/a
Avg loss %                               -8.56            -25.88
Realized P&L $                          -13.66            -12.90
Equity $ (MTM)                          986.34            987.10
Total P&L $                             -13.66            -12.90
Cash $                                  986.34            987.10
Open positions                               0                 0
Daily-loss halt                              -                 -

Kills by PRIMARY reason:
  bundled>10%(proxy:insider_networks)                 11      11
  liquidity<40k                                      161     161
  mint_authority_not_revoked                          13      13
  pumped>80%_1h                                       12      12
  vol1h<50k                                           34      34

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                 24      24
  freeze_authority_not_revoked                        13      13
  honeypot/token2022_transfer_restriction              0      13
  liquidity<40k                                      161     161
  lp_not_burned_or_locked                             13      13
  mint_authority_not_revoked                          13      13
  pumped>80%_1h                                       18      18
  top10>25%                                           13      13
  unknown:price_change_1h                            163     163
  vol1h<50k                                          191     191
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=35, median 53.4, max 85.0): {'40-44': 3, '45-49': 9, '50-54': 9, '55-59': 2, '60-64': 3, '65-69': 3, '70-74': 4, '75-79': 1, '85-89': 1}

[original] entry blocks: {'cooldown_4h_after_loss': 4}
  CLOSED OGTA         -7.51%  $-6.01  stop  18:34:23 -> 18:35:24
  CLOSED AI           -9.62%  $-7.65  stop  18:58:26 -> 18:59:06
  stop exits: fill vs stop level median -1.11%, worst -1.56% (n=2)
  buys: 2 (2 filled at Jupiter quote), fill vs fast mid median +1.67%, round-trip executable cost median 2.70%

[adjusted] entry blocks: -
  CLOSED AI          -30.26%  $-7.56  stop  18:58:29 -> 19:02:42
  CLOSED OGTA        -21.49%  $-5.33  stop  19:58:11 -> 20:01:36
  stop exits: fill vs stop level median -4.54%, worst -6.10% (n=2)
  buys: 2 (2 filled at Jupiter quote), fill vs fast mid median +5.86%, round-trip executable cost median 2.56%

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n=  2442 median      33  p95     114  max    1014
  http:lite-api.jup.ag/price n=  3123 median      40  p95     126  max    2199
  http:api.geckoterminal.com n=   755 median      34  p95     341  max     913
  http:api.rugcheck.xyz      n=    59 median     372  p95    1193  max    2075
  http:lite-api.jup.ag/quote n=    12 median      52  p95     160  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=451: median |div| 1.25%, max |div| 50.82%, |div|>2.6% costs: 129, fast BELOW slow by >2.6%: 84
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=17: median |div| 2.68%, max |div| 7.06%, |div|>2.6% costs: 9, fast BELOW slow by >2.6%: 7
```
