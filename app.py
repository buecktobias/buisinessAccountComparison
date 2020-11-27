from flask import Flask, render_template

from databaseQueries import DatabaseConnection

app = Flask(__name__)


@app.route('/')
def index():
    all_banks = DatabaseConnection.get_all()
    return render_template("index.html", banks=all_banks)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001)
