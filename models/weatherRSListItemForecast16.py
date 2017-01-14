class WeatherRSListItemForecast16(object):

    def __init__(self):
        """ Members of ListItem """
        self._temp_min = None
        self._temp_max = None
        self._temp_morn = None
        self._temp_day = None
        self._temp_eve = None
        self._temp_night = None
        self._humidity = None
        self._wind_speed = None
        self._wind_deg = None
        self._pressure = None
        self._clouds = None
        self._snow = None
        self._rain = None
        self._weather_desc = None
        self._weather_desc_main = None
        self._weather_icon = None
        self._time_of_weather = None

    def set_response(self, weather):
        """ Sets response variables to local members """
        try:
            self._temp_min = weather['temp']['min']
            self._temp_max = weather['temp']['max']
            self._temp_morn = weather['temp']['morn']
            self._temp_day = weather['temp']['day']
            self._temp_eve = weather['temp']['eve']
            self._temp_night = weather['temp']['night']
            self._humidity = weather['humidity']
            self._pressure = weather['pressure']
            self._wind_speed = weather['speed']
            self._wind_deg = weather['deg']
            self._weather_icon = weather['weather'][0]['icon']
            self._weather_desc = weather['weather'][0]['description']
            self._weather_desc_main = weather['weather'][0]['main']

            if 'clouds' in weather:
                self._clouds = weather['clouds']
            if 'snow' in weather:
                self._snow = weather['snow']
            if 'rain' in weather:
                self._rain = weather['rain']

        except KeyError as e:
            raise Exception(
                ''.join(['Invalid Response Key: ', '{}'.format(e)])
            )

    @property
    def temp_min(self):
        return self._temp_min

    @temp_min.setter
    def temp_min(self, temp_min):
        self._temp_min = temp_min
        return None

    @property
    def temp_max(self):
        return self._temp_max

    @temp_max.setter
    def temp_max(self, temp_max):
        self._temp_max = temp_max
        return None

    @property
    def temp_morn(self):
        return self._temp_morn

    @temp_morn.setter
    def temp_morn(self, temp_morn):
        self._temp_morn = temp_morn
        return None

    @property
    def temp_day(self):
        return self._temp_day

    @temp_day.setter
    def temp_day(self, temp_day):
        self._temp_day = temp_day
        return None

    @property
    def temp_eve(self):
        return self._temp_eve

    @temp_eve.setter
    def temp_eve(self, temp_eve):
        self._temp_eve = temp_eve
        return None

    @property
    def temp_night(self):
        return self._temp_night

    @temp_night.setter
    def temp_night(self, temp_night):
        self._temp_night = temp_night
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
    def pressure(self, pressure):
        self._pressure = pressure
        return None

    @property
    def wind_speed(self):
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, wind_speed):
        self._wind_speed = wind_speed
        return None

    @property
    def wind_deg(self):
        return self._wind_deg

    @wind_deg.setter
    def wind_deg(self, wind_deg):
        self._wind_deg = wind_deg
        return None

    @property
    def clouds(self):
        return self._clouds

    @clouds.setter
    def clouds(self, clouds):
        self._clouds = clouds
        return None

    @property
    def snow(self):
        return self._snow

    @snow.setter
    def snow(self, snow):
        self._snow = snow
        return None

    @property
    def rain(self):
        return self._rain

    @rain.setter
    def rain(self, rain):
        self._rain = rain
        return None

    @property
    def weather_icon(self):
        return self._weather_icon

    @weather_icon.setter
    def weather_icon(self, description):
        self._weather_icon = description
        return None

    @property
    def weather_desc(self):
        return self._weather_desc

    @weather_desc.setter
    def weather_desc(self, description):
        self._weather_desc = description
        return None

    @property
    def weather_desc_main(self):
        return self._weather_desc_main

    @weather_desc_main.setter
    def weather_desc_main(self, description):
        self._weather_desc_main = description
        return None
