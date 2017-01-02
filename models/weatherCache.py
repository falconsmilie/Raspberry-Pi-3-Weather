from os import path, walk, listdir, remove
import glob
import time


class WeatherCache(object):

    def __init__(self):
        self.__path_to_cache = 'cache/'
        self.__cache_folders = ['weather', 'forecast5', 'forecast16']

    def clean_cache(self, cache_time=10):
        """ Removes cache files older than '10' minutes """

        for cache_folder in self.__cache_folders:
            files = []
            for file in listdir(self.__path_to_cache):
                if file.endswith('.json'):
                    files.append(file)

            for file in files:
                file_timestamp = '{:.10}'.format(file)
                timestamp = time.time()

                if (timestamp - float(file_timestamp)) / 60 > cache_time:
                    remove(self.__path_to_cache + file)

        return None

    def check_cache(self, filename, request_type):
        """ Check for a cache file based on city ID and request type """

        filename = '{}'.format(filename)

        files = glob.glob(
            self.__path_to_cache + request_type + '/*[0-9]-' + filename + '.json'
        )

        if files:
            filename = files[0]

            cache_file_path = path.join(
                path.dirname(path.realpath('__file__')),
                filename
            )

            return self.read_cache(cache_file_path)
        else:
            return None

    def read_cache(self, filename):
        """ Read and return cache file """

        weather_cache = open(filename, 'rU')
        weather = weather_cache.read()
        weather_cache.close()

        return weather

    def set_cache(self, weather, location, request_type):
        """ Add the weather data to the cache """

        weather = '{}'.format(weather)
        location = '{}'.format(location)
        cache_time = '{}'.format(time.time())
        # Remove micro seconds from timestamp
        cache_time = '{:.10}'.format(cache_time)

        file_name = path.join(
            self.__path_to_cache,
            request_type,
            cache_time + '-' + location + '.json'
        )

        cache_file = open(file_name, 'w+')
        cache_file.write(weather)
        cache_file.close()

        return None
