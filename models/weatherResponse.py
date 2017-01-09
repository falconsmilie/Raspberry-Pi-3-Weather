class WeatherResponse(object):

    def __init__(self):
        """ Members available to each response type """
        self.__city_name = None
        self.__city_id = None
        self.__country = None
        self.__coord_lat = None
        self.__coord_lon = None

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
