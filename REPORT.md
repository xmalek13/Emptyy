# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2252 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-20T02:53:58-05:00 (137.5s) | last risk tick 2026-11-20T02:54:05-05:00 (120 ms) | risk ticks 10018
Scan loops 209 | last scan: discovered 456 tokens, 454 pairs, 12 in Scout range
Evaluations 974 | unique tokens evaluated 40 | RugCheck ok/fail 234/0 | API errors 3169
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 4, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 8, 'ds-search': 8, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 13, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                     27/115             6/136
Evaluations killed                         832               832
Closed trades                                7                 5
Win rate                                 14.3%              0.0%
Avg win %                                +3.89               n/a
Avg loss %                               -8.79            -23.23
Realized P&L $                          -38.49            -28.70
Equity $ (MTM)                          961.51            971.30
Total P&L $                             -38.49            -28.70
Cash $                                  961.51            971.30
Open positions                               0                 0
Daily-loss halt                              -                 -

Kills by PRIMARY reason:
  bundled>10%(proxy:insider_networks)                 46      46
  liquidity<40k                                      602     602
  mint_authority_not_revoked                          38      38
  pumped>80%_1h                                       30      30
  top10>25%                                            8       8
  vol1h<50k                                          108     108

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                 84      84
  freeze_authority_not_revoked                        38      38
  honeypot/token2022_transfer_restriction              0      38
  liquidity<40k                                      602     602
  lp_not_burned_or_locked                             38      38
  mint_authority_not_revoked                          38      38
  pumped>80%_1h                                       37      37
  top10>25%                                           46      46
  unknown:price_change_1h                            582     582
  vol1h<50k                                          705     705
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=142, median 56.0, max 85.0): {'40-44': 5, '45-49': 17, '50-54': 43, '55-59': 22, '60-64': 13, '65-69': 15, '70-74': 21, '75-79': 4, '80-84': 1, '85-89': 1}

[original] entry blocks: {'cooldown_4h_after_loss': 17, 'already_open': 3}
  CLOSED OGTA         -7.51%  $-6.01  stop  18:34:23 -> 18:35:24
  CLOSED AI           -9.62%  $-7.65  stop  18:58:26 -> 18:59:06
  CLOSED LOOSY       -11.06%  $-8.73  stop  21:58:13 -> 22:00:54
  CLOSED iAgent       -8.28%  $-6.47  stop  23:12:35 -> 23:15:00
  CLOSED OGTA         +3.89%  $+3.02  trailing_stop  01:15:35 -> 01:33:14
  CLOSED OGTA         -7.96%  $-6.20  stop  01:39:36 -> 01:59:11
  CLOSED LOOSY        -8.33%  $-6.45  stop  02:03:37 -> 02:35:20
  stop exits: fill vs stop level median -1.35%, worst -3.17% (n=7)
  buys: 7 (7 filled at Jupiter quote), fill vs fast mid median +1.21%, round-trip executable cost median 2.94%

[adjusted] entry blocks: {'cooldown_4h_after_loss': 1}
  CLOSED AI          -30.26%  $-7.56  stop  18:58:29 -> 19:02:42
  CLOSED OGTA        -21.49%  $-5.33  stop  19:58:11 -> 20:01:36
  CLOSED LOOSY       -20.57%  $-5.08  stop  21:58:16 -> 22:18:00
  CLOSED iAgent      -22.75%  $-5.59  stop  23:48:37 -> 00:00:09
  CLOSED OGTA        -21.08%  $-5.14  stop  02:15:36 -> 02:24:47
  stop exits: fill vs stop level median -2.99%, worst -6.10% (n=5)
  buys: 5 (5 filled at Jupiter quote), fill vs fast mid median +1.68%, round-trip executable cost median 2.67%

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n=  8233 median      38  p95     114  max    1135
  http:lite-api.jup.ag/price n= 10233 median      45  p95     127  max    2737
  http:api.geckoterminal.com n=  2475 median      38  p95     342  max    1397
  http:api.rugcheck.xyz      n=   234 median     372  p95     575  max    2075
  http:lite-api.jup.ag/quote n=    36 median      39  p95     110  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=1752: median |div| 1.07%, max |div| 50.82%, |div|>2.6% costs: 413, fast BELOW slow by >2.6%: 277
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=227: median |div| 1.64%, max |div| 11.58%, |div|>2.6% costs: 64, fast BELOW slow by >2.6%: 45
```
