import json
import requests
import time
from pathlib import Path

# データの保存場所
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "fundingrate_btcusdt.jsonl"

# URL
url = "https://fapi.binance.com/fapi/v1/premiumIndex"

# パラメータ
params = {"symbol": "BTCUSDT"}

while True:
    # レスポンスオブジェクトの作成
    response = requests.get(
        url,
        params=params
    )
    
    # データ受信時刻を取得
    current_unixtime_ms = int(time.time() * 1000)

    # JSONとして取得
    data = response.json()
    
    # データ受信時刻を付与
    result = {"received_at": current_unixtime_ms, "payload": data}

    # データの書き込み
    with open(DATA_FILE, mode="a", encoding="utf-8") as f:
        f.write(json.dumps(result) + "\n")

    # 60秒間隔で実行
    time.sleep(60)
