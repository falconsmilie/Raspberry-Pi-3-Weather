from models.weatherResponse import *
from models.weatherResponseListItem import *


class WeatherResponseForecast5(WeatherResponse):

    def __init__(self):
        """ Members of the 'forecast5' response """

        super(WeatherResponse, self).__init__()

        self.__list_count = None
        self.__weather_list = []

    def set_response(self, weather):
        """ Sets response variables to local members """

        try:
            json_util = WeatherJson()
            weather = json_util.fix_json_string(weather)

            # Base Members
            self.set_city_name(weather['city']['name'])
            self.set_city_id(weather['city']['id'])
            self.set_country(weather['city']['country'])
            self.set_coord_lat(weather['city']['coord']['lat'])
            self.set_coord_lon(weather['city']['coord']['lon'])

            # Forecast5 members
            self.set_list_count(weather['cnt'])
            self.set_list(weather)

        except KeyError as e:
            raise Exception('Invalid Response Key: ' + '{}'.format(e))

        return None

    def set_list_count(self, count):
        self.__weather_list_count = count
        return None

    def get_list_count(self):
        return self.__weather_list_count

    def set_list(self, weather):

        for list_item in weather['list']:

            list_response = WeatherResponseListItem()
            list_response.set_response(list_item)

            self.__weather_list.append(list_response)

        return None

    def get_list(self):
        return self.__weather_list
