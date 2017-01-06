class WeatherResponseList(object):

    def __init__(self):
        """ Members of List """
        self.__pressure = None
        self.__temp = None
        self.__temp_min = None
        self.__temp_max = None
        self.__humidity = None
        self.__wind_speed = None
        self.__wind_deg = None

    def set_response(self, weather):
        """ Sets response variables to local members """
        try:
            self.set_pressure(weather['main']['pressure'])
            self.set_temp(weather['main']['temp'])
            self.set_temp_min(weather['main']['temp_min'])
            self.set_temp_max(weather['main']['temp_max'])
            self.set_humidity(weather['main']['humidity'])
            self.set_wind(weather)

        except KeyError as e:
            raise Exception('Invalid Response Key: ' + '{}'.format(e))

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

    def set_wind(self, weather):

        if 'wind' in weather:

            if 'deg' in weather['wind']:
                self.set_wind_deg(weather['wind']['deg'])

            if 'speed' in weather['wind']:
                self.set_wind_speed(weather['wind']['speed'])

    def set_wind_deg(self, wind_deg):
        self.__wind_deg = wind_deg
        return None

    def get_wind_deg(self):
        return self.__wind_deg

    def set_wind_speed(self, wind_speed):
        self.__wind_speed = wind_speed
        return None

    def get_wind_speed(self):
        return self.__wind_speed
