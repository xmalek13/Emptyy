# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2406 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-19T19:22:26-05:00 (146.7s) | last risk tick 2026-11-19T19:24:35-05:00 (36 ms) | risk ticks 1051
Scan loops 21 | last scan: discovered 431 tokens, 431 pairs, 10 in Scout range
Evaluations 82 | unique tokens evaluated 23 | RugCheck ok/fail 26/0 | API errors 332
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 2, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 1, 'ds-search': 3, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 11, 'gt:dexes/meteora-damm-v2/pools': 2}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                       2/14              1/15
Evaluations killed                          66                66
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
  bundled>10%(proxy:insider_networks)                  5       5
  liquidity<40k                                       45      45
  mint_authority_not_revoked                           5       5
  pumped>80%_1h                                        2       2
  vol1h<50k                                            9       9

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                 10      10
  freeze_authority_not_revoked                         5       5
  honeypot/token2022_transfer_restriction              0       5
  liquidity<40k                                       45      45
  lp_not_burned_or_locked                              5       5
  mint_authority_not_revoked                           5       5
  pumped>80%_1h                                        2       2
  top10>25%                                            5       5
  unknown:price_change_1h                             47      47
  vol1h<50k                                           53      53
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=16, median 52.5, max 85.0): {'40-44': 2, '45-49': 5, '50-54': 3, '55-59': 2, '60-64': 1, '65-69': 1, '70-74': 1, '85-89': 1}

[original] entry blocks: -
  CLOSED OGTA         -7.51%  $-6.01  stop  18:34:23 -> 18:35:24
  CLOSED AI           -9.62%  $-7.65  stop  18:58:26 -> 18:59:06
  stop exits: fill vs stop level median -1.11%, worst -1.56% (n=2)
  buys: 2 (2 filled at Jupiter quote), fill vs fast mid median +1.67%, round-trip executable cost median 2.70%

[adjusted] entry blocks: -
  CLOSED AI          -30.26%  $-7.56  stop  18:58:29 -> 19:02:42
  stop exits: fill vs stop level median -6.10%, worst -6.10% (n=1)
  buys: 1 (1 filled at Jupiter quote), fill vs fast mid median +10.40%, round-trip executable cost median 2.45%

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n=   826 median      32  p95     108  max     830
  http:lite-api.jup.ag/price n=  1074 median      36  p95     125  max    1765
  http:api.geckoterminal.com n=   261 median      33  p95     313  max     590
  http:api.rugcheck.xyz      n=    26 median     373  p95     391  max     399
  http:lite-api.jup.ag/quote n=     9 median      58  p95     160  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=131: median |div| 1.45%, max |div| 27.93%, |div|>2.6% costs: 36, fast BELOW slow by >2.6%: 26
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=11: median |div| 2.68%, max |div| 7.06%, |div|>2.6% costs: 6, fast BELOW slow by >2.6%: 5
```
