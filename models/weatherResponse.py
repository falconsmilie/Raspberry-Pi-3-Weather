from models.weatherResponseWeather import *
from models.weatherResponseForecast5 import *
from models.weatherResponseForecast16 import *


class WeatherResponse(object):

    def set_response(self, weather, request):
        """ Determine what kind of response to return """

        if request == 'weather':
            response = WeatherResponseWeather()

        elif request == 'forecast5':
            response = WeatherResponseForecast5()

        elif request == 'forecast16':
            response = WeatherResponseForecast16()

        response.set_response(weather)

        return response
