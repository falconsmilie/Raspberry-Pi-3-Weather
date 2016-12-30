from requests import get

class WeatherRequest(object):

    def __init__(self):
        self.__location = None
        self.__api_key = None
        self.__endpoint = 'http://api.openweathermap.org/data/2.5/weather'


    def set_location(self, location):
        self.__location = location


    def set_api_key(self, api_key):
        self.__api_key = api_key


    def get_weather(self):
        
        url = self.__endpoint + '?id=' + self.__location + '&APPID=' + self.__api_key

        return get(url).json()
