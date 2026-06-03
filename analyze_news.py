import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

title = "台風6号が関東へ接近"
description = "強い雨や風が予想されています"

prompt = f"""
あなたは小学生向けニュース編集者です。

ニュースを分析してください。

返答はJSONのみ。

カテゴリは以下から選ぶ。

AI
科学
経済
世界
歴史
防災
除外

ニュース

タイトル:
{title}

概要:
{description}

返答形式

{{
 "category":"",
 "summary":"",
 "quiz":"",
 "answer":""
}}
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

result = json.loads(
    response.choices[0].message.content
)

print(result)