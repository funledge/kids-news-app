import gspread
from google.oauth2.service_account import Credentials

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

sheet.append_row([
    "テストニュース",
    "これはテストです",
    "AIとは何でしょう？",
    "人工知能",
    "AI",
    "",
    "2026-06-03"
])

print("追加成功")
