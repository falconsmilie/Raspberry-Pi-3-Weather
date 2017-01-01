import json
import os
from pathlib import Path


class WeatherConfigError(Exception):
    """ Exception Handling """

    def __int__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class WeatherConfig(object):

    def __init__(self):
        self.__relative_path_to_config_file = 'config/weatherConfig.json'
        self.__config = None

    def set_config(self):
        """ Read and then set JSON config file to local member """

        file_dir = os.path.dirname(os.path.realpath('__file__'))

        config_file_path = os.path.join(
            file_dir,
            self.__relative_path_to_config_file
        )

        config_file = Path(config_file_path)

        if config_file.is_file():

            json_config = open(config_file_path)
            self.__config = json.load(json_config)
            json_config.close()

        else:
            raise WeatherConfigError('Cannot load Weather Config.')

        return None

    def get_config_all(self):
        """ Return all config items """

        if self.__config is None:
            raise WeatherConfigError(
                'There is nothing in the Weather Config to load.'
            )

        return self.__config
