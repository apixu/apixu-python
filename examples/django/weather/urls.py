from django.urls import path
from .views import CurrentWeatherView
import os
from apixu.client import ApixuClient

api_key = os.environ['APIXUKEY']
client = ApixuClient(api_key)

urlpatterns = [
    path('weather', CurrentWeatherView.as_view(apixu=client), name="current-weather")
]
