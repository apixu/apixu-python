import unittest
from apixu.client import ApixuClient, ApixuException


class HistoryTestCase(unittest.TestCase):

    def test_history_invalid_api_key(self):
        client = ApixuClient('INVALID_KEY')
        with self.assertRaises(ApixuException) as cm:
            client.history()

        self.assertEqual(cm.exception.code, 2006)

    def test_history_no_api_key(self):
        client = ApixuClient()
        with self.assertRaises(ApixuException) as cm:
            client.history()

        self.assertEqual(cm.exception.code, 1002)

    def test_history_invalid_since(self):
        client = ApixuClient()
        with self.assertRaises(ApixuException) as cm:
            client.history(since='notdate')

        self.assertEqual(cm.exception.code, 0)


if __name__ == '__main__':
    unittest.main()
