# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2406 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-19T18:53:31-05:00 (137.2s) | last risk tick 2026-11-19T18:54:29-05:00 (97 ms) | risk ticks 449
Scan loops 9 | last scan: discovered 471 tokens, 437 pairs, 11 in Scout range
Evaluations 41 | unique tokens evaluated 23 | RugCheck ok/fail 10/0 | API errors 141
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 2, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 1, 'ds-search': 3, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 11, 'gt:dexes/meteora-damm-v2/pools': 2}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                        1/5               0/6
Evaluations killed                          35                35
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
  bundled>10%(proxy:insider_networks)                  2       2
  liquidity<40k                                       26      26
  mint_authority_not_revoked                           2       2
  pumped>80%_1h                                        2       2
  vol1h<50k                                            3       3

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                  4       4
  freeze_authority_not_revoked                         2       2
  honeypot/token2022_transfer_restriction              0       2
  liquidity<40k                                       26      26
  lp_not_burned_or_locked                              2       2
  mint_authority_not_revoked                           2       2
  pumped>80%_1h                                        2       2
  top10>25%                                            2       2
  unknown:price_change_1h                             25      25
  vol1h<50k                                           28      28
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=6, median 57.2, max 70.8): {'45-49': 1, '50-54': 1, '55-59': 2, '65-69': 1, '70-74': 1}

[original] entry blocks: -
  CLOSED OGTA         -7.51%  $-6.01  stop  18:34:23 -> 18:35:24
  stop exits: fill vs stop level median -0.66%, worst -0.66% (n=1)
  buys: 1 (1 filled at Jupiter quote), fill vs fast mid median +0.96%, round-trip executable cost median 3.09%

[adjusted] entry blocks: -

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n=   353 median      32  p95     109  max     611
  http:lite-api.jup.ag/price n=   459 median      36  p95     123  max     214
  http:api.geckoterminal.com n=   113 median      34  p95     336  max     590
  http:api.rugcheck.xyz      n=    10 median     378  p95     386  max     386
  http:lite-api.jup.ag/quote n=     3 median      30  p95      30  max      30
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=56: median |div| 1.42%, max |div| 27.93%, |div|>2.6% costs: 17, fast BELOW slow by >2.6%: 15
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=2: median |div| 4.87%, max |div| 7.06%, |div|>2.6% costs: 2, fast BELOW slow by >2.6%: 2
```
