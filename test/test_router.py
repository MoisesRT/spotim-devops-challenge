import unittest
import json
import sys

sys.path.append('../app')
import router


class TestStringMethods(unittest.TestCase):
    def test_dynamo_response(self):
        self.assertTrue('secret_code' in json.loads(router.secret()))

    def test_health_response(self):
        self.assertTrue('status' in json.loads(router.health()))


if __name__ == '__main__':
    unittest.main()
