import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GNEWS_API_KEY")

url = f"https://gnews.io/api/v4/top-headlines?category=general&lang=ja&country=jp&max=10&apikey={API_KEY}"

response = requests.get(url)

data = response.json()

print(data)

for article in data["articles"]:
    print(article["title"])