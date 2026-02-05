import requests
from bs4 import BeautifulSoup
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg})


headers = {
    "User-Agent": "Mozilla/5.0"
}


def get_price(url, selector):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    el = soup.select_one(selector)
    if not el:
        return None

    price = el.text.replace(",", "").replace("₹", "").strip()
    return int(price)


def check_product(name, url, selector, target):

    price = get_price(url, selector)

    if price is None:
        send(f"⚠️ Could not read price for {name}")
        return

    if price <= target:
        send(f"🔥 PRICE DROP!\n{name}\n₹{price} (target ₹{target})")


if __name__ == "__main__":

    TARGET = 3000

    # ====== PRODUCTS ======

    check_product(
        "KENT Ultra Digital 4.5L",
        "PASTE_KENT_AMAZON_LINK_HERE",
        ".a-price-whole",   # Amazon selector
        TARGET
    )

    check_product(
        "Inalsa Tasty Fry DW",
        "PASTE_INALSA_AMAZON_LINK_HERE",
        ".a-price-whole",
        TARGET
    )
