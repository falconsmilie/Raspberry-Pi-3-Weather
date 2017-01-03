from models.weatherCache import *
from models.weatherConfig import *
from models.weatherRequest import *
from models.weatherResponse import *

# Testing Controller
try:
    # Config
    weather_config = WeatherConfig()
    weather_config.set_config()
    wconfig = weather_config.get_config_all()

    if wconfig is None:
        raise Exception('No config can be found.')

    location = wconfig['location']
    request_type = wconfig['request_type']

    # Caching
    weather_cache = WeatherCache()
    weather_cache.clean_cache()

    # Get Weather from Cache
    weather = weather_cache.check_cache(location, request_type)

    if weather is None:
        # Request weather from Server
        weather_request = WeatherRequest()
        weather_request.set_params(wconfig)
        weather = weather_request.get_weather()
        # Cache response
        weather_cache.set_cache(weather, location, request_type)

    # Package up Response
    weather_response = WeatherResponse()
    weather_response.set_response(weather, request_type)

    print(weather)

except Exception as e:
    print(e)
