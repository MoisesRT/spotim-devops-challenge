import unittest
import sys

sys.path.append('../app')
from app import app


class TestStringMethods(unittest.TestCase):
    def test_if_app_has_health(self):
        self.assertTrue('health' in app.url_map._rules_by_endpoint)

    def test_if_app_has_secret(self):
        self.assertTrue('secret' in app.url_map._rules_by_endpoint)


if __name__ == '__main__':
    unittest.main()
