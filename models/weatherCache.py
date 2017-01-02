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
            directory = path.join(self.__path_to_cache, cache_folder)

            for filename in listdir(directory):
                print(filename)
                if filename.endswith('.json'):
                    files.append(filename)

            for filename in files:
                filetimestamp = '{:.10}'.format(filename)
                timestamp = time.time()

                if (timestamp - float(filetimestamp)) / 60 > cache_time:
                    file_del = path.join(
                        self.__path_to_cache,
                        cache_folder,
                        filename
                    )
                    remove(file_del)

        return None

    def check_cache(self, filename, request):
        """ Check for a cache file based on city ID and request type """

        name = '{}'.format(filename)

        files = glob.glob(
            self.__path_to_cache + request + '/*[0-9]-' + name + '.json'
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
