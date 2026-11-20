# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2252 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-20T02:13:11-05:00 (138.2s) | last risk tick 2026-11-20T02:13:56-05:00 (69 ms) | risk ticks 9215
Scan loops 192 | last scan: discovered 451 tokens, 451 pairs, 21 in Scout range
Evaluations 901 | unique tokens evaluated 40 | RugCheck ok/fail 212/0 | API errors 2916
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 4, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 8, 'ds-search': 8, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 13, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                     25/102             5/122
Evaluations killed                         774               774
Closed trades                                6                 4
Win rate                                 16.7%              0.0%
Avg win %                                +3.89               n/a
Avg loss %                               -8.89            -23.77
Realized P&L $                          -32.04            -23.56
Equity $ (MTM)                          966.69            976.44
Total P&L $                             -33.31            -23.56
Cash $                                  890.53            976.44
Open positions                               1                 0
Daily-loss halt                              -                 -

Kills by PRIMARY reason:
  bundled>10%(proxy:insider_networks)                 42      42
  liquidity<40k                                      562     562
  mint_authority_not_revoked                          35      35
  pumped>80%_1h                                       28      28
  top10>25%                                            8       8
  vol1h<50k                                           99      99

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                 77      77
  freeze_authority_not_revoked                        35      35
  honeypot/token2022_transfer_restriction              0      35
  liquidity<40k                                      562     562
  lp_not_burned_or_locked                             35      35
  mint_authority_not_revoked                          35      35
  pumped>80%_1h                                       35      35
  top10>25%                                           43      43
  unknown:price_change_1h                            545     545
  vol1h<50k                                          656     656
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=127, median 55.0, max 85.0): {'40-44': 5, '45-49': 17, '50-54': 40, '55-59': 19, '60-64': 10, '65-69': 11, '70-74': 20, '75-79': 3, '80-84': 1, '85-89': 1}

[original] entry blocks: {'cooldown_4h_after_loss': 16, 'already_open': 2}
  OPEN LOOSY      entry 0.00115441 last 0.00116364 (+0.8%) stop 0.00108515 trail off cost $77.44 since 2026-11-20T02:03:37-05:00
  CLOSED OGTA         -7.51%  $-6.01  stop  18:34:23 -> 18:35:24
  CLOSED AI           -9.62%  $-7.65  stop  18:58:26 -> 18:59:06
  CLOSED LOOSY       -11.06%  $-8.73  stop  21:58:13 -> 22:00:54
  CLOSED iAgent       -8.28%  $-6.47  stop  23:12:35 -> 23:15:00
  CLOSED OGTA         +3.89%  $+3.02  trailing_stop  01:15:35 -> 01:33:14
  CLOSED OGTA         -7.96%  $-6.20  stop  01:39:36 -> 01:59:11
  stop exits: fill vs stop level median -1.40%, worst -3.17% (n=6)
  buys: 7 (7 filled at Jupiter quote), fill vs fast mid median +1.21%, round-trip executable cost median 2.94%

[adjusted] entry blocks: {'cooldown_4h_after_loss': 1}
  CLOSED AI          -30.26%  $-7.56  stop  18:58:29 -> 19:02:42
  CLOSED OGTA        -21.49%  $-5.33  stop  19:58:11 -> 20:01:36
  CLOSED LOOSY       -20.57%  $-5.08  stop  21:58:16 -> 22:18:00
  CLOSED iAgent      -22.75%  $-5.59  stop  23:48:37 -> 00:00:09
  stop exits: fill vs stop level median -3.88%, worst -6.10% (n=4)
  buys: 4 (4 filled at Jupiter quote), fill vs fast mid median +1.50%, round-trip executable cost median 2.56%

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n=  7541 median      37  p95     114  max    1135
  http:lite-api.jup.ag/price n=  9412 median      44  p95     126  max    2737
  http:api.geckoterminal.com n=  2276 median      37  p95     341  max    1397
  http:api.rugcheck.xyz      n=   212 median     372  p95     691  max    2075
  http:lite-api.jup.ag/quote n=    32 median      39  p95     110  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=1609: median |div| 1.11%, max |div| 50.82%, |div|>2.6% costs: 386, fast BELOW slow by >2.6%: 261
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=170: median |div| 1.88%, max |div| 11.58%, |div|>2.6% costs: 54, fast BELOW slow by >2.6%: 37
```
