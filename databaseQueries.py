import sqlite3
import os
from bankObject import BankObject


class DatabaseConnection:
    @classmethod
    def __get_all(cls):
        # TODO connect address ????
        current_dir = os.getcwd()
        database_path = os.path.join(current_dir, "geschaeftskonto")
        conn = sqlite3.connect(database_path)
        cur = conn.execute("SELECT Paket_Name,Bank_Name,Beschreibung, Kosten_Im_Jahr, Logo, Link FROM geschaeftskonto;")
        result = cur.fetchall()
        conn.commit()
        return result

    @classmethod
    def get_all_bank_objects(cls):
        all_rows = cls.__get_all()
        all_bank_objects = []
        for row in all_rows:
            new_bank_object = BankObject(bank_name=row[1], package_name=row[0], price_per_year=row[3], description=row[2], logo=row[4], href=row[5])
            all_bank_objects.append(new_bank_object)
        return all_bank_objects


if __name__ == '__main__':
    print(DatabaseConnection.get_all_bank_objects())
