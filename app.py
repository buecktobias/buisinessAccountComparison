from flask import Flask, render_template

from bankObject import BankObject
from databaseQueries import DatabaseConnection

app = Flask(__name__)


@app.route('/')
def index():
    all_banks = DatabaseConnection.get_all_bank_objects()
    column_names = ["Bank", "Beschreibung", "Preis im Jahr"]
    return render_template("index.html", banks=all_banks, column_names=column_names)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001)
