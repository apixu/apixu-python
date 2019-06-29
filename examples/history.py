import datetime
import os

from apixu.client import ApixuClient

api_key = os.environ['APIXUKEY']
client = ApixuClient(api_key)

now = datetime.datetime.now()
history = client.history(q='London', since=datetime.date(now.year, now.month, now.day))

print(history['location']['name'])

for day in history['forecast']['forecastday']:
    print(day['date'])
    print(day['day']['maxtemp_c'])
    print(day['day']['condition']['text'])

'''
{  
   "location":{  
      "name":"London",
      "region":"City of London, Greater London",
      "country":"United Kingdom",
      "lat":51.52,
      "lon":-0.11,
      "tz_id":"Europe/London",
      "localtime_epoch":1548103791,
      "localtime":"2019-01-21 20:49"
   },
   "forecast":{  
      "forecastday":[  
         {  
            "date":"2019-01-21",
            "date_epoch":1548028800,
            "day":{  
               "maxtemp_c":5.2,
               "maxtemp_f":41.4,
               "mintemp_c":1.3,
               "mintemp_f":34.3,
               "avgtemp_c":3.3,
               "avgtemp_f":37.9,
               "maxwind_mph":10.3,
               "maxwind_kph":16.6,
               "totalprecip_mm":0.0,
               "totalprecip_in":0.0,
               "avgvis_km":20.0,
               "avgvis_miles":12.0,
               "avghumidity":80.0,
               "condition":{  
                  "text":"Overcast",
                  "icon":"//cdn.apixu.com/weather/64x64/day/122.png",
                  "code":1009
               },
               "uv":0.0
            },
            "astro":{  
               "sunrise":"07:54 AM",
               "sunset":"04:30 PM",
               "moonrise":"04:58 PM",
               "moonset":"08:08 AM",
               "moon_phase":"Full Moon",
               "moon_illumination":"98"
            },
            "hour":[  
               {  
                  "time_epoch":1548028800,
                  "time":"2019-01-21 00:00",
                  "temp_c":3.2,
                  "temp_f":37.8,
                  "is_day":0,
                  "condition":{  
                     "text":"Partly cloudy",
                     "icon":"//cdn.apixu.com/weather/64x64/night/116.png",
                     "code":1003
                  },
                  "wind_mph":2.5,
                  "wind_kph":4.0,
                  "wind_degree":355,
                  "wind_dir":"N",
                  "pressure_mb":1024.0,
                  "pressure_in":30.7,
                  "precip_mm":0.0,
                  "precip_in":0.0,
                  "humidity":70,
                  "cloud":7,
                  "feelslike_c":2.5,
                  "feelslike_f":36.5,
                  "windchill_c":2.5,
                  "windchill_f":36.5,
                  "heatindex_c":3.2,
                  "heatindex_f":37.8,
                  "dewpoint_c":-1.7,
                  "dewpoint_f":28.9,
                  "will_it_rain":0,
                  "chance_of_rain":"0",
                  "will_it_snow":0,
                  "chance_of_snow":"0",
                  "vis_km":20.0,
                  "vis_miles":12.0
               }
            ]
         }
      ]
   }
}
'''
