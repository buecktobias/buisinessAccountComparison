import unittest

from databaseQueries import DatabaseConnection


class MyDatabaseTest(unittest.TestCase):
    def test_get_all(self):
        database_result = DatabaseConnection.get_all()


if __name__ == '__main__':
    unittest.main()
