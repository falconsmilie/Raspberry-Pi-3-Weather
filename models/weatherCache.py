import os
from pathlib import Path

class WeatherCache(object):

    def __init__(self):
        self.__path_to_cache = 'cache/'
        self.__cache_file_extension = '.json'


    def check_cache(self, filename):
        """ Check for existence of a cache file """

        file_dir = os.path.dirname(os.path.realpath('__file__'))

        cache_relative_path = self.__path_to_cache + filename + self.__cache_file_extension

        cache_file_path = os.path.join(file_dir, cache_relative_path) 
        
        cache_file = Path(cache_file_path)
        
        if cache_file.is_file():
            return self.read_cache(cache_file_path)
        else:
            return None
        
    
    def read_cache(self, filename):
        """ Read cache file """

        weather_cache = open(filename, 'rU')

        return weather_cache.read()
