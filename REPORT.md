# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 3039 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-20T06:44:23-05:00 (143.7s) | last risk tick 2026-11-20T06:44:58-05:00 (22 ms) | risk ticks 14607
Scan loops 304 | last scan: discovered 412 tokens, 394 pairs, 10 in Scout range
Evaluations 1417 | unique tokens evaluated 46 | RugCheck ok/fail 336/0 | API errors 4640
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 5, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 10, 'ds-search': 8, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 16, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                     49/157            17/189
Evaluations killed                        1211              1211
Closed trades                                9                 7
Win rate                                 22.2%             28.6%
Avg win %                                +3.46             +9.55
Avg loss %                               -9.00            -23.23
Realized P&L $                          -44.04            -24.06
Equity $ (MTM)                          957.68            976.68
Total P&L $                             -42.32            -23.32
Cash $                                  879.48            927.15
Open positions                               1                 2
Daily-loss halt                              -                 -

Kills by PRIMARY reason:
  bundled>10%(proxy:insider_networks)                 65      65
  liquidity<40k                                      871     871
  mint_authority_not_revoked                          58      58
  pumped>80%_1h                                       34      34
  top10>25%                                            8       8
  vol1h<50k                                          175     175

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                123     123
  freeze_authority_not_revoked                        58      58
  honeypot/token2022_transfer_restriction              0      58
  liquidity<40k                                      871     871
  lp_not_burned_or_locked                             58      58
  mint_authority_not_revoked                          58      58
  pumped>80%_1h                                       42      42
  top10>25%                                           66      66
  unknown:price_change_1h                            849     849
  vol1h<50k                                         1040    1040
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=206, median 56.8, max 85.0): {'40-44': 10, '45-49': 26, '50-54': 51, '55-59': 29, '60-64': 20, '65-69': 21, '70-74': 32, '75-79': 15, '80-84': 1, '85-89': 1}

[original] entry blocks: {'cooldown_4h_after_loss': 32, 'already_open': 5, 'max_2_entries_per_token_day': 2}
  OPEN LOOSY      entry 0.00167833 last 0.00175883 (+4.8%) stop 0.00157763 trail off cost $76.48 since 2026-11-20T06:41:47-05:00
  CLOSED OGTA         -7.51%  $-6.01  stop  18:34:23 -> 18:35:24
  CLOSED AI           -9.62%  $-7.65  stop  18:58:26 -> 18:59:06
  CLOSED LOOSY       -11.06%  $-8.73  stop  21:58:13 -> 22:00:54
  CLOSED iAgent       -8.28%  $-6.47  stop  23:12:35 -> 23:15:00
  CLOSED OGTA         +3.89%  $+3.02  trailing_stop  01:15:35 -> 01:33:14
  CLOSED OGTA         -7.96%  $-6.20  stop  01:39:36 -> 01:59:11
  CLOSED LOOSY        -8.33%  $-6.45  stop  02:03:37 -> 02:35:20
  CLOSED iAgent       +3.04%  $+2.34  trailing_stop  03:15:33 -> 03:40:17
  CLOSED iAgent      -10.24%  $-7.89  stop  03:51:36 -> 03:52:29
  stop exits: fill vs stop level median -1.56%, worst -3.60% (n=9)
  buys: 10 (10 filled at Jupiter quote), fill vs fast mid median +1.18%, round-trip executable cost median 2.84%

[adjusted] entry blocks: {'cooldown_4h_after_loss': 7, 'already_open': 1}
  OPEN OGTA       entry 0.000303282 last 0.000313251 (+3.3%) stop 0.000248691 trail off cost $24.40 since 2026-11-20T06:39:13-05:00
  OPEN LOOSY      entry 0.001705 last 0.00175883 (+3.2%) stop 0.0013981 trail off cost $24.39 since 2026-11-20T06:41:50-05:00
  CLOSED AI          -30.26%  $-7.56  stop  18:58:29 -> 19:02:42
  CLOSED OGTA        -21.49%  $-5.33  stop  19:58:11 -> 20:01:36
  CLOSED LOOSY       -20.57%  $-5.08  stop  21:58:16 -> 22:18:00
  CLOSED iAgent      -22.75%  $-5.59  stop  23:48:37 -> 00:00:09
  CLOSED OGTA        -21.08%  $-5.14  stop  02:15:36 -> 02:24:47
  CLOSED iAgent       +2.90%  $+0.70  trailing_stop  05:51:37 -> 06:10:25
  CLOSED LOOSY       +16.20%  $+3.94  trailing_stop  05:56:47 -> 06:30:10
  stop exits: fill vs stop level median -4.76%, worst -9.06% (n=7)
  buys: 9 (9 filled at Jupiter quote), fill vs fast mid median +1.32%, round-trip executable cost median 2.67%

Latency per source (ms, every HTTP call incl. retries; status 200 only):
  http:api.dexscreener.com   n= 12009 median      38  p95     114  max    1135
  http:lite-api.jup.ag/price n= 14912 median      44  p95     127  max    2737
  http:api.geckoterminal.com n=  3573 median      39  p95     340  max    1397
  http:api.rugcheck.xyz      n=   336 median     377  p95     691  max    2075
  http:lite-api.jup.ag/quote n=    55 median      37  p95     128  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=2534: median |div| 1.04%, max |div| 50.82%, |div|>2.6% costs: 575, fast BELOW slow by >2.6%: 393
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=389: median |div| 1.36%, max |div| 11.58%, |div|>2.6% costs: 93, fast BELOW slow by >2.6%: 55
```
