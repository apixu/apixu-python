import unittest
from schema import schema
import os
from apixu.client import ApixuClient, ApixuException
from apixu import errors
from jsonschema import validate
import datetime


class HistoryTestCase(unittest.TestCase):

    @staticmethod
    def test_history():
        api_key = os.environ['APIXUKEY']
        client = ApixuClient(api_key)

        now = datetime.datetime.now()
        history = client.history(
            q='London',
            since=datetime.date(now.year, now.month, now.day),
            until=datetime.date(now.year, now.month, now.day),
        )
        validate(history, schema.read("history.json"))

    def test_history_invalid_api_key(self):
        client = ApixuClient('INVALID_KEY')
        with self.assertRaises(ApixuException) as cm:
            client.history()

        self.assertEqual(cm.exception.code, errors.API_KEY_INVALID)

    def test_history_no_api_key(self):
        client = ApixuClient()
        with self.assertRaises(ApixuException) as cm:
            client.history()

        self.assertEqual(cm.exception.code, errors.API_KEY_NOT_PROVIDED)

    def test_history_invalid_since(self):
        client = ApixuClient()
        with self.assertRaises(ApixuException) as cm:
            client.history(since='notdate')

        self.assertEqual(cm.exception.code, 0)

    def test_history_invalid_until(self):
        client = ApixuClient()
        with self.assertRaises(ApixuException) as cm:
            client.history(until='notdate')

        self.assertEqual(cm.exception.code, 0)


if __name__ == '__main__':
    unittest.main()
