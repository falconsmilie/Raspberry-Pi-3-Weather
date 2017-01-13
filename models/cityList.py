from os import path, remove
from pathlib import Path as path_lib
from requests import get
import csv
import gzip
import json

class CityList(object):

    def __init__(self):
        # Server location of city list
        self._endpoint = 'http://bulk.openweathermap.org/sample/'
        self._endpoint_filename = 'city.list.json.gz'

        self._config_folder = 'config/'

        # Local location of compressed downloaded file
        self._city_list_filename_compressed = 'citylist.gzip'

        # Local location of uncompressed file
        self._city_list_filename_json = 'citylist.json'

        # Local location of converted JSON to CSV city list
        self._city_list_filename_csv = 'citylist.csv'

        #Request params
        self._request_timeout = 10

    def download_city_list(self):
        try:
            response = self.download()

            if path_lib(response).is_file():
                file_to_write = self.unpack(response)
            else:
                raise Exception('Error unpacking City List')

            if file_to_write:
                json_path = self.json_to_file(file_to_write)
            else:
                raise Exception('Error with City List JSON File Write')

            if json_path:
                self.json_to_csv(json_path)
            else:
                raise Exception('Error with City List CSV Conversion')

        except Exception as e:
            raise Exception(e)

    def download(self):

        response = get(
            self._endpoint + self._endpoint_filename,
            timeout=self._request_timeout,
            stream=True
        )

        compressed_path = path.join(
            path.dirname(path.realpath('__file__')),
            self._config_folder,
            self._city_list_filename_compressed
        )

        with open(compressed_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        f.close()

        return compressed_path

    def unpack(self, compressed_path):

        unpacked = False

        if path_lib(compressed_path).is_file():

            uncompressed_file = gzip.open(compressed_path, 'rb')

            unpacked = uncompressed_file.read()

            uncompressed_file.close()

            remove(compressed_path)

        return unpacked

    def json_to_file(self, file_to_write):

        json_path = path.join(
            path.dirname(path.realpath('__file__')),
            self._config_folder,
            self._city_list_filename_json
        )

        json_file = open(json_path, 'wb')
        json_file.write(file_to_write)
        json_file.close()

        return json_path

    def json_to_csv(self, json_path):

        csv_path = path.join(
            path.dirname(path.realpath('__file__')),
            self._config_folder,
            self._city_list_filename_csv
        )

        csv_file = csv.writer(open(csv_path, 'w'))

        # JSON is not in correct format
        with open(json_path, 'r') as f:
            for line in f:

                json_data = json.loads(line)

                #print(json_data['_id'], json_data['name'], json_data['country'])

                csv_file.writerow([
                    json_data['_id'],
                    json_data['name'],
                    json_data['country']
                    #json_data['coord']['lon'],
                    #json_data['coord']['lat']
                ])

        f.close()

        remove(json_path)

    def get(self):
        pass

    def update(self):
        pass


