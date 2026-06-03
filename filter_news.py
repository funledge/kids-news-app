from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("OPENAI_API_KEY"))

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def is_kids_news(title, description):

    prompt = f"""
あなたは小学生向けニュース編集長です。

以下のニュースを判定してください。

掲載してよいジャンル
・AI
・科学
・宇宙
・環境
・経済
・お金
・世界情勢
・歴史
・教育
・テクノロジー
・防災

掲載しないジャンル
・芸能
・恋愛
・ゴシップ
・スキャンダル
・スポーツ結果
・広告

回答はYESかNOのみ。

タイトル:
{title}

概要:
{description}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response.choices[0].message.content.strip()

    return result == "YES"

print(
    is_kids_news(
        "台風6号が関東へ接近",
        "強い雨風に注意が必要です"
    )
)

print(
    is_kids_news(
        "嵐の松本潤が結婚か",
        "熱愛報道で話題"
    )
)