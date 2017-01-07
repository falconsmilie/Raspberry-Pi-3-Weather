class WeatherResponseConditions(object):

    def __init__(self):
        """ Members of this class """
        self.__clouds = None
        self.__rain = None
        self.__snow = None
        self.__wind = None

    def set_conditions(self, weather):
        """ A set of weather conditions common to each response """
        self.set_clouds(weather)
        self.set_rain(weather)
        self.set_snow(weather)
        self.set_wind(weather)

    def set_clouds(self, weather):
        if 'clouds' in weather:
            if 'all' in weather['clouds']:
                self.__clouds = weather['clouds']['all']
        return None

    def get_clouds(self):
        return self.__clouds

    def set_rain(self, weather):
        if 'rain' in weather:
            if '3h' in weather['rain']:
                self.__rain = weather['rain']['3h']
        return None

    def get_rain(self):
        return self.__rain

    def set_snow(self, weather):
        if 'snow' in weather:
            if '3h' in weather['snow']:
                self.__snow = weather['snow']['3h']
        return None

    def get_snow(self):
        return self.__snow

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
