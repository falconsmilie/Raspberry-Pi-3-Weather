from models.weatherCache import *
from models.weatherConfig import *
from models.weatherRequest import *

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

    location = wconfig['location']
    
    # Caching
    weather_cache = WeatherCache()
    weather_cache.clean_cache()
    print('WeatherCache: Cache cleaned')
    
    weather = weather_cache.check_cache(location)

    if weather == None:
        weather_request = WeatherRequest()
        weather_request.set_params(wconfig)
        weather = weather_request.get_weather()
        
        weather_cache.set_cache(weather, location)

    print(weather)
    
except Exception as e:
    print(str(e))
