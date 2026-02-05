import requests
from bs4 import BeautifulSoup
import os

BOT_TOKEN = os.getenv("BOT8477262621:AAHaIyBEaUl2zbh-EL8w_66xxjl_9So8kKU_TOKEN")
CHAT_ID = os.getenv("824968295")


def send(msg):
    url = f"https://api.telegram.org/bot{BOT_8477262621:AAHaIyBEaUl2zbh-EL8w_66xxjl_9So8kKUTOKEN}/sendMessage"
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

    TARGET = 5900

    # ====== PRODUCTS ======

    check_product(
        "KENT Ultra Digital 4.5L",
        "https://www.amazon.in/KENT-Digital-Air-Fryer-8L/dp/B0DGKY4WLP/ref=sr_1_6?crid=3PC7HOKD3MY0Y&dib=eyJ2IjoiMSJ9.Ymgecwgq-FxXPqnNLQwhgb7qYkBVokXr9SMtWJuff3KCyZgP0pXmatr4z3YjXBhgUNT-Cg5z7J9-fOwzh-Xa70rB0C6DHhQuHN4H7c23ZEhe1HEUrhlB0zXzywi6Whh5j5_U9WzvUPmsw9R2v6cAxkUdPliAipIh65DhLCqTcL8j_WhRkkYeN9MUNnRyqznCTW4qXi5WdPPWdUFSMcxIoChYkeEhBo9gzwqOXA5mGEQ.03HOm6ZbBcSDZgUnVgdI7MHZX_qi8Hc_HobQcDXUXIM&dib_tag=se&keywords=kent+air+fryer+4+litre&qid=1770294467&sprefix=kent+a%2Caps%2C352&sr=8-6",
        ".a-price-whole",   # Amazon selector
        TARGET
    )

    check_product(
        "Inalsa Tasty Fry DW",
        "https://www.amazon.in/Nutricook-Warranty-Toxin-Free-Coating-No-Microplastics/dp/B0DN162F92/ref=sxbs_pa_sp_search_thematic_btf_sspa?content-id=amzn1.sym.6748dafd-1857-4dd2-9058-aab807cb526e%3Aamzn1.sym.6748dafd-1857-4dd2-9058-aab807cb526e&crid=3PC7HOKD3MY0Y&cv_ct_cx=kent%2Bair%2Bfryer%2B4%2Blitre&keywords=kent%2Bair%2Bfryer%2B4%2Blitre&pd_rd_i=B0DN162F92&pd_rd_r=fcfb1e92-eef0-4a20-aa7a-27fae56aa371&pd_rd_w=dAg4R&pd_rd_wg=oG0lf&pf_rd_p=6748dafd-1857-4dd2-9058-aab807cb526e&pf_rd_r=4N9Q0JPMAEZ2Q8ZGPKYS&qid=1770294467&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=kent%2Ba%2Caps%2C352&sr=1-3-2907eac4-8056-42c7-8014-fdf7bd4c5395-spons&aref=0KnlGcenKg&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWNfYnRm&th=1",
        ".a-price-whole",
        TARGET
    )
