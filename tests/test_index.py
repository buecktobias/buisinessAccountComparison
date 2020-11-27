import unittest
import requests
# TODO implement Test test index page


class IndexPageTest(unittest.TestCase):
    def test_has_title(self):
        r = requests.get("http://127.0.0.1:5001")
        self.assertTrue("<title>" in str(r.content))


if __name__ == '__main__':
    unittest.main()
