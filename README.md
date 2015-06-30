apixu-client
========

A python client library to call Apixu api.

Installation:
-------------------
python setup.py install


Example usage:
-------------------

```python
from apixu.client import ApixuClient, ApixuException
api_key = 'xxxxxxxxxxxx'
client = ApixuClient(api_key)

###########################
# current weather
###########################
current = client.getCurrentWeather(q='London')
# "current" is a dict with a structure like this:
"""
{
    'current': {
        'cloud': 0,
        'condition': {
            'code': 1000,
            'icon': 'http://www.apixu.com/static/weather/64x64/day/113.png',
            'text': 'Sunny'
        },
        'feelslike_c': 24.6,
        'feelslike_f': 76.2,
        'humidity': 36,
        'last_updated': '2015-06-29 13:30',
        'last_updated_epoch': 1435584602,
        'precip_in': 0.0,
        'precip_mm': 0.0,
        'pressure_in': 30.7,
        'pressure_mb': 1022.0,
        'temp_c': 24.0,
        'temp_f': 75.2,
        'wind_degree': 260,
        'wind_dir': 'W',
        'wind_kph': 19.1,
        'wind_mph': 11.9
    },
    'location': {
        'country': 'United Kingdom',
        'lat': 51.52,
        'localtime': '2015-06-29 13:50',
        'localtime_epoch': 1435585840,
        'lon': -0.11,
        'name': 'London',
        'region': 'City Of London, Greater London',
        'tz_id': 'Europe/London'
    }
}
"""
print current['current']['wind_degree']  # show wind degree
print current['current']['temp_c']  # show temprature in celsius
print current['location']['country']  # name of country
print current['location']['lat']  # latitude value
print current['location']['lat']  # longitude value

###########################
# forecast weather
###########################
forecast = client.getForecastWeather(q='07112', days=7)
# "forecast" is a dict with a structure like this:
'''
{
    'current': {
        ...
    },
    'location': {
        ...
    },
    'forecast': {
        'forecastday': [{
            'astro': {
                'moonrise': '06:07 PM',
                'moonset': '03:33 AM',
                'sunrise': '05:29 AM',
                'sunset': '08:32 PM'
            },
            'date': '2015-06-29',
            'date_epoch': 1435536000,
            'day': {
                'avgtemp_c': 21.7,
                'avgtemp_f': 71.1,
                'condition': {
                    'code': 1063,
                    'icon': 'http://www.apixu.com/static/weather/64x64/day/176.png',
                    'text': 'Patchy rain nearby'
                },
                'maxtemp_c': 27.6,
                'maxtemp_f': 81.7,
                'maxwind_kph': 25.2,
                'maxwind_mph': 15.7,
                'mintemp_c': 17.5,
                'mintemp_f': 63.5,
                'totalprecip_in': 0.01,
                'totalprecip_mm': 0.2
            },
            'hour': [{
                'cloud': 16,
                'condition': {
                    'code': 1000,
                    'icon': 'http://www.apixu.com/static/weather/64x64/night/113.png',
                    'text': 'Clear '
                },
                'dewpoint_c': 15.1,
                'dewpoint_f': 59.2,
                'feelslike_c': 18.4,
                'feelslike_f': 65.1,
                'heatindex_c': 18.4,
                'heatindex_f': 65.1,
                'humidity': 81,
                'precip_in': 0.0,
                'precip_mm': 0.0,
                'pressure_in': 30.2,
                'pressure_mb': 1007.0,
                'temp_c': 18.4,
                'temp_f': 65.1,
                'time': '2015-06-29 00:00',
                'time_epoch': 1435536000,
                'will_it_rain': 0,
                'will_it_snow': 0,
                'wind_degree': 255,
                'wind_dir': 'WSW',
                'wind_kph': 25.6,
                'wind_mph': 15.9,
                'windchill_c': 18.4,
                'windchill_f': 65.1
            }]
        }]
    },
}
'''

print forecast['forecast']['forecastday'][0]['date'] # get date of forecast
print forecast['forecast']['forecastday'][0]['astro']['moonrise'] # get moonrise time

```
