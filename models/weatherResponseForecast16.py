from models.weatherResponse import *


class WeatherResponseForecast16(WeatherResponse):


    def __init__(self):

        super(WeatherResponse, self).__init__()

        """ Members of the 'forecast16' response """
        self.__weather_list = {}

    def set_response(self, weather):
        """ Sets response variables to local members """

        try:
            json_util = WeatherJson()
            weather = json_util.fix_json_string(weather)

            self.set_city_name(weather['name'])

            # TODO: Add other members

        except KeyError as e:
            raise Exception('Invalid Response Key: ' + '{}'.format(e))

        return None
