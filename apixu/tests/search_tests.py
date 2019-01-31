import unittest
from schema import schema
import os
from apixu.client import ApixuClient, ApixuException
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

        self.assertEqual(cm.exception.code, 2006)

    def test_search_no_api_key(self):
        client = ApixuClient()
        with self.assertRaises(ApixuException) as cm:
            client.search()

        self.assertEqual(cm.exception.code, 1002)


if __name__ == '__main__':
    unittest.main()
