import requests
from datetime import datetime

BOT_TOKEN = "PUT_TOKEN"
CHAT_ID = "PUT_CHAT_ID"

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg})

if __name__ == "__main__":
    send(f"✅ Bot running at {datetime.now()}")
