import unittest
from schema import schema
import os
from apixu.client import ApixuClient, ApixuException
from apixu import errors
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

        self.assertEqual(cm.exception.code, errors.API_KEY_INVALID)

    def test_current_no_api_key(self):
        client = ApixuClient()
        with self.assertRaises(ApixuException) as cm:
            client.current()

        self.assertEqual(cm.exception.code, errors.API_KEY_NOT_PROVIDED)


if __name__ == '__main__':
    unittest.main()
