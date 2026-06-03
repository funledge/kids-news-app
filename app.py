import gspread
from flask import Flask, jsonify
from google.oauth2.service_account import Credentials

app = Flask(__name__)

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


@app.route("/news")
def news():

    rows = sheet.get_all_records()

    return jsonify(rows)


if __name__ == "__main__":
    app.run(debug=True)