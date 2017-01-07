class WeatherResponseListItemForecast16(object):

    def __init__(self):
        """ Members of ListItem """
        self.__temp_min = None
        self.__temp_max = None
        self.__temp_morn = None
        self.__temp_day = None
        self.__temp_eve = None
        self.__temp_night = None
        self.__humidity = None
        self.__wind_speed = None
        self.__wind_deg = None
        self.__pressure = None
        self.__clouds = None
        self.__snow = None
        self.__rain = None
        self.__weather_description = None
        self.__weather_description_main = None
        self.__weather_icon = None
        self.__time_of_weather = None

    def set_response(self, weather):
        """ Sets response variables to local members """
        try:
            self.set_temp_min(weather['temp']['min'])
            self.set_temp_max(weather['temp']['max'])
            self.set_temp_morn(weather['temp']['morn'])
            self.set_temp_day(weather['temp']['day'])
            self.set_temp_eve(weather['temp']['eve'])
            self.set_temp_night(weather['temp']['night'])
            self.set_humidity(weather['humidity'])
            self.set_pressure(weather['pressure'])
            self.set_wind_speed(weather['speed'])
            self.set_wind_deg(weather['deg'])
            self.set_clouds(weather)
            self.set_snow(weather)
            self.set_rain(weather)
            self.set_weather_icon(weather['weather'][0]['icon'])
            self.set_weather_description(
                weather['weather'][0]['description']
            )
            self.set_weather_description_main(
                weather['weather'][0]['main']
            )

        except KeyError as e:
            raise Exception('Invalid Response Key: ' + '{}'.format(e))

    def set_temp_min(self, temp_min):
        self.__temp_min = temp_min
        return None

    def get_temp_min(self):
        return self.__temp_min

    def set_temp_max(self, temp_max):
        self.__temp_max = temp_max
        return None

    def get_temp_max(self):
        return self.__temp_max

    def set_temp_morn(self, temp_morn):
        self.__temp_morn = temp_morn
        return None

    def get_temp_morn(self):
        return self.__temp_morn

    def set_temp_day(self, temp_day):
        self.__temp_day = temp_day
        return None

    def get_temp_day(self):
        return self.__temp_day

    def set_temp_eve(self, temp_eve):
        self.__temp_eve = temp_eve
        return None

    def get_temp_eve(self):
        return self.__temp_eve

    def set_temp_night(self, temp_night):
        self.__temp_night = temp_night
        return None

    def get_temp_night(self):
        return self.__temp_night

    def set_humidity(self, humidity):
        self.__humidity = humidity
        return None

    def get_humidity(self):
        return self.__humidity

    def set_pressure(self, pressure):
        self.__pressure = pressure
        return None

    def get_pressure(self):
        return self.__pressure

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

    def set_clouds(self, weather):
        if 'clouds' in weather:
            self.__clouds = weather['clouds']
        return None

    def get_clouds(self):
        return self.__clouds

    def set_snow(self, weather):
        if 'snow' in weather:
            self.__snow = weather['snow']
        return None

    def get_snow(self):
        return self.__snow

    def set_rain(self, weather):
        if 'rain' in weather:
            self.__rain = weather['rain']
        return None

    def get_rain(self):
        return self.__rain

    def set_weather_icon(self, description):
        self.__weather_icon = description
        return None

    def get_weather_icon(self):
        return self.__weather_icon

    def set_weather_description(self, description):
        self.__weather_description = description
        return None

    def get_weather_description(self):
        return self.__weather_description

    def set_weather_description_main(self, description):
        self.__weather_description_main = description
        return None

    def get_weather_description_main(self):
        return self.__weather_description_main
