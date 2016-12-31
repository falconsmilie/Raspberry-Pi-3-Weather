import sys
from weatherCache import *
from weatherConfig import *
from weatherRequest import *

# Testing Controller
try:
    print('Starting ... ')
    
    # Config
    weather_config = WeatherConfig()
    print('WeatherConfig: Instantiated')
    
    weather_config.set_config()
    print('WeatherConfig: Config Set')
    
    wconfig = weather_config.get_config_all()
    print('WeatherConfig: Got Config')

    if wconfig == None:
        raise Exception('No config can be found.')

    # Caching
    open_weather_cache = WeatherCache()
    weather = open_weather_cache.check_cache(wconfig['location'])

    if weather == None:
        weather_request = WeatherRequest()
        weather_request.set_params(wconfig)
        weather = weather_request.get_weather()

    print(weather)
    
except Exception as e:
    print(str(e))
