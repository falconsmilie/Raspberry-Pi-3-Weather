from requests import get


class WeatherRequest(object):


    def __init__(self):
        """ Construct sets members required for processing request. """
        
        self.__location = None
        self.__api_key = None
        self.__endpoint = 'http://api.openweathermap.org/data/2.5/weather'


    def set_params(self, params):
        """ Set local configuration values """
        
        try:
            self.set_location(params['location'])
            self.set_api_key(params['api_key'])
        
        except KeyError as e:
            raise Exception(repr('Not a valid config key: ' + str(e)))

        
    def set_location(self, location):
        """ Set the location we want to query """
        
        self.__location = location


    def set_api_key(self, api_key):
        """ Set the client's API key for accessing OpenWeatherMaps """
        
        self.__api_key = api_key


    def get_weather(self):
        """ Send the request """
        
        payload = {
            'id': self.__location,
            'APPID': self.__api_key
        }

        return get(self.__endpoint, params=payload).json()
