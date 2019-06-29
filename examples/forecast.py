import os

from apixu.client import ApixuClient

api_key = os.environ['APIXUKEY']
client = ApixuClient(api_key=api_key, lang="es")

forecast = client.forecast(q='London', days=2)

print(forecast['location']['name'])

print(forecast['current']['last_updated_epoch'])
print(forecast['current']['condition']['text'])

for day in forecast['forecast']['forecastday']:
    print(day['date'])
    print(day['day']['maxtemp_c'])

'''
{  
   "location":{  
      "name":"London",
      "region":"City of London, Greater London",
      "country":"United Kingdom",
      "lat":51.52,
      "lon":-0.11,
      "tz_id":"Europe/London",
      "localtime_epoch":1548103480,
      "localtime":"2019-01-21 20:44"
   },
   "current":{  
      "last_updated_epoch":1548102624,
      "last_updated":"2019-01-21 20:30",
      "temp_c":4.0,
      "temp_f":39.2,
      "is_day":0,
      "condition":{  
         "text":"Clear",
         "icon":"//cdn.apixu.com/weather/64x64/night/113.png",
         "code":1000
      },
      "wind_mph":6.9,
      "wind_kph":11.2,
      "wind_degree":210,
      "wind_dir":"SSW",
      "pressure_mb":1015.0,
      "pressure_in":30.4,
      "precip_mm":0.0,
      "precip_in":0.0,
      "humidity":81,
      "cloud":0,
      "feelslike_c":1.2,
      "feelslike_f":34.2,
      "vis_km":10.0,
      "vis_miles":6.0,
      "uv":0.0
   },
   "forecast":{  
      "forecastday":[  
         {  
            "date":"2019-01-21",
            "date_epoch":1548028800,
            "day":{  
               "maxtemp_c":5.1,
               "maxtemp_f":41.2,
               "mintemp_c":-1.4,
               "mintemp_f":29.5,
               "avgtemp_c":2.5,
               "avgtemp_f":36.5,
               "maxwind_mph":8.9,
               "maxwind_kph":14.4,
               "totalprecip_mm":0.0,
               "totalprecip_in":0.0,
               "avgvis_km":18.7,
               "avgvis_miles":11.0,
               "avghumidity":76.0,
               "condition":{  
                  "text":"Partly cloudy",
                  "icon":"//cdn.apixu.com/weather/64x64/day/116.png",
                  "code":1003
               },
               "uv":0.7
            },
            "astro":{  
               "sunrise":"07:54 AM",
               "sunset":"04:30 PM",
               "moonrise":"04:58 PM",
               "moonset":"08:08 AM"
            }
         }
      ]
   }
}
'''
