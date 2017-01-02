from models.weatherCache import *
from models.weatherConfig import *
from models.weatherRequest import *

# Testing Controller
try:
    # Config
    weather_config = WeatherConfig()
    weather_config.set_config()
    wconfig = weather_config.get_config_all()

    if wconfig is None:
        raise Exception('No config can be found.')

    location = wconfig['location']

    # Caching
    weather_cache = WeatherCache()
    weather_cache.clean_cache()

    # Get Weather
    weather = weather_cache.check_cache(
        location,
        wconfig['request_type']
    )

    if weather is None:
        weather_request = WeatherRequest()
        weather_request.set_params(wconfig)
        weather = weather_request.get_weather()

        weather_cache.set_cache(
            weather,
            location,
            wconfig['request_type']
        )
        

    print(weather)

except Exception as e:
    print(e)
