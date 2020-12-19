import requests
from flask import Flask, render_template, request

from bankObjectSorter import BankObjectSorter
from column import Column
from databaseQueries import DatabaseConnection
from restdbioAccess import save_email_address
app = Flask(__name__)


def get_columns():
    #column_names = [Column("Bank", False, ""), Column("Beschreibung", False, ""), Column("Preis im Jahr", True, "price_per_year")]
    pass

@app.route('/comparison')
def index():
    column = request.args.get('sort_by', None)
    is_ascending = request.args.get('sort_type', None)
    all_banks = DatabaseConnection.get_all_bank_objects()
    print(column)
    if column is not None and column == "price_per_year":
        all_banks = BankObjectSorter().sort_by_price(all_banks)

    return render_template("index.html", banks=all_banks)


@app.route('/')
def email_signup():
    return render_template("email_signup.html")


@app.route('/email/', methods=["POST"])
def add_email_to_database():
    email = request.form.get("email")
    print(email)
    save_email_address(email)
    return render_template("email_signed_up.html")


if __name__ == '__main__':
    #add_to_database()
    app.run(host="127.0.0.1", port=5001)
