import json
from os import path
from pathlib import Path as path_lib


class WeatherConfig(object):

    def __init__(self):
        """ Set local members """
        self._path_to_config_file = 'config/weatherConfig.json'
        self._config = None
        self._config_keys = [
            'api_key', 'location', 'request_type', 'forecast_count_5',
            'forecast_count_16', 'units', 'lang'
        ]

    def set(self):
        """ Read and then set JSON config file to local member """
        config_file_path = path.join(
            path.dirname(path.realpath('__file__')),
            self._path_to_config_file
        )

        if path_lib(config_file_path).is_file():

            with open(config_file_path, 'rU') as json_config:
                self._config = json.load(json_config)

            self.validate()
        else:
            raise Exception('Cannot load Weather Config.')

        return None

    def get(self):
        """ Return all config items """
        if self._config is None:
            raise Exception(
                'There is nothing in the Weather Config to load.'
            )

        if self.validate():
            return self._config

    def validate(self):
        """ Check keys are all there. Pain to update, but cool for user
        of this class knowing they are going to get all the keys back.
        """
        for key in self._config_keys:
            if not key in self._config:
                raise Exception('Data is missing from Config: ' + key)

        return True
