from models.weatherCache import WeatherCache
from models.weatherConfig import WeatherConfig
from models.weatherRequest import WeatherRequest
from models.weatherResponse import (
    WeatherResponse, WeatherResponseWeather,
    WeatherResponseForecast5, WeatherResponseForecast16
)

# Testing Controller
try:
    # Config
    weather_config = WeatherConfig()
    weather_config.set_config()
    wconfig = weather_config.get_config_all()
    location = wconfig['location']
    request_type = wconfig['request_type']

    # Caching
    weather_cache = WeatherCache()
    weather_cache.clean_cache()
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

    weatherlist = response.get_weather_list()

    # Test forecast 5 response
    #print(response.city_name)
    #for w_list in weatherlist:
        #print(w_list.temp)
        #print(w_list.get_conditions().wind_speed)

    # Test forecast 16 response
    print(response.city_name)
    for w_list in weatherlist:
        print(w_list.temp_min)
        print(w_list.temp_max)

    # Test weather response
    #print(response.city_name)
    #print(weatherlist.temp)
    #print(weatherlist.get_conditions().wind_speed)

except Exception as e:
    print(e)
