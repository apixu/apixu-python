import unittest
from schema import schema
import os
from apixu.client import ApixuClient, ApixuException
from apixu import errors
from jsonschema import validate


class ForecastTestCase(unittest.TestCase):

    @staticmethod
    def test_forecast():
        api_key = os.environ['APIXUKEY']
        client = ApixuClient(api_key)

        forecast = client.forecast('London', 1, 12)
        validate(forecast, schema.read("forecast.json"))

    def test_forecast_invalid_api_key(self):
        client = ApixuClient('INVALID_KEY')
        with self.assertRaises(ApixuException) as cm:
            client.forecast()

        self.assertEqual(cm.exception.code, errors.API_KEY_INVALID)

    def test_forecast_no_api_key(self):
        client = ApixuClient()
        with self.assertRaises(ApixuException) as cm:
            client.forecast()

        self.assertEqual(cm.exception.code, errors.API_KEY_NOT_PROVIDED)


if __name__ == '__main__':
    unittest.main()
