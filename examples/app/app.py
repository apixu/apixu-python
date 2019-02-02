import os
from dotenv import dotenv_values
from apixu.client import ApixuClient

os.environ.update(dotenv_values())

api_key = os.environ['APIXUKEY']
client = ApixuClient(api_key)

query = 'London'
current = client.current(q=query)

print(current['location'])
