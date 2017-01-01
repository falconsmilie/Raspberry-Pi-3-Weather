from requests import get


class WeatherRequest(object):

    def __init__(self):
        """ Construct sets members required for processing request. """

        self.__endpoint_base_url = 'http://api.openweathermap.org/data/2.5/'
        #self.__endpoint_weather = 'weather'
        #self.__endpoint_5_day_forecast = 'forecast'
        
        self.__request_type = None
        self.__location = None
        self.__api_key = None
        self.__units = None
        self.__lang = None

    def set_params(self, params):
        """ Set local configuration values """

        try:
            self.set_request_type(params['request_type'])
            self.set_location(params['location'])
            self.set_api_key(params['api_key'])
            self.set_units(params['units'])
            self.set_lang(params['lang'])

        except KeyError as e:
            raise Exception(repr('Not a valid config key: ' + str(e)))

        return None

    def set_request_type(self, request_type):
        """ The type of request the user wants """
        self.__request_type = request_type
        return None

    def set_location(self, location):
        """ Set the location we want to query """
        self.__location = location
        return None

    def set_api_key(self, api_key):
        """ Set the client's API key for accessing OpenWeatherMaps """
        self.__api_key = api_key
        return None

    def set_units(self, units):
        """ Set the unit weather is returned in """
        self.__units = units
        return None

    def set_lang(self, lang):
        """ Set the Langauge Description is returned in """
        self.__lang = lang
        return None

    def get_weather(self):
        """ Send the request """

        payload = {
            'id': self.__location,
            'units': self.__units,
            'lang': self.__lang,
            'APPID': self.__api_key
        }

        response = get(
            self.__endpoint_base_url + self.__request_type,
            params=payload
        ).json()

        try:
            # There has been an error returned from the server
            if response['message']:
                raise Exception(
                    'Request Error: ' + response['message']
                )

        except KeyError as e:
            # The response is OK
            return response
