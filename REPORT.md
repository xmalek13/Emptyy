# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2406 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-19T19:53:23-05:00 (137.2s) | last risk tick 2026-11-19T19:54:42-05:00 (34 ms) | risk ticks 1653
Scan loops 34 | last scan: discovered 430 tokens, 429 pairs, 20 in Scout range
Evaluations 136 | unique tokens evaluated 25 | RugCheck ok/fail 36/0 | API errors 522
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 2, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 2, 'ds-search': 4, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 11, 'gt:dexes/meteora-damm-v2/pools': 2}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                       4/18              1/21
Evaluations killed                         114               114
Closed trades                                2                 1
Win rate                                  0.0%              0.0%
Avg win %                                  n/a               n/a
Avg loss %                               -8.56            -30.26
Realized P&L $                          -13.66             -7.56
Equity $ (MTM)                          986.34            992.44
Total P&L $                             -13.66             -7.56
Cash $                                  986.34            992.44
Open positions                               0                 0
Daily-loss halt                              -                 -

Kills by PRIMARY reason:
  bundled>10%(proxy:insider_networks)                  7       7
  liquidity<40k                                       83      83
  mint_authority_not_revoked                           7       7
  pumped>80%_1h                                        3       3
  vol1h<50k                                           14      14

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                 14      14
  freeze_authority_not_revoked                         7       7
  honeypot/token2022_transfer_restriction              0       7
  liquidity<40k                                       83      83
  lp_not_burned_or_locked                              7       7
  mint_authority_not_revoked                           7       7
  pumped>80%_1h                                        3       3
  top10>25%                                            7       7
  unknown:price_change_1h                             87      87
  vol1h<50k                                           96      96
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=22, median 51.1, max 85.0): {'40-44': 3, '45-49': 7, '50-54': 4, '55-59': 2, '60-64': 1, '65-69': 1, '70-74': 3, '85-89': 1}

[original] entry blocks: {'cooldown_4h_after_loss': 2}
  CLOSED OGTA         -7.51%  $-6.01  stop  18:34:23 -> 18:35:24
  CLOSED AI           -9.62%  $-7.65  stop  18:58:26 -> 18:59:06
  stop exits: fill vs stop level median -1.11%, worst -1.56% (n=2)
  buys: 2 (2 filled at Jupiter quote), fill vs fast mid median +1.67%, round-trip executable cost median 2.70%

[adjusted] entry blocks: -
  CLOSED AI          -30.26%  $-7.56  stop  18:58:29 -> 19:02:42
  stop exits: fill vs stop level median -6.10%, worst -6.10% (n=1)
  buys: 1 (1 filled at Jupiter quote), fill vs fast mid median +10.40%, round-trip executable cost median 2.45%

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n=  1327 median      32  p95     111  max     830
  http:lite-api.jup.ag/price n=  1689 median      37  p95     123  max    1765
  http:api.geckoterminal.com n=   411 median      34  p95     321  max     759
  http:api.rugcheck.xyz      n=    36 median     376  p95     575  max     895
  http:lite-api.jup.ag/quote n=     9 median      58  p95     160  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=212: median |div| 1.33%, max |div| 27.93%, |div|>2.6% costs: 63, fast BELOW slow by >2.6%: 43
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=11: median |div| 2.68%, max |div| 7.06%, |div|>2.6% costs: 6, fast BELOW slow by >2.6%: 5
```
