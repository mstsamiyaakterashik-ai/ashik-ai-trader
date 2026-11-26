
import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.environ.get("BOT_TOKEN")
API = f"https://api.telegram.org/bot{TOKEN}"

def send_message(chat_id, text):
    requests.post(
        f"{API}/sendMessage",
        json={"chat_id": chat_id, "text": text},
        timeout=15
    )

@app.route("/", methods=["GET"])
def home():
    return "ASHIK AI TRADER is running!"

@app.route("/telegram", methods=["POST"])
def telegram():
    data = request.get_json(silent=True) or {}
    message = data.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "").strip().upper()

    if not chat_id:
        return "OK"

    if text == "/START":
        send_message(chat_id, "Welcome to ASHIK AI TRADER!\n\nType SIGNAL for analysis.")

    elif text == "SIGNAL":
        send_message(
            chat_id,
            "ASHIK AI TRADER\n\n"
            "EUR/USD | M1\n"
            "Status: WAIT\n"
            "Live market data is not connected yet."
        )
    else:
        send_message(chat_id, "Type /start or SIGNAL")

    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
