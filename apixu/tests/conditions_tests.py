import unittest
from schema import schema
from apixu.client import ApixuClient
from jsonschema import validate


class CurrentTestCase(unittest.TestCase):

    @staticmethod
    def test_conditions():
        client = ApixuClient()

        conditions = client.conditions()
        validate(conditions, schema.read("conditions.json"))


if __name__ == '__main__':
    unittest.main()
