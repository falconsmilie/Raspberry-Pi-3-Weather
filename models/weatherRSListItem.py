from models.weatherRSConditions import WeatherRSConditions


class WeatherRSListItem(object):

    def __init__(self):
        """ Members of List """
        self._temp = None
        self._temp_min = None
        self._temp_max = None
        self._humidity = None
        self._wind_speed = None
        self._wind_deg = None
        self._pressure = None
        self._pressure_sea_level = None
        self._pressure_ground_level = None
        self._conditions = None

    def set_response(self, weather):
        """ Sets response variables to local members """
        try:
            self._temp = weather['main']['temp']
            self._temp_min = weather['main']['temp_min']
            self._temp_max = weather['main']['temp_max']
            self._humidity = weather['main']['humidity']
            self._pressure = weather['main']
            self._pressure_sea_level = weather['main']
            self._pressure_ground_level = weather['main']

            # weatherResponseConditions object
            self.set_conditions(weather)

        except KeyError as e:
            raise Exception('Invalid Response Key: ' + '{}'.format(e))

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, temp):
        """ Temperature. Unit Default: Kelvin,
        User defined options: Metric: Celsius, Imperial: Fahrenheit.
        """
        self._temp = temp
        return None

    @property
    def temp_min(self):
        return self._temp_min

    @temp_min.setter
    def temp_min(self, temp_min):
        """ Minimum temperature at the moment. This is deviation from
        current temp that is possible for large cities.
        """
        self._temp_min = temp_min
        return None

    @property
    def temp_max(self):
        return self._temp_max

    @temp_max.setter
    def temp_max(self, temp_max):
        """ Minimum temperature at the moment. This is deviation from
        current temp that is possible for large cities.
        """
        self._temp_max = temp_max
        return None

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, humidity):
        self._humidity = humidity
        return None

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, weather_main):
        if 'pressure' in weather_main:
            self._pressure = weather_main['pressure']
        return None

    @property
    def pressure_sea_level(self):
        return self._pressure_sea_level

    @pressure_sea_level.setter
    def pressure_sea_level(self, weather_main):
        if 'sea_level' in weather_main:
            self._pressure_sea_level = weather_main['sea_level']
        return None

    @property
    def pressure_ground_level(self):
        return self._pressure_ground_level

    @pressure_ground_level.setter
    def pressure_ground_level(self, weather_main):
        if 'grnd_level' in weather_main:
            self._pressure_ground_level = weather_main['grnd_level']
        return None

    def get_conditions(self):
        return self._conditions

    def set_conditions(self, weather):
        condition_response = WeatherRSConditions()
        condition_response.set_conditions(weather)
        self._conditions = condition_response
        return None
