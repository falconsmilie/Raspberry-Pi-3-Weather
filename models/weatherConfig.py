import json
from os import path
from pathlib import Path as path_lib


class WeatherConfig(object):

    def __init__(self):
        """ Set local members """
        self.__path_to_config_file = 'config/weatherConfig.json'
        self.__config = None

    def set_config(self):
        """ Read and then set JSON config file to local member """

        config_file_path = path.join(
            path.dirname(path.realpath('__file__')),
            self.__path_to_config_file
        )

        if path_lib(config_file_path).is_file():

            json_config = open(config_file_path, 'rU')
            self.__config = json.load(json_config)
            json_config.close()

        else:
            raise Exception('Cannot load Weather Config.')

        return None

    def get_config_all(self):
        """ Return all config items """

        if self.__config is None:
            raise Exception(
                'There is nothing in the Weather Config to load.'
            )

        return self.__config
