import os

from apixu.client import ApixuClient

api_key = os.environ['APIXUKEY']
client = ApixuClient(api_key)

conditions = client.conditions()

for condition in conditions:
    print(condition['code'])
    print(condition['day'])
    print(condition['icon'])
    print('\n')

'''
[
    {
        "code" : 1000,
        "day" : "Sunny",
        "night" : "Clear",
        "icon" : 113
    }
]
'''
