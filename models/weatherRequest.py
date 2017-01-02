from requests import get


class WeatherRequest(object):

    def __init__(self):
        """ Construct sets members required for processing request. """

        self.__endpoint = 'http://api.openweathermap.org/data/2.5/'
        self.__request_timeout = 10
        self.__request_type = None
        self.__location = None
        self.__api_key = None
        self.__units = None
        self.__lang = None
        self.__forecast_count = None

    def set_params(self, params):
        """ Set local configuration values """

        try:
            self.set_request_type(params['request_type'])
            self.set_location(params['location'])
            self.set_api_key(params['api_key'])
            self.set_units(params['units'])
            self.set_lang(params['lang'])

            if (self.__request_type == 'forecast16' or
                self.__request_type == 'forecast5'):
                # Count is specific to forecast5 and forecast16
                self.set_forecast_count(params['forecast_count'])

        except KeyError as e:
            raise Exception('Invalid Config key: ' + '{}'.format(e))

        return None

    def set_request_type(self, request_type):
        """ The type of request the user wants """
        self.__request_type = request_type
        return None

    def set_location(self, location):
        """ Set the location we want to query """
        self.__location = '{}'.format(location)
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

    def set_forecast_count(self, count):
        """ Set the day count for forecast 16 request """
        self.__forecast_count = count
        return None

    def get_weather(self):
        """ Send the request """

        payload = {
            'id': self.__location,
            'units': self.__units,
            'lang': self.__lang,
            'APPID': self.__api_key
        }

        # Two types of 'forecast' requests are available
        if (self.__request_type == 'forecast5' or
            self.__request_type == 'forecast16'):
            # Both forecasts except a count value
            payload['cnt'] = self.__forecast_count

            if self.__request_type == 'forecast5':
                self.set_request_type('forecast')

            elif self.__request_type == 'forecast16':
                self.set_request_type('forecast/daily')

        try:
            response = get(
                self.__endpoint + self.__request_type,
                params=payload,
                timeout=self.__request_timeout
            ).json()

        except ValueError as e:
            raise Exception(e)

        return self.validate_response(response)

    def validate_response(self, response):
        """ Validate the response"""

        if self.__request_type == 'weather':
            response = self.validate_response_weather(response)

        elif self.__request_type == 'forecast':
            response = self.validate_response_forecast(response)

        elif self.__request_type == 'forecast/daily':
            response = self.validate_response_forecast(response)

        return response

    def validate_response_weather(self, response):
        """ Validates the 'weather' type response """
        try:
            # There has been an error returned from the server
            if response['message']:
                raise Exception('Request Error: ' + response['message'])

        except KeyError as e:
            return response

    def validate_response_forecast(self, response):
        """ API returns a 'message' att for success and fail :S """

        # There has been an error returned from the server
        if response['message'] and type(response['message']) == 'str':
            raise Exception('Request Error: ' + response['message'])

        return response
