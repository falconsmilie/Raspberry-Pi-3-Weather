from os import path
from pathlib import Path as path_lib
import json


class LanguageManager(object):

    def __init__(self):

        self._path_to_language_file = 'config/languageConfig.json'

    def get_languages(self):

        languages = []

        language_file_path = path.join(
            path.dirname(path.realpath('__file__')),
            self._path_to_language_file
        )

        if path_lib(language_file_path).is_file():

            with open(language_file_path, 'r') as language_config:
                language_json = json.load(language_config)

            for lang_id, lang in language_json.items():
                languages.append(''.join([lang,' (', lang_id, ')']))

            languages = sorted(languages)

        else:
            raise Exception('Cannot load Weather Languages.')

        return languages
