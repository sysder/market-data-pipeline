# 収集データ形式

## openInterest

- 取得間隔：5秒
- 保存先：data/openinterest_btcusdt.jsonl
- 1行の形式：{"received_at":...,"payload":{"symbol":"BTCUSDT","openInterest":"100353.561","time":1784351887684}}
- received_at：ポーラーがレスポンスを受信した時刻、Unix時間ミリ秒
- time：Binanceサーバ時刻、Unix時間ミリ秒
