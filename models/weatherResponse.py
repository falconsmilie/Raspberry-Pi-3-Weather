from models.weatherResponseListItem import WeatherResponseListItem
from models.weatherResponseListItemForecast16 import (
    WeatherResponseListItemForecast16
)
from utils.weatherJson import WeatherJson


class WeatherResponse(object):
    """ Reads a server response, or cached file, weather data """

    def __init__(self):
        """ Members available to each extending response type """
        self._city_name = None
        self._city_id = None
        self._country = None
        self._coord_lat = None
        self._coord_lon = None

    def fix_json_string(self, weather_string):
        json_utils = WeatherJson()
        return json_utils.fix_json_string(weather_string)

    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, name):
        self._city_name = name
        return None

    @property
    def city_id(self):
        return self._city_id

    @city_id.setter
    def city_id(self, city_id):
        self._city_id = city_id
        return None

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        """ Country code (GB, JP etc.) """
        self._country = country
        return None

    @property
    def coord_lat(self):
        return self._coord_lat

    @coord_lat.setter
    def coord_lat(self, coord_lat):
        self._coord_lat = coord_lat
        return None

    @property
    def coord_lon(self):
        return self._coord_lon

    @coord_lon.setter
    def coord_lon(self, coord_lon):
        self._coord_lon = coord_lon
        return None


class WeatherResponseWeather(WeatherResponse):
    """ Handles the 'weather' type response """

    def __init__(self):
        """ Members of the 'weather' type response """
        self._response_list_item = None
        self._sunrise = None
        self._sunset = None
        self._weather_desc_main = None
        self._weather_desc = None
        self._weather_icon_id = None
        self._time_of_weather = None
        self._weather_list = None

    def set_response(self, weather):
        """ Sets response variables to local members """
        try:
            weather = self.fix_json_string(weather)

            # Base members
            super(WeatherResponseWeather, self.__class__). \
                city_name.fset(self, weather['name'])
            super(WeatherResponseWeather, self.__class__). \
                city_id.fset(self, weather['id'])
            super(WeatherResponseWeather, self.__class__). \
                country.fset(self, weather['sys']['country'])
            super(WeatherResponseWeather, self.__class__). \
                coord_lat.fset(self, weather['coord']['lat'])
            super(WeatherResponseWeather, self.__class__). \
                coord_lon.fset(self, weather['coord']['lon'])

            # 'Weather' response type members
            self._sunrise = weather['sys']['sunrise']
            self._sunset = weather['sys']['sunset']
            self._weather_desc_main = weather['weather'][0]['main']
            self._weather_desc = weather['weather'][0]['description']
            self._weather_icon_id = weather['weather'][0]['icon']
            self._time_of_weather = weather['dt']

            # weatherResponseList object
            self.set_weather_list(weather)

        except KeyError as e:
            raise Exception('Invalid Response Key: ' + '{}'.format(e))

        return None

    @property
    def sunrise(self):
        return self._sunrise

    @sunrise.setter
    def sunrise(self, sunrise):
        """ Sunrise time, unix, UTC """
        self._sunrise = sunrise
        return None

    @property
    def sunset(self):
        return self._sunset

    @sunset.setter
    def sunset(self, sunset):
        """ sunset time, unix, UTC """
        self._sunset = sunset
        return None

    @property
    def weather_desc_main(self):
        return self._weather_desc_main

    @weather_desc_main.setter
    def weather_desc_main(self, weather_desc_main):
        self._weather_desc_main = weather_desc_main
        return None

    @property
    def weather_desc(self):
        return self._weather_desc

    @weather_desc.setter
    def weather_desc(self, weather_desc):
        self._weather_desc = weather_desc
        return None

    @property
    def weather_icon_id(self):
        return self._weather_icon_id

    @weather_icon_id.setter
    def weather_icon_id(self, weather_icon_id):
        self._weather_icon_id = weather_icon_id
        return None

    @property
    def time_of_weather(self):
        return self._time_of_weather

    @time_of_weather.setter
    def time_of_weather(self, time_of_weather):
        """ Time of data calculation, unix, UTC """
        self._time_of_weather = time_of_weather
        return None

    def get_weather_list(self):
        return self._weather_list

    def set_weather_list(self, weather):
        list_response = WeatherResponseListItem()
        list_response.set_response(weather)
        self._weather_list = list_response
        return None


class WeatherResponseForecast5(WeatherResponse):
    """ Handles response for 5 day forecast """

    def __init__(self):
        """ Members of the 'forecast5' response """
        self._list_count = None
        self._weather_list = []

    def set_response(self, weather):
        """ Sets response variables to local members """

        try:
            weather = self.fix_json_string(weather)

            # Base Members
            super(WeatherResponseForecast5, self.__class__). \
                city_name.fset(self, weather['city']['name'])
            super(WeatherResponseForecast5, self.__class__). \
                city_id.fset(self, weather['city']['id'])
            super(WeatherResponseForecast5, self.__class__). \
                country.fset(self, weather['city']['country'])
            super(WeatherResponseForecast5, self.__class__). \
                coord_lat.fset(self, weather['city']['coord']['lat'])
            super(WeatherResponseForecast5, self.__class__). \
                coord_lon.fset(self, weather['city']['coord']['lon'])

            # Forecast5 members
            self._list_count = weather['cnt']
            self.set_weather_list(weather)

        except KeyError as e:
            raise Exception('Invalid Response Key: ' + '{}'.format(e))

        return None

    @property
    def list_count(self):
        return self._weather_list_count

    @list_count.setter
    def list_count(self, count):
        self._weather_list_count = count
        return None

    def get_weather_list(self):
        return self._weather_list

    def set_weather_list(self, weather):
        for list_item in weather['list']:
            list_response = WeatherResponseListItem()
            list_response.set_response(list_item)
            self._weather_list.append(list_response)
        return None


class WeatherResponseForecast16(WeatherResponse):
    """ Handles response for 16 day forecast """

    def __init__(self):
        """ Members of the 'forecast16' response """
        self._list_count = None
        self._weather_list = []

    def set_response(self, weather):
        """ Sets response variables to local members """

        try:
            weather = self.fix_json_string(weather)

            # Base Members
            super(WeatherResponseForecast16, self.__class__). \
                city_name.fset(self, weather['city']['name'])
            super(WeatherResponseForecast16, self.__class__). \
                city_id.fset(self, weather['city']['id'])
            super(WeatherResponseForecast16, self.__class__). \
                country.fset(self, weather['city']['country'])
            super(WeatherResponseForecast16, self.__class__). \
                coord_lat.fset(self, weather['city']['coord']['lat'])
            super(WeatherResponseForecast16, self.__class__). \
                coord_lon.fset(self, weather['city']['coord']['lon'])

            # Local members
            self.list_count = weather['cnt']
            self.set_weather_list(weather['list'])

        except KeyError as e:
            raise Exception('Invalid Response Key: ' + '{}'.format(e))

        return None

    @property
    def list_count(self):
        return self._weather_list_count

    @list_count.setter
    def list_count(self, count):
        self._weather_list_count = count
        return None

    def get_weather_list(self):
        return self._weather_list

    def set_weather_list(self, weather):
        for list_item in weather:
            list_response = WeatherResponseListItemForecast16()
            list_response.set_response(list_item)
            self._weather_list.append(list_response)
        return None
