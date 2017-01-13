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
    weather_config.set()
    wconfig = weather_config.get()
    location = wconfig['location']
    request_type = wconfig['request_type']

    # Caching
    weather_cache = WeatherCache()
    weather_cache.clean()
    weather = weather_cache.check(location, request_type)

    if weather is None:
        # Request weather from Server
        weather_request = WeatherRequest()
        weather_request.set(wconfig)
        weather = weather_request.get()
        # Cache response
        weather_cache.set(weather, location, request_type)

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
    #print(response.city_name)
    #for w_list in weatherlist:
        #print(w_list.temp_min)
        #print(w_list.temp_max)
        #print(w_list.clouds)
        #print(w_list.snow)
        #print(w_list.rain)
        #print()

    # Test weather response
    conditions = weatherlist.get_conditions()
    print(response.city_name)
    print(weatherlist.temp)
    print(conditions.clouds)
    print(conditions.rain)
    print(conditions.snow)
    print()

except Exception as e:
    print(e)
