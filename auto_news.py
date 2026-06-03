import os
import json
import requests
import gspread

from dotenv import load_dotenv
from openai import OpenAI
from google.oauth2.service_account import Credentials

load_dotenv()

# -------------------
# API設定
# -------------------

GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

# -------------------
# Google Sheets
# -------------------

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "kids-news-app-498305-fcc24b7b3575.json",
    scopes=SCOPES
)

gc = gspread.authorize(creds)

SPREADSHEET_ID = "1GEjFU21y3oTDaT9QLy_B0am_CWj3UhGwJ0RRPLa1Nyk"

sheet = gc.open_by_key(SPREADSHEET_ID).sheet1

# 既存タイトル取得
existing_titles = sheet.col_values(1)

# -------------------
# GNews取得
# -------------------

url = f"https://gnews.io/api/v4/top-headlines?lang=ja&country=jp&max=5&apikey={GNEWS_API_KEY}"

news_data = requests.get(url).json()

# -------------------
# 記事ごと処理
# -------------------

for article in news_data["articles"]:

    title = article["title"]
    description = article.get("description", "")

    # 重複チェック
    if title in existing_titles:
        print("重複スキップ:", title)
        continue

    print("処理中:", title)

    prompt = f"""
あなたは小学生向けニュース編集者です。

以下のニュースを分析してください。

カテゴリは必ず以下から選ぶ

AI
科学
経済
世界
歴史
防災
除外

返答はJSONのみ

タイトル:
{title}

概要:
{description}

形式:

{{
 "category":"",
 "summary":"",
 "quiz":"",
 "answer":""
}}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        response_format={"type":"json_object"},
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    result = json.loads(
        response.choices[0].message.content
    )

    # 除外記事は保存しない
    if result["category"] == "除外":
        print("除外")
        continue

    sheet.append_row([
        title,
        result["summary"],
        result["quiz"],
        result["answer"],
        result["category"],
        "",
        ""
])

print("保存完了")