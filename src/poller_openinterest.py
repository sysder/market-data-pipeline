import json
import requests
import time
from pathlib import Path

# データの保存場所
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "openinterest_btcusdt.jsonl"

# URL
url = "https://fapi.binance.com/fapi/v1/openInterest"

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

    with open(DATA_FILE, mode="a", encoding="utf-8") as f:
        f.write(json.dumps(result) + "\n")

    time.sleep(5)

# https://fapi.binance.com/fapi/v1/openInterest?symbol=BTCUSDT