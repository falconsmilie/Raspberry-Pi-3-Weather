# coding=utf-8
from nose.tools import *
from models.weatherConfig import *

config = {'api_key': '', 'location': '2925533'}

weather_config = WeatherConfig()

def test_set_config():
    """ Test setting the config """
    
    assert_equal(weather_config.set_config(), None)

def test_get_config_all():
    """ Test getting the config """

    assert_equal(weather_config.get_config_all(), config)
