# 決定

60秒間隔を採用

# 理由

- 実測（下記）の結果、lastFundingRateに一定の更新周期は観測されなかった（ファンディングレートの更新は、市場の動きに依存するため）
- よってサーバ周期への整合という0004-建玉データの基準は適用できない
- したがって、8時間かけて決済値へ収束していくその軌跡を描くためには、60秒間隔で十分と判断した

## 重複の定義（0004から基準を変更）

基準はtimeではなくlastFundingRate（取得したい対象のフィールド）。premiumIndexのtimeはmarkPriceの再計算でほぼ毎応答変わるため、time基準では無駄撃ち率が常に約0%となり指標にならない。

- 無駄撃ち率 = (行数 − ユニークな lastFundingRate の数) / 行数。新しい値を運ばなかったリクエストの割合（効率の指標）
- 多重捕捉率 = 同一lastFundingRateが2回以上現れる行の割合（取りこぼしにくさの指標）

## データの観察

観測日: 2026-07-19。"https://fapi.binance.com/fapi/v1/premiumIndex?symbol=BTCUSDT" を叩いて調査した。

| sleep | 行数 | ユニーク lastFundingRate | 無駄撃ち率 | 多重捕捉率 |
|---|---|---|---|---|
| 10秒 | 10 | 2 | 80% (8/10) | 100% (10/10) |
| 5秒 | 10 | 2 | 80% (8/10) | 100% (10/10) |
| 30秒 | 10 | 4 | 60% (6/10) | 100% (10/10) |
| 40秒 | 10 | 5 | 50% (5/10) | 80% (8/10) |
| 50秒 | 11 | 6 | 45% (5/11) | 73% (8/11) |
| 60秒 | 10 | 6 | 40% (4/10) | 80% (8/10) |

注意:
- 各標本は10行前後と小さく、値の変化頻度は市場の動きに依存するため、率は目安

time.sleep(10)：無駄撃ち率 80% (8/10)・多重捕捉率 100% (10/10)
```json
{"symbol":"BTCUSDT","markPrice":"64750.10000000","indexPrice":"64768.97108696","estimatedSettlePrice":"64774.66340918","lastFundingRate":"0.00003098","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425510000}
{"symbol":"BTCUSDT","markPrice":"64750.03601449","indexPrice":"64768.97108696","estimatedSettlePrice":"64774.61441159","lastFundingRate":"0.00003098","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425520000}
{"symbol":"BTCUSDT","markPrice":"64750.04385507","indexPrice":"64768.95217391","estimatedSettlePrice":"64774.56455881","lastFundingRate":"0.00003098","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425530010}
{"symbol":"BTCUSDT","markPrice":"64750.10000000","indexPrice":"64768.95000000","estimatedSettlePrice":"64774.51018577","lastFundingRate":"0.00003098","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425541000}
{"symbol":"BTCUSDT","markPrice":"64750.07437781","indexPrice":"64768.97913043","estimatedSettlePrice":"64774.46029855","lastFundingRate":"0.00003098","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425551003}
{"symbol":"BTCUSDT","markPrice":"64750.00000000","indexPrice":"64768.86891304","estimatedSettlePrice":"64774.42184082","lastFundingRate":"0.00003211","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425561000}
{"symbol":"BTCUSDT","markPrice":"64750.02251449","indexPrice":"64768.89260870","estimatedSettlePrice":"64774.39712669","lastFundingRate":"0.00003211","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425571000}
{"symbol":"BTCUSDT","markPrice":"64750.08476762","indexPrice":"64768.94173913","estimatedSettlePrice":"64774.36968677","lastFundingRate":"0.00003211","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425581001}
{"symbol":"BTCUSDT","markPrice":"64750.08766667","indexPrice":"64768.95173913","estimatedSettlePrice":"64774.34840604","lastFundingRate":"0.00003211","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425591000}
{"symbol":"BTCUSDT","markPrice":"64750.09110145","indexPrice":"64768.98608696","estimatedSettlePrice":"64774.32179686","lastFundingRate":"0.00003211","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425601006}
```

time.sleep(5)：無駄撃ち率 80% (8/10)・多重捕捉率 100% (10/10)
```json
{"symbol":"BTCUSDT","markPrice":"64750.08271014","indexPrice":"64768.99217391","estimatedSettlePrice":"64774.15815018","lastFundingRate":"0.00003211","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425671001}
{"symbol":"BTCUSDT","markPrice":"64750.10000000","indexPrice":"64768.99652174","estimatedSettlePrice":"64774.14727005","lastFundingRate":"0.00003211","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425676001}
{"symbol":"BTCUSDT","markPrice":"64750.05340580","indexPrice":"64768.97913043","estimatedSettlePrice":"64774.13805314","lastFundingRate":"0.00003325","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425681000}
{"symbol":"BTCUSDT","markPrice":"64750.10000000","indexPrice":"64768.99000000","estimatedSettlePrice":"64774.12510809","lastFundingRate":"0.00003325","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425686009}
{"symbol":"BTCUSDT","markPrice":"64750.00000000","indexPrice":"64768.93108696","estimatedSettlePrice":"64774.11706751","lastFundingRate":"0.00003325","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425691007}
{"symbol":"BTCUSDT","markPrice":"64750.10000000","indexPrice":"64768.93978261","estimatedSettlePrice":"64774.11206872","lastFundingRate":"0.00003325","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425696000}
{"symbol":"BTCUSDT","markPrice":"64750.01370315","indexPrice":"64768.93978261","estimatedSettlePrice":"64774.10635495","lastFundingRate":"0.00003325","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425701000}
{"symbol":"BTCUSDT","markPrice":"64750.02296377","indexPrice":"64768.93978261","estimatedSettlePrice":"64774.10019348","lastFundingRate":"0.00003325","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425706000}
{"symbol":"BTCUSDT","markPrice":"64750.08507971","indexPrice":"64768.99217391","estimatedSettlePrice":"64774.09412150","lastFundingRate":"0.00003325","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425711000}
{"symbol":"BTCUSDT","markPrice":"64750.10000000","indexPrice":"64768.99869565","estimatedSettlePrice":"64774.08769698","lastFundingRate":"0.00003325","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784425716002}
```

time.sleep(30)：無駄撃ち率 60% (6/10)・多重捕捉率 100% (10/10)
```json
{"symbol":"BTCUSDT","markPrice":"64762.52819340","indexPrice":"64779.85586957","estimatedSettlePrice":"64773.25680447","lastFundingRate":"0.00003761","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426053000}
{"symbol":"BTCUSDT","markPrice":"64761.89527536","indexPrice":"64779.82239130","estimatedSettlePrice":"64773.36860314","lastFundingRate":"0.00003761","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426083000}
{"symbol":"BTCUSDT","markPrice":"64753.61889130","indexPrice":"64772.55500000","estimatedSettlePrice":"64773.40030278","lastFundingRate":"0.00003865","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426113000}
{"symbol":"BTCUSDT","markPrice":"64752.45692654","indexPrice":"64772.43826087","estimatedSettlePrice":"64773.30494469","lastFundingRate":"0.00003865","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426143009}
{"symbol":"BTCUSDT","markPrice":"64751.52023188","indexPrice":"64772.51586957","estimatedSettlePrice":"64773.16734988","lastFundingRate":"0.00003981","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426173000}
{"symbol":"BTCUSDT","markPrice":"64751.36172414","indexPrice":"64772.55434783","estimatedSettlePrice":"64773.02191423","lastFundingRate":"0.00003981","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426203001}
{"symbol":"BTCUSDT","markPrice":"64752.19890580","indexPrice":"64773.53956522","estimatedSettlePrice":"64772.89262850","lastFundingRate":"0.00004073","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426234000}
{"symbol":"BTCUSDT","markPrice":"64751.26556222","indexPrice":"64773.55478261","estimatedSettlePrice":"64772.78551401","lastFundingRate":"0.00004073","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426264000}
{"symbol":"BTCUSDT","markPrice":"64751.25647676","indexPrice":"64773.54826087","estimatedSettlePrice":"64772.68410350","lastFundingRate":"0.00004073","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426294000}
{"symbol":"BTCUSDT","markPrice":"64751.24828986","indexPrice":"64773.54021739","estimatedSettlePrice":"64772.58115664","lastFundingRate":"0.00004073","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426324009}
```

time.sleep(40)：無駄撃ち率 50% (5/10)・多重捕捉率 80% (8/10)
```json
{"symbol":"BTCUSDT","markPrice":"64750.00000000","indexPrice":"64769.84956522","estimatedSettlePrice":"64772.34266663","lastFundingRate":"0.00004155","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426396000}
{"symbol":"BTCUSDT","markPrice":"64750.35368116","indexPrice":"64769.22913043","estimatedSettlePrice":"64772.17233587","lastFundingRate":"0.00004227","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426437000}
{"symbol":"BTCUSDT","markPrice":"64750.00000000","indexPrice":"64768.76608696","estimatedSettlePrice":"64772.00910072","lastFundingRate":"0.00004227","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426477000}
{"symbol":"BTCUSDT","markPrice":"64714.50000000","indexPrice":"64737.44869565","estimatedSettlePrice":"64771.26764599","lastFundingRate":"0.00004227","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426517000}
{"symbol":"BTCUSDT","markPrice":"64746.18132609","indexPrice":"64765.54347826","estimatedSettlePrice":"64770.79756075","lastFundingRate":"0.00004330","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426557000}
{"symbol":"BTCUSDT","markPrice":"64762.00000000","indexPrice":"64778.06869565","estimatedSettlePrice":"64770.76232472","lastFundingRate":"0.00004430","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426597001}
{"symbol":"BTCUSDT","markPrice":"64807.57485507","indexPrice":"64824.17717391","estimatedSettlePrice":"64771.38206727","lastFundingRate":"0.00004430","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426637000}
{"symbol":"BTCUSDT","markPrice":"64800.14602899","indexPrice":"64823.90130435","estimatedSettlePrice":"64772.56556896","lastFundingRate":"0.00004559","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426677000}
{"symbol":"BTCUSDT","markPrice":"64807.80000000","indexPrice":"64826.71673913","estimatedSettlePrice":"64773.62059010","lastFundingRate":"0.00004559","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426717000}
{"symbol":"BTCUSDT","markPrice":"64811.15440580","indexPrice":"64832.64673913","estimatedSettlePrice":"64774.86457379","lastFundingRate":"0.00004559","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426758000}
```

time.sleep(50)：無駄撃ち率 45% (5/11)・多重捕捉率 73% (8/11)
```json
{"symbol":"BTCUSDT","markPrice":"64868.10000000","indexPrice":"64885.30543478","estimatedSettlePrice":"64777.92182114","lastFundingRate":"0.00004710","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426827001}
{"symbol":"BTCUSDT","markPrice":"64870.05235507","indexPrice":"64891.12108696","estimatedSettlePrice":"64781.55788104","lastFundingRate":"0.00004710","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426877003}
{"symbol":"BTCUSDT","markPrice":"64832.44173913","indexPrice":"64858.84108696","estimatedSettlePrice":"64784.43432160","lastFundingRate":"0.00004710","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426927006}
{"symbol":"BTCUSDT","markPrice":"64818.91773913","indexPrice":"64848.38826087","estimatedSettlePrice":"64786.70643019","lastFundingRate":"0.00004807","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784426978002}
{"symbol":"BTCUSDT","markPrice":"64853.00000000","indexPrice":"64870.20608696","estimatedSettlePrice":"64788.96573092","lastFundingRate":"0.00004844","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784427028000}
{"symbol":"BTCUSDT","markPrice":"64870.20000000","indexPrice":"64885.49565217","estimatedSettlePrice":"64791.99639027","lastFundingRate":"0.00004910","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784427078003}
{"symbol":"BTCUSDT","markPrice":"64847.17787681","indexPrice":"64874.38347826","estimatedSettlePrice":"64795.12832967","lastFundingRate":"0.00004910","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784427128001}
{"symbol":"BTCUSDT","markPrice":"64860.80000000","indexPrice":"64882.12869565","estimatedSettlePrice":"64798.05868587","lastFundingRate":"0.00004910","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784427178000}
{"symbol":"BTCUSDT","markPrice":"64885.00000000","indexPrice":"64897.87000000","estimatedSettlePrice":"64801.46334034","lastFundingRate":"0.00004976","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784427228000}
{"symbol":"BTCUSDT","markPrice":"64880.90000000","indexPrice":"64898.50108696","estimatedSettlePrice":"64805.21142488","lastFundingRate":"0.00005067","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784427279000}
{"symbol":"BTCUSDT","markPrice":"64881.83586232","indexPrice":"64899.09217391","estimatedSettlePrice":"64808.72735676","lastFundingRate":"0.00005067","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784427329000}
```

time.sleep(60)：無駄撃ち率 40% (4/10)・多重捕捉率 80% (8/10)
```json
{"symbol":"BTCUSDT","markPrice":"64813.20000000","indexPrice":"64840.86913043","estimatedSettlePrice":"64859.56607922","lastFundingRate":"0.00005569","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784429136001}
{"symbol":"BTCUSDT","markPrice":"64812.48796377","indexPrice":"64840.23891304","estimatedSettlePrice":"64857.29217476","lastFundingRate":"0.00005569","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784429196000}
{"symbol":"BTCUSDT","markPrice":"64802.80655072","indexPrice":"64833.56173913","estimatedSettlePrice":"64855.29665640","lastFundingRate":"0.00005586","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784429256000}
{"symbol":"BTCUSDT","markPrice":"64792.20000000","indexPrice":"64824.72130435","estimatedSettlePrice":"64854.26108539","lastFundingRate":"0.00005593","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784429316000}
{"symbol":"BTCUSDT","markPrice":"64795.40000000","indexPrice":"64824.77304348","estimatedSettlePrice":"64853.43622524","lastFundingRate":"0.00005576","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784429376000}
{"symbol":"BTCUSDT","markPrice":"64816.10000000","indexPrice":"64842.82608696","estimatedSettlePrice":"64853.98697210","lastFundingRate":"0.00005576","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784429436000}
{"symbol":"BTCUSDT","markPrice":"64802.24734058","indexPrice":"64831.44804348","estimatedSettlePrice":"64854.93784420","lastFundingRate":"0.00005593","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784429496000}
{"symbol":"BTCUSDT","markPrice":"64808.83889855","indexPrice":"64836.90913043","estimatedSettlePrice":"64855.57012428","lastFundingRate":"0.00005615","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784429557000}
{"symbol":"BTCUSDT","markPrice":"64839.38604348","indexPrice":"64859.92173913","estimatedSettlePrice":"64856.37417814","lastFundingRate":"0.00005615","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784429617000}
{"symbol":"BTCUSDT","markPrice":"64816.88321739","indexPrice":"64846.97934783","estimatedSettlePrice":"64857.07182041","lastFundingRate":"0.00005647","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784429677000}
```
