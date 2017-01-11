class WeatherResponseConditions(object):
    """ Clouds, rain, snow and wind response data """

    def __init__(self):
        self._clouds = None
        self._rain = None
        self._snow = None
        self._wind_deg = None
        self._wind_speed = None

    def set_conditions(self, weather):
        self._clouds = weather
        self._rain = weather
        self._snow = weather
        self._wind_deg = weather
        self._wind_speed = weather

    @property
    def clouds(self):
        return self._clouds

    @clouds.setter
    def clouds(self, weather):
        if 'clouds' in weather:
            if 'all' in weather['clouds']:
                self._clouds = weather['clouds']['all']
        return None

    @property
    def rain(self):
        return self._rain

    @rain.setter
    def rain(self, weather):
        if 'rain' in weather:
            if '3h' in weather['rain']:
                self._rain = weather['rain']['3h']
        return None

    @property
    def snow(self):
        return self._snow

    @snow.setter
    def snow(self, weather):
        if 'snow' in weather:
            if '3h' in weather['snow']:
                self._snow = weather['snow']['3h']
        return None

    @property
    def wind_deg(self):
        return self._wind_deg

    @wind_deg.setter
    def wind_deg(self, weather):
        if 'wind' in weather:
            if 'deg' in weather['wind']:
                self._wind_deg = weather['wind']['deg']
        return None

    @property
    def wind_speed(self):
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, weather):
        if 'wind' in weather:
            if 'speed' in weather['wind']:
                self._wind_speed = weather['wind']['speed']
        return None
