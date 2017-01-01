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

    if wconfig is None:
        raise Exception('No config can be found.')

    location = wconfig['location']

    # Caching
    weather_cache = WeatherCache()
    weather_cache.clean_cache()
    print('WeatherCache: Cache cleaned')

    # Get Weather
    weather = weather_cache.check_cache(location)

    if weather is None:
        weather_request = WeatherRequest()
        weather_request.set_params(wconfig)
        weather = weather_request.get_weather()
        print('WeatherRequest: Request Weather')

        weather_cache.set_cache(weather, location)
        print('WeatherCache: Cached Weather')

    print(weather)

except Exception as e:
    print(str(e))
