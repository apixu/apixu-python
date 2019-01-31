import os

from apixu.client import ApixuClient

api_key = os.environ['APIXUKEY']
client = ApixuClient(api_key)

search = client.search(q='London')

for location in search:
    print(location['id'])
    print(location['name'])
    print(location['region'])
    print('\n')

'''
[  
   {  
      "id":2801268,
      "name":"London, City of London, Greater London, United Kingdom",
      "region":"City of London, Greater London",
      "country":"United Kingdom",
      "lat":51.52,
      "lon":-0.11,
      "url":"london-city-of-london-greater-london-united-kingdom"
   }
]
'''
