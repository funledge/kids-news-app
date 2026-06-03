from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Kids News API"

@app.route("/news")
def news():
    return jsonify([
        {
            "title": "テストニュース",
            "summary": "これはテストです",
            "quiz": "AIとは何でしょう？",
            "answer": "人工知能",
            "category": "AI"
        }
    ])

if __name__ == "__main__":
    app.run()
