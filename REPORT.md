# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2252 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-20T03:41:58-05:00 (133.4s) | last risk tick 2026-11-20T03:44:17-05:00 (37 ms) | risk ticks 11022
Scan loops 229 | last scan: discovered 462 tokens, 462 pairs, 21 in Scout range
Evaluations 1056 | unique tokens evaluated 43 | RugCheck ok/fail 252/0 | API errors 3487
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 5, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 9, 'ds-search': 8, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 14, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                     33/119             7/145
Evaluations killed                         904               904
Closed trades                                8                 5
Win rate                                 25.0%              0.0%
Avg win %                                +3.46               n/a
Avg loss %                               -8.79            -23.23
Realized P&L $                          -36.15            -28.70
Equity $ (MTM)                          963.85            971.30
Total P&L $                             -36.15            -28.70
Cash $                                  963.85            971.30
Open positions                               0                 0
Daily-loss halt                              -                 -

Kills by PRIMARY reason:
  bundled>10%(proxy:insider_networks)                 50      50
  liquidity<40k                                      653     653
  mint_authority_not_revoked                          42      42
  pumped>80%_1h                                       30      30
  top10>25%                                            8       8
  vol1h<50k                                          121     121

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                 92      92
  freeze_authority_not_revoked                        42      42
  honeypot/token2022_transfer_restriction              0      42
  liquidity<40k                                      653     653
  lp_not_burned_or_locked                             42      42
  mint_authority_not_revoked                          42      42
  pumped>80%_1h                                       38      38
  top10>25%                                           50      50
  unknown:price_change_1h                            629     629
  vol1h<50k                                          768     768
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=152, median 56.4, max 85.0): {'40-44': 5, '45-49': 18, '50-54': 43, '55-59': 23, '60-64': 13, '65-69': 17, '70-74': 26, '75-79': 5, '80-84': 1, '85-89': 1}

[original] entry blocks: {'cooldown_4h_after_loss': 20, 'already_open': 5}
  CLOSED OGTA         -7.51%  $-6.01  stop  18:34:23 -> 18:35:24
  CLOSED AI           -9.62%  $-7.65  stop  18:58:26 -> 18:59:06
  CLOSED LOOSY       -11.06%  $-8.73  stop  21:58:13 -> 22:00:54
  CLOSED iAgent       -8.28%  $-6.47  stop  23:12:35 -> 23:15:00
  CLOSED OGTA         +3.89%  $+3.02  trailing_stop  01:15:35 -> 01:33:14
  CLOSED OGTA         -7.96%  $-6.20  stop  01:39:36 -> 01:59:11
  CLOSED LOOSY        -8.33%  $-6.45  stop  02:03:37 -> 02:35:20
  CLOSED iAgent       +3.04%  $+2.34  trailing_stop  03:15:33 -> 03:40:17
  stop exits: fill vs stop level median -1.46%, worst -3.60% (n=8)
  buys: 8 (8 filled at Jupiter quote), fill vs fast mid median +1.18%, round-trip executable cost median 2.92%

[adjusted] entry blocks: {'cooldown_4h_after_loss': 2}
  CLOSED AI          -30.26%  $-7.56  stop  18:58:29 -> 19:02:42
  CLOSED OGTA        -21.49%  $-5.33  stop  19:58:11 -> 20:01:36
  CLOSED LOOSY       -20.57%  $-5.08  stop  21:58:16 -> 22:18:00
  CLOSED iAgent      -22.75%  $-5.59  stop  23:48:37 -> 00:00:09
  CLOSED OGTA        -21.08%  $-5.14  stop  02:15:36 -> 02:24:47
  stop exits: fill vs stop level median -2.99%, worst -6.10% (n=5)
  buys: 5 (5 filled at Jupiter quote), fill vs fast mid median +1.68%, round-trip executable cost median 2.67%

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n=  9072 median      38  p95     114  max    1135
  http:lite-api.jup.ag/price n= 11256 median      45  p95     128  max    2737
  http:api.geckoterminal.com n=  2723 median      39  p95     340  max    1397
  http:api.rugcheck.xyz      n=   252 median     374  p95     691  max    2075
  http:lite-api.jup.ag/quote n=    39 median      40  p95     131  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=1914: median |div| 1.07%, max |div| 50.82%, |div|>2.6% costs: 446, fast BELOW slow by >2.6%: 303
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=275: median |div| 1.40%, max |div| 11.58%, |div|>2.6% costs: 67, fast BELOW slow by >2.6%: 46
```
