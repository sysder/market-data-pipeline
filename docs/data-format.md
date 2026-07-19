# 収集データ形式

## openInterest

- 取得間隔：5秒
- 保存先：data/openinterest_btcusdt.jsonl
- 1行の形式：{"received_at":...,"payload":{"symbol":"BTCUSDT","openInterest":"100353.561","time":1784351887684}}
- received_at：ポーラーがレスポンスを受信した時刻、Unix時間ミリ秒
- time：Binanceサーバ時刻、Unix時間ミリ秒

## fundingRate

- 取得間隔：60秒
- 保存先：data/fundingrate_btcusdt.jsonl
- 1行の形式：{"received_at":...,"payload":{"symbol":"BTCUSDT","markPrice":"64816.10000000","indexPrice":"64842.82608696","estimatedSettlePrice":"64853.98697210","lastFundingRate":"0.00005576","interestRate":"0.00010000","nextFundingTime":1784448000000,"time":1784429436000}}
- received_at：ポーラーがレスポンスを受信した時刻、Unix時間ミリ秒
- time：Binanceサーバ時刻、Unix時間ミリ秒
