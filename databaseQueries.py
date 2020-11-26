import sqlite3


class DatabaseConnection:
    @staticmethod
    def get_all():
        conn = sqlite3.connect("/home/tobias/PycharmProjects/flaskProject/geschaeftskonto")
        cur = conn.execute("SELECT * FROM geschaeftskonto")
        result = cur.fetchall()
        conn.commit()
        return result


if __name__ == '__main__':
    DatabaseConnection.get_all()
