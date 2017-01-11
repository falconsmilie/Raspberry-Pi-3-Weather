class WeatherResponseConditions(object):
    """ Clouds, rain, snow and wind response data """

    def __init__(self):
        self._clouds = None
        self._rain = None
        self._snow = None
        self._wind_deg = None
        self._wind_speed = None

    def set_conditions(self, weather):

        if 'clouds' in weather:
            if 'all' in weather['clouds']:
                self._clouds = weather['clouds']['all']

        if 'rain' in weather:
            if '3h' in weather['rain']:
                self._rain = weather['rain']['3h']

        if 'snow' in weather:
            if '3h' in weather['snow']:
                self._snow = weather['snow']['3h']

        if 'wind' in weather:
            if 'deg' in weather['wind']:
                self._wind_deg = weather['wind']['deg']

        if 'wind' in weather:
            if 'speed' in weather['wind']:
                self._wind_speed = weather['wind']['speed']

    @property
    def clouds(self):
        return self._clouds

    @clouds.setter
    def clouds(self, clouds):
        self._clouds = clouds
        return None

    @property
    def rain(self):
        return self._rain

    @rain.setter
    def rain(self, rain):
        self._rain = rain
        return None

    @property
    def snow(self):
        return self._snow

    @snow.setter
    def snow(self, snow):
        self._snow = snow
        return None

    @property
    def wind_deg(self):
        return self._wind_deg

    @wind_deg.setter
    def wind_deg(self, wind_deg):
        self._wind_deg = wind_deg
        return None

    @property
    def wind_speed(self):
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, wind_speed):
        self._wind_speed = wind_speed
        return None
