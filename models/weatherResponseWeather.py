import json


class WeatherResponseWeather(object):

    def __init__(self):
        """ Members of the response """
        self.__city_name = None
        self.__city_id = None
        self.__country = None
        self.__sunrise = None
        self.__sunset = None
        self.__weather_desc_main = None
        self.__weather_desc = None
        self.__coord_lat = None
        self.__coord_lon = None
        self.__time_of_weather = None
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
            weather = self.fix_json_string(weather)

            self.set_city_name(weather['name'])
            self.set_city_id(weather['id'])
            self.set_country(weather['sys']['country'])
            self.set_sunrise(weather['sys']['sunrise'])
            self.set_sunset(weather['sys']['sunset'])
            self.set_weather_desc_main(weather['weather'][0]['main'])
            self.set_weather_desc(weather['weather'][0]['description'])
            self.set_coord_lat(weather['coord']['lat'])
            self.set_coord_lon(weather['coord']['lon'])
            self.set_time_of_weather(weather['dt'])
            self.set_pressure(weather['main']['pressure'])
            self.set_temp(weather['main']['temp'])
            self.set_temp_min(weather['main']['temp_min'])
            self.set_temp_max(weather['main']['temp_max'])
            self.set_humidity(weather['main']['humidity'])
            self.set_wind_speed(weather['wind']['speed'])
            self.set_wind_deg(weather['wind']['deg'])

        except KeyError as e:
            raise Exception('Invalid Response Key: ' + '{}'.format(e))

    def fix_json_string(self, weather):
        """ Response from server is dict and cache is string """

        if type(weather) is dict:
            weather = json.dumps(weather)

        weather = weather.replace("'",'"')
        weather = weather.replace('u"','"')
        weather = json.loads(weather)

        return weather

    def set_city_name(self, name):
        self.__city_name = name
        return None

    def get_city_name(self):
        return self.__city_name

    def set_city_id(self, name):
        self.__city_id = name
        return None

    def get_city_id(self):
        return self.__city_id

    def set_country(self, country):
        """ Country code (GB, JP etc.) """
        self.__country = country
        return None

    def get_country(self):
        return self.__country

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

    def set_coord_lat(self, coord_lat):
        self.__coord_lat = coord_lat
        return None

    def get_coord_lat(self):
        return self.__coord_lat

    def set_coord_lon(self, coord_lon):
        self.__coord_lon = coord_lon
        return None

    def get_coord_lon(self):
        return self.__coord_lon

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