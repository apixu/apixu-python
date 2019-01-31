import unittest
from schema import schema
import os
from apixu.client import ApixuClient, ApixuException
from jsonschema import validate


class CurrentTestCase(unittest.TestCase):

    @staticmethod
    def test_current():
        api_key = os.environ['APIXUKEY']
        client = ApixuClient(api_key)

        current = client.current('London')
        validate(current, schema.read('current.json'))

    def test_current_invalid_api_key(self):
        client = ApixuClient('INVALID_KEY')
        with self.assertRaises(ApixuException) as cm:
            client.current()

        self.assertEqual(cm.exception.code, 2006)

    def test_current_no_api_key(self):
        client = ApixuClient()
        with self.assertRaises(ApixuException) as cm:
            client.current()

        self.assertEqual(cm.exception.code, 1002)


if __name__ == '__main__':
    unittest.main()
