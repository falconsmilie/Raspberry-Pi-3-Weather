from models.weatherResponse import *


class WeatherResponseForecast16(WeatherResponse):


    def __init__(self):

        super(WeatherResponse, self).__init__()

        """ Members of the 'forecast16' response """
        self.__weather_list = {}

    def set_response(self, weather):
        """ Sets response variables to local members """

        print(weather)
        exit()

        try:
            json_util = WeatherJson()
            weather = json_util.fix_json_string(weather)

            # Base Members
            self.set_city_name(weather['city']['name'])
            self.set_city_id(weather['city']['id'])
            self.set_country(weather['city']['country'])
            self.set_coord_lat(weather['city']['coord']['lat'])
            self.set_coord_lon(weather['city']['coord']['lon'])

            # TODO: Add other members

        except KeyError as e:
            raise Exception('Invalid Response Key: ' + '{}'.format(e))

        return None
