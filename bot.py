import requests
from datetime import datetime

BOT_TOKEN = "8477262621:AAHaIyBEaUl2zbh-EL8w_66xxjl_9So8kKU    "
CHAT_ID = "824968295"

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg})

if __name__ == "__main__":
    send(f"✅ Bot running at {datetime.now()}")
