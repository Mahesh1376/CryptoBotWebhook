from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("c8a90d84e6c1098d453f216fdb0f6480d7b3cad202b68cc3")
API_SECRET = os.getenv("1b7888990f5090c993a4cc0ce89723462fa89982ff7dcc652adad5c6a064f62c")

def fetch_market_price(symbol):
    url = "https://api.coindcx.com/exchange/v1/margin/create"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for item in data:
            if item.get("market") == symbol:
                return float(item.get("last_price"))
    return None

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("🔥 Webhook received:", data)  # Add this line

    # Then continue your logic to fetch price & place order

    symbol = data.get("symbol")
    side = data.get("side")
    qty = data.get("qty")

    price = fetch_market_price(symbol)
    if not price:
        return jsonify({"status": "error", "message": "Failed to fetch market price."})

    # Simulated trade execution
    def place_order(symbol, side, qty, price):
        url = "https://api.coindcx.com/exchange/v1/margin/create"

    order_data = {
        "market": symbol,
        "side": side,
        "order_type": "market",
        "price": price,
        "quantity": qty,
        "leverage": 3,
        "timestamp": int(time.time() * 1000),
        "ecode": "I"
    }

    print(f"📤 Sending order: {order_data}")

    headers = {
        "Content-Type": "application/json",
        "X-AUTH-APIKEY": API_KEY,
        "X-AUTH-SIGNATURE": generate_signature(order_data),
    }

    response = requests.post(url, headers=headers, json=order_data)

    print(f"📥 Order response status: {response.status_code}")
    print(f"📄 Order response text: {response.text}")

    return response.status_code == 200

import os

port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)




