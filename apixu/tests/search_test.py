import unittest
from schema import schema
import os
from apixu.client import ApixuClient, ApixuException
from apixu import errors
from jsonschema import validate


class SearchTestCase(unittest.TestCase):

    @staticmethod
    def test_search():
        api_key = os.environ['APIXUKEY']
        client = ApixuClient(api_key)

        history = client.search(q='London')
        validate(history, schema.read("search.json"))

    def test_search_invalid_api_key(self):
        client = ApixuClient('INVALID_KEY')
        with self.assertRaises(ApixuException) as cm:
            client.search()

        self.assertEqual(cm.exception.code, errors.API_KEY_INVALID)

    def test_search_no_api_key(self):
        client = ApixuClient()
        with self.assertRaises(ApixuException) as cm:
            client.search()

        self.assertEqual(cm.exception.code, errors.API_KEY_NOT_PROVIDED)


if __name__ == '__main__':
    unittest.main()
