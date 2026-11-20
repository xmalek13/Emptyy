# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2406 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-19T20:03:01-05:00 (141.3s) | last risk tick 2026-11-19T20:04:45-05:00 (33 ms) | risk ticks 1854
Scan loops 38 | last scan: discovered 435 tokens, 435 pairs, 20 in Scout range
Evaluations 157 | unique tokens evaluated 27 | RugCheck ok/fail 41/0 | API errors 587
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 2, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 2, 'ds-search': 4, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 12, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                       5/20              2/23
Evaluations killed                         132               132
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
  bundled>10%(proxy:insider_networks)                  8       8
  liquidity<40k                                       96      96
  mint_authority_not_revoked                           8       8
  pumped>80%_1h                                        3       3
  vol1h<50k                                           17      17

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                 16      16
  freeze_authority_not_revoked                         8       8
  honeypot/token2022_transfer_restriction              0       8
  liquidity<40k                                       96      96
  lp_not_burned_or_locked                              8       8
  mint_authority_not_revoked                           8       8
  pumped>80%_1h                                        4       4
  top10>25%                                            8       8
  unknown:price_change_1h                            101     101
  vol1h<50k                                          112     112
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=25, median 51.1, max 85.0): {'40-44': 3, '45-49': 8, '50-54': 5, '55-59': 2, '60-64': 1, '65-69': 1, '70-74': 3, '75-79': 1, '85-89': 1}

[original] entry blocks: {'cooldown_4h_after_loss': 3}
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
  http:api.dexscreener.com   n=  1487 median      33  p95     113  max     830
  http:lite-api.jup.ag/price n=  1894 median      37  p95     125  max    1765
  http:api.geckoterminal.com n=   459 median      34  p95     332  max     759
  http:api.rugcheck.xyz      n=    41 median     378  p95     575  max     895
  http:lite-api.jup.ag/quote n=    12 median      52  p95     160  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=238: median |div| 1.30%, max |div| 27.93%, |div|>2.6% costs: 69, fast BELOW slow by >2.6%: 47
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=17: median |div| 2.68%, max |div| 7.06%, |div|>2.6% costs: 9, fast BELOW slow by >2.6%: 7
```
