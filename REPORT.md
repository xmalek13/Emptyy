# MemeDesk paper-trading report

Simulation only. No wallets, private keys, signing, or real orders.

```
MemeDesk v2 PAPER TRADING (simulated) | started 2026-11-19T18:32:05-05:00 | ends 2026-11-20T09:00:00-05:00 | pid 2406 RUNNING
Box pauses seen by risk thread: 0 (0 s total)
Last scan 2026-11-19T20:43:48-05:00 (137.6s) | last risk tick 2026-11-19T20:44:51-05:00 (107 ms) | risk ticks 2656
Scan loops 55 | last scan: discovered 425 tokens, 424 pairs, 22 in Scout range
Evaluations 226 | unique tokens evaluated 32 | RugCheck ok/fail 52/0 | API errors 841
Unique evaluated tokens by discovery source: {'dstoken-boosts': 1, 'gt:trending_pools': 2, 'gt:dexes/pumpswap/pools': 2, 'dstoken-profiles': 6, 'ds-search': 5, 'gt:pools': 1, 'gt:dexes/bags-fm/pools': 12, 'gt:dexes/meteora-damm-v2/pools': 2, 'dscommunity-takeovers': 1}

                               ORIGINAL (>=70)   ADJUSTED (>=75)
Analyst pass / fail                       6/25              2/29
Evaluations killed                         195               195
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
  bundled>10%(proxy:insider_networks)                 10      10
  liquidity<40k                                      141     141
  mint_authority_not_revoked                          11      11
  pumped>80%_1h                                        6       6
  vol1h<50k                                           27      27

Kills by ANY reason:
  bundled>10%(proxy:insider_networks)                 21      21
  freeze_authority_not_revoked                        11      11
  honeypot/token2022_transfer_restriction              0      11
  liquidity<40k                                      141     141
  lp_not_burned_or_locked                             11      11
  mint_authority_not_revoked                          11      11
  pumped>80%_1h                                       11      11
  top10>25%                                           11      11
  unknown:price_change_1h                            144     144
  vol1h<50k                                          165     165
  (kills caused ONLY by unknown data)                  0       0

Analyst score distribution (n=31, median 53.4, max 85.0): {'40-44': 3, '45-49': 8, '50-54': 8, '55-59': 2, '60-64': 2, '65-69': 2, '70-74': 4, '75-79': 1, '85-89': 1}

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
  http:api.dexscreener.com   n=  2135 median      33  p95     112  max    1014
  http:lite-api.jup.ag/price n=  2713 median      39  p95     125  max    2199
  http:api.geckoterminal.com n=   657 median      34  p95     340  max     913
  http:api.rugcheck.xyz      n=    52 median     374  p95     691  max    2075
  http:lite-api.jup.ag/quote n=    12 median      52  p95     160  max     160
Divergence fast(Jupiter) vs slow(DexScreener) [scan_candidate] n=368: median |div| 1.13%, max |div| 36.27%, |div|>2.6% costs: 100, fast BELOW slow by >2.6%: 64
Divergence fast(Jupiter) vs slow(DexScreener) [open_position] n=17: median |div| 2.68%, max |div| 7.06%, |div|>2.6% costs: 9, fast BELOW slow by >2.6%: 7
```
