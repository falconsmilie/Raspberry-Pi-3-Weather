# coding=utf-8
from nose.tools import *
from models.weatherRequest import *

config = {
    "api_key": "",
    "location": "2925533",
    "request_type": "forecast5",
    "forecast_count_5": 5,
    "forecast_count_16": 16,
    "units": "metric",
    "lang": "en"
}

weather_data = "{'weather': [{'description': 'mist', 'icon': '50d', 'main': 'Mist', 'id': 701}, {'description': 'fog', 'icon': '50d', 'main': 'Fog', 'id': 741}], 'dt': 1483280400, 'clouds': {'all': 90}, 'coord': {'lat': 50.12, 'lon': 8.68}, 'sys': {'sunset': 1483284862, 'sunrise': 1483255456, 'country': 'DE', 'type': 1, 'id': 4881, 'message': 0.0042}, 'base': 'stations', 'wind': {'speed': 1.5, 'deg': 210}, 'main': {'temp': 270.5, 'temp_min': 270.15, 'humidity': 100, 'temp_max': 271.15, 'pressure': 1020}, 'id': 2925533, 'name': 'Frankfurt am Main', 'cod': 200, 'visibility': 4500}{'weather': [{'description': 'mist', 'icon': '50d', 'main': 'Mist', 'id': 701}, {'description': 'fog', 'icon': '50d', 'main': 'Fog', 'id': 741}], 'dt': 1483280400, 'clouds': {'all': 90}, 'coord': {'lat': 50.12, 'lon': 8.68}, 'sys': {'sunset': 1483284862, 'sunrise': 1483255456, 'country': 'DE', 'type': 1, 'id': 4881, 'message': 0.0042}, 'base': 'stations', 'wind': {'speed': 1.5, 'deg': 210}, 'main': {'temp': 270.5, 'temp_min': 270.15, 'humidity': 100, 'temp_max': 271.15, 'pressure': 1020}, 'id': 2925533, 'name': 'Frankfurt am Main', 'cod': 200, 'visibility': 4500}"

weather_request = WeatherRequest()

def test_set_params():
    """ Test setting params """

    assert_equal(weather_request.set_params(config), None)

def test_get_weather():
    """ Test the request to the server """

    assert_equal(weather_request.get_weather(), weather_data)
