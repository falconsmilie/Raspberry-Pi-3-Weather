from models.weatherResponseConditions import *


class WeatherResponseListItem(object):

    def __init__(self):
        """ Members of List """
        self.__temp = None
        self.__temp_min = None
        self.__temp_max = None
        self.__humidity = None
        self.__wind_speed = None
        self.__wind_deg = None
        self.__pressure = None
        self.__pressure_sea_level = None
        self.__pressure_ground_level = None
        self.__conditions = None

    def set_response(self, weather):
        """ Sets response variables to local members """
        try:
            self.set_temp(weather['main']['temp'])
            self.set_temp_min(weather['main']['temp_min'])
            self.set_temp_max(weather['main']['temp_max'])
            self.set_humidity(weather['main']['humidity'])
            self.set_pressures(weather['main'])

            # weatherResponseConditions object
            self.set_conditions(weather)

        except KeyError as e:
            raise Exception('Invalid Response Key: ' + '{}'.format(e))

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

    def set_pressures(self, weather_main):
        """ Atmospheric pressure (on sea level, if no
        sea_level or grnd_level data), hPa
        """
        if 'pressure' in weather_main:
            self.__pressure = weather_main['pressure']

        if 'sea_level' in weather_main:
            self.__pressure_sea_level = weather_main['sea_level']

        if 'grnd_level' in weather_main:
            self.__pressure_ground_level = weather_main['grnd_level']

        return None

    def get_pressure(self):
        return self.__pressure

    def get_pressure_sea_level(self):
        return self.__pressure_sea_level

    def get_pressure_ground_level(self):
        return self.__pressure_ground_level

    def set_conditions(self, weather):
        condition_response = WeatherResponseConditions()
        condition_response.set_conditions(weather)
        self.__conditions = condition_response
        return None

    def get_conditions(self):
        return self.__conditions
