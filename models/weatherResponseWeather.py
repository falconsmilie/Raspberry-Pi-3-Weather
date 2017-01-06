from models.weatherResponse import *
from models.weatherResponseList import *


class WeatherResponseWeather(WeatherResponse):

    def __init__(self):

        super(WeatherResponse, self).__init__()

        """ Members of the 'weather' type response """
        self.__sunrise = None
        self.__sunset = None
        self.__weather_desc_main = None
        self.__weather_desc = None
        self.__time_of_weather = None
        self.__pressure = None
        self.__weather_list = None

    def set_response(self, weather):
        """ Sets response variables to local members """
        try:
            json_util = WeatherJson()
            weather = json_util.fix_json_string(weather)

            # Base members
            self.set_city_name(weather['name'])
            self.set_city_id(weather['id'])
            self.set_country(weather['sys']['country'])
            self.set_coord_lat(weather['coord']['lat'])
            self.set_coord_lon(weather['coord']['lon'])

            # 'Weather' response type members
            self.set_sunrise(weather['sys']['sunrise'])
            self.set_sunset(weather['sys']['sunset'])
            self.set_weather_desc_main(weather['weather'][0]['main'])
            self.set_weather_desc(weather['weather'][0]['description'])
            self.set_time_of_weather(weather['dt'])

            # List of weather data
            list_response = WeatherResponseList()
            list_response.set_response(weather)
            self.__weather_list = list_response

        except KeyError as e:
            raise Exception('Invalid Response Key: ' + '{}'.format(e))

        return None

    def get_list(self):
        return self.__weather_list

    def set_sunrise(self, sunrise):
        """ Sunrise time, unix, UTC """
        self.__sunrise = sunrise
        return None

    def get_sunrise(self):
        return self.__sunrise

    def set_sunset(self, sunset):
        """ sunset time, unix, UTC """
        self.__sunset = sunset
        return None

    def get_sunset(self):
        return self.__sunset

    def set_weather_desc_main(self, weather_desc_main):
        self.__weather_desc_main = weather_desc_main
        return None

    def get_weather_desc_main(self):
        return self.__weather_desc_main

    def set_weather_desc(self, weather_desc):
        self.__weather_desc = weather_desc
        return None

    def get_weather_desc(self):
        return self.__weather_desc

    def set_time_of_weather(self, time_of_weather):
        """ Time of data calculation, unix, UTC """
        self.__time_of_weather = time_of_weather
        return None

    def get_time_of_weather(self):
        return self.__time_of_weather

    def set_pressure(self, pressure):
        """ Atmospheric pressure (on sea level, if no
        sea_level or grnd_level data), hPa
        """
        self.__pressure = pressure
        return None

    def get_pressure(self):
        return self.__pressure

    def set_temp(self, temp):
        """ Temperature. Unit Default: Kelvin,
        User defined options: Metric: Celsius, Imperial: Fahrenheit.
        """
        self.__temp = temp
        return None

    def get_temp(self):
        return self.__temp

    def set_temp_min(self, temp_min):
        """ Minimum temperature at the moment. This is deviation from
        current temp that is possible for large cities.
        """
        self.__temp_min = temp_min
        return None

    def get_temp_min(self):
        return self.__temp_min

    def set_temp_max(self, temp_max):
        """ Minimum temperature at the moment. This is deviation from
        current temp that is possible for large cities.
        """
        self.__temp_max = temp_max
        return None

    def get_temp_max(self):
        return self.__temp_max

    def set_humidity(self, humidity):
        self.__humidity = humidity
        return None

    def get_humidity(self):
        return self.__humidity

    def set_wind_speed(self, wind_speed):
        self.__wind_speed = wind_speed
        return None

    def get_wind_speed(self):
        return self.__wind_speed

    def set_wind_deg(self, wind_deg):
        self.__wind_deg = wind_deg
        return None

    def get_wind_deg(self):
        return self.__wind_deg
