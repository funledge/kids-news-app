import requests
import os
import gspread

from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

# GNews API
load_dotenv()

API_KEY = os.getenv("GNEWS_API_KEY")

url = f"https://gnews.io/api/v4/top-headlines?category=general&lang=ja&country=jp&max=10&apikey={API_KEY}"

response = requests.get(url)
data = response.json()

# Google Sheets接続
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "kids-news-app-498305-fcc24b7b3575.json",
    scopes=SCOPES
)

client = gspread.authorize(creds)

SPREADSHEET_ID = "1GEjFU21y3oTDaT9QLy_B0am_CWj3UhGwJ0RRPLa1Nyk"

sheet = client.open_by_key(SPREADSHEET_ID).sheet1

# ニュース保存
for article in data["articles"]:

    title = article["title"]

    summary = article.get("description", "")

    sheet.append_row([
        title,
        summary,
        "",
        "",
        "ニュース",
        "",
        article["publishedAt"]
    ])

    print("保存:", title)

print("完了")