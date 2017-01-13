# coding=utf-8
from nose.tools import assert_equal
from models.weatherCache import WeatherCache

# Test data
location = 2925533

weather_data = """{'weather': [{'description': 'mist', 'icon': '50d',
'main': 'Mist', 'id': 701}, {'description': 'fog', 'icon': '50d',
'main': 'Fog', 'id': 741}], 'dt': 1483280400, 'clouds': {'all': 90},
'coord': {'lat': 50.12, 'lon': 8.68}, 'sys': {'sunset': 1483284862,
'sunrise': 1483255456, 'country': 'DE', 'type': 1, 'id': 4881,
'message': 0.0042}, 'base': 'stations', 'wind': {'speed': 1.5,
'deg': 210}, 'main': {'temp': 270.5, 'temp_min': 270.15,
'humidity': 100, 'temp_max': 271.15, 'pressure': 1020}, 'id': 2925533,
'name': 'Frankfurt am Main', 'cod': 200, 'visibility': 4500}"""

weather_cache = WeatherCache()


def test_set_cache():
    """" Test setting the cache. Required for all other Cache tests """

    assert_equal(
        weather_cache.set_cache(weather_data, location, 'weather'),
        None
    )


def test_check_cache():
    """ Test reading the cache """

    assert_equal(
        weather_cache.check_cache(location, 'weather'),
        weather_data
    )
    assert_equal(
        weather_cache.check_cache(str(location) + 'fail', 'weather'),
        None
    )


def test_clean_cache():
    """ Clean the cache """

    assert_equal(weather_cache.clean_cache(1), None)
