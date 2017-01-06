from models.weatherCache import *
from models.weatherConfig import *
from models.weatherRequest import *
from models.weatherResponseWeather import *
from models.weatherResponseForecast5 import *
from models.weatherResponseForecast16 import *

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
    if request_type == 'weather':
        response = WeatherResponseWeather()

    elif request_type == 'forecast5':
        response = WeatherResponseForecast5()

    elif request_type == 'forecast16':
        response = WeatherResponseForecast16()

    response.set_response(weather)

    weatherlist = response.get_list()

    # Test forecast
    #for w_list in weatherlist:
        #print(w_list.get_temp())

    # Test weather list
    print(weatherlist.get_temp())

except Exception as e:
    print(e)
