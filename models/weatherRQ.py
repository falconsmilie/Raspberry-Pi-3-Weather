from requests import get


class WeatherRQ(object):

    def __init__(self):
        """ Construct sets members required for processing request. """
        self._endpoint = 'http://api.openweathermap.org/data/2.5/'
        self._request_timeout = 10
        self._request_type = None
        self._location = None
        self._api_key = None
        self._units = None
        self._lang = None
        self._forecast_count = None

    def set(self, params):
        """ Set local configuration values """
        try:
            # Standard vars for every request type
            self.set_request_type(params['request_type'])
            self.set_location(params['location'])
            self.set_api_key(params['api_key'])
            self.set_units(params['units'])
            self.set_lang(params['lang'])
            self.determine_forecast_count(params)
        except KeyError as e:
            raise Exception('Invalid Config key: ' + '{}'.format(e))

        return None

    def set_request_type(self, request_type):
        """ The type of request the user wants """
        self._request_type = request_type
        return None

    def set_location(self, location):
        """ Set the location we want to query """
        self._location = '{}'.format(location)
        return None

    def set_api_key(self, api_key):
        """ Set the users API key for accessing OpenWeatherMaps """
        self._api_key = api_key
        return None

    def set_units(self, units):
        """ Set the unit weather is returned in """
        self._units = units
        return None

    def set_lang(self, lang):
        """ Set the Langauge Description is returned in """
        self._lang = lang
        return None

    def determine_forecast_count(self, params):
        """ Count is specific to forecast5 and forecast16 requests """
        if (self._request_type == 'forecast16' or
                self._request_type == 'forecast5'):

            if self._request_type == 'forecast5':
                count = params['forecast_count_5']
            else:
                count = params['forecast_count_16']

            self.set_forecast_count(count)

        return None

    def set_forecast_count(self, count):
        """ Set the day count for forecast 5 and 16 requests """
        self._forecast_count = count
        return None

    def get(self):
        """ Send the request """
        payload = {
            'id': self._location,
            'units': self._units,
            'lang': self._lang,
            'APPID': self._api_key
        }

        # Two types of 'forecast' requests are available. They both have
        # different endpoints and allow for a 'count' parameter.
        if (self._request_type == 'forecast5' or
                self._request_type == 'forecast16'):

            payload['cnt'] = self._forecast_count

            if self._request_type == 'forecast5':
                self.set_request_type('forecast')
            else:
                self.set_request_type('forecast/daily')
        try:
            response = get(
                self._endpoint + self._request_type,
                params=payload,
                timeout=self._request_timeout
            ).json()
        except ValueError as e:
            raise Exception(e)

        return self.validate(response)

    def validate(self, response):
        """ Validate the response"""
        if self._request_type == 'weather':
            response = self.validate_weather(response)

        elif self._request_type == 'forecast':
            response = self.validate_forecast(response)

        elif self._request_type == 'forecast/daily':
            response = self.validate_forecast(response)

        return response

    def validate_weather(self, response):
        """ Validates the 'weather' type response """
        try:
            # There has been an error returned from the server
            if response['message']:
                raise Exception('Request Error: ' + response['message'])

        except KeyError:
            return response

    def validate_forecast(self, response):
        """ API returns a 'message' att for success and fail :S """

        # There has been an error returned from the server
        if response['message'] and isinstance(response['message'], str):
            raise Exception('Request Error: ' + response['message'])

        return response
