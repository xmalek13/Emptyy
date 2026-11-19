# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2406 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-19T18:43:58-05:00 (137.1s) | last risk tick 2026-11-19T18:44:26-05:00 (29 ms) | risk ticks 248
Scan loops 5 | last scan: discovered 443 tokens, 442 pairs, 19 in Scout range
Evaluations 21 | unique tokens evaluated 21 | RugCheck ok/fail 5/0 | API errors 77
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 2, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 1, 'ds-search': 3, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 11}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                        1/2               0/3
Evaluations killed                          18                18
Closed trades                                1                 0
Win rate                                  0.0%               n/a
Avg win %                                  n/a               n/a
Avg loss %                               -7.51               n/a
Realized P&L $                           -6.01             +0.00
Equity $ (MTM)                          993.99           1000.00
Total P&L $                              -6.01             +0.00
Cash $                                  993.99           1000.00
Open positions                               0                 0
Daily-loss halt                              -                 -

Kills by PRIMARY reason:
  bundled>10%(proxy:insider_networks)                  1       1
  liquidity<40k                                       13      13
  mint_authority_not_revoked                           1       1
  pumped>80%_1h                                        1       1
  vol1h<50k                                            2       2

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                  2       2
  freeze_authority_not_revoked                         1       1
  honeypot/token2022_transfer_restriction              0       1
  liquidity<40k                                       13      13
  lp_not_burned_or_locked                              1       1
  mint_authority_not_revoked                           1       1
  pumped>80%_1h                                        1       1
  top10>25%                                            1       1
  unknown:price_change_1h                             13      13
  vol1h<50k                                           15      15
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=3, median 65.2, max 70.8): {'50-54': 1, '65-69': 1, '70-74': 1}

[original] entry blocks: -
  CLOSED OGTA         -7.51%  $-6.01  stop  18:34:23 -> 18:35:24
  stop exits: fill vs stop level median -0.66%, worst -0.66% (n=1)
  buys: 1 (1 filled at Jupiter quote), fill vs fast mid median +0.96%, round-trip executable cost median 3.09%

[adjusted] entry blocks: -

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n=   198 median      32  p95     109  max     611
  http:lite-api.jup.ag/price n=   254 median      37  p95     132  max     214
  http:api.geckoterminal.com n=    62 median      33  p95     287  max     446
  http:api.rugcheck.xyz      n=     5 median     381  p95     386  max     386
  http:lite-api.jup.ag/quote n=     3 median      30  p95      30  max      30
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=31: median |div| 1.48%, max |div| 7.05%, |div|>2.6% costs: 11, fast BELOW slow by >2.6%: 9
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=2: median |div| 4.87%, max |div| 7.06%, |div|>2.6% costs: 2, fast BELOW slow by >2.6%: 2
```
