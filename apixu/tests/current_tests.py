import unittest
from apixu.client import ApixuClient, ApixuException


class CurrentTestCase(unittest.TestCase):

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
