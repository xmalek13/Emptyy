# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2406 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-19T21:53:25-05:00 (141.6s) | last risk tick 2026-11-19T21:55:06-05:00 (104 ms) | risk ticks 4061
Scan loops 84 | last scan: discovered 424 tokens, 422 pairs, 23 in Scout range
Evaluations 380 | unique tokens evaluated 34 | RugCheck ok/fail 81/0 | API errors 1285
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 2, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 7, 'ds-search': 6, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 12, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                       6/41              2/45
Evaluations killed                         333               333
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
  bundled>10%(proxy:insider_networks)                 15      15
  liquidity<40k                                      232     232
  mint_authority_not_revoked                          17      17
  pumped>80%_1h                                       25      25
  top10>25%                                            2       2
  vol1h<50k                                           42      42

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                 32      32
  freeze_authority_not_revoked                        17      17
  honeypot/token2022_transfer_restriction              0      17
  liquidity<40k                                      232     232
  lp_not_burned_or_locked                             17      17
  mint_authority_not_revoked                          17      17
  pumped>80%_1h                                       31      31
  top10>25%                                           19      19
  unknown:price_change_1h                            234     234
  vol1h<50k                                          270     270
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=47, median 52.8, max 85.0): {'40-44': 3, '45-49': 9, '50-54': 18, '55-59': 4, '60-64': 3, '65-69': 4, '70-74': 4, '75-79': 1, '85-89': 1}

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
  http:api.dexscreener.com   n=  3240 median      33  p95     117  max    1135
  http:lite-api.jup.ag/price n=  4148 median      42  p95     126  max    2199
  http:api.geckoterminal.com n=  1003 median      35  p95     345  max     913
  http:api.rugcheck.xyz      n=    81 median     369  p95     880  max    2075
  http:lite-api.jup.ag/quote n=    12 median      52  p95     160  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=673: median |div| 1.22%, max |div| 50.82%, |div|>2.6% costs: 196, fast BELOW slow by >2.6%: 120
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=17: median |div| 2.68%, max |div| 7.06%, |div|>2.6% costs: 9, fast BELOW slow by >2.6%: 7
```
