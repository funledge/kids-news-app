import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

news_text = """
AppleがWWDC2026で新しい製品やサービスを発表しました。
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": """
あなたは小学生向けニュース編集者です。

100文字以内で説明してください。

難しい言葉は使わないでください。

最後にクイズを1問作ってください。
"""
        },
        {
            "role": "user",
            "content": news_text
        }
    ]
)

print(response.choices[0].message.content)