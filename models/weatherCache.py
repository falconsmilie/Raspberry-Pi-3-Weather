from os import path, walk, listdir, remove
from pathlib import Path as path_lib
import time

class WeatherCache(object):

    def __init__(self):
        self.__path_to_cache = 'cache/'
        self.__cache_file_extension = '.json'


    def clean_cache(self):
        """ Removes cache files older than 10 minutes """
        
        files = []
        for file in listdir(self.__path_to_cache):
            if file.endswith('.json'):
                files.append(file)

        for file in files:
            file_timestamp = '{:.10}'.format(file)
            timestamp = time.time()

            if (timestamp - float(file_timestamp)) / 60 > 10:
                remove(self.__path_to_cache + file)


    def check_cache(self, filename):
        """ Check for existence of a cache file """
        
        cache_file_path = path.join(
            path.dirname(path.realpath('__file__')),
            self.__path_to_cache + filename + self.__cache_file_extension
        )
        
        if path_lib(cache_file_path).is_file():
            return self.read_cache(cache_file_path)
        else:
            return None


    def read_cache(self, filename):
        """ Read cache file """

        weather_cache = open(filename, 'rU')
        weather = weather_cache.read()
        weather_cache.close()

        return weather


    def set_cache(self, weather, location):
        """ Add the weather data to the cache """

        # Make sure we have strings
        weather = '{}'.format(weather)
        cache_time = '{}'.format(time.time())
        
        # Remove seconds from timestamp
        file_name = self.__path_to_cache + '{:.10}'.format(cache_time) + '-' + location + '.json'
        
        cache_file = open(file_name, 'w+', 1, 'utf-8')
        cache_file.write(weather)
        cache_file.close()
        
