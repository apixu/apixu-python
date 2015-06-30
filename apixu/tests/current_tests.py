import unittest
from apixu.client import ApixuClient, ApixuException


class CurrentTestCase(unittest.TestCase):

    def test_getCurrentWeather_invalid_api_key(self):
        client = ApixuClient('INVALID_KEY')
        with self.assertRaises(ApixuException) as cm:
            client.getCurrentWeather()

        self.assertEqual(cm.exception.code, 2006)

    def test_getCurrentWeather_no_api_key(self):
        client = ApixuClient()
        with self.assertRaises(ApixuException) as cm:
            client.getCurrentWeather()

        self.assertEqual(cm.exception.code, 1002)

if __name__ == '__main__':
    unittest.main()
