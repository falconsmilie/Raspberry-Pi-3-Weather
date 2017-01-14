import json


class WeatherJson(object):

    def fix_json_string(self, json_string):
        """ Response from server is a dict and cache is a string """

        if isinstance(json_string, dict):
            json_string = json.dumps(json_string)

        weather = json_string.replace("'", '"')
        weather = json.loads(weather)

        return weather
