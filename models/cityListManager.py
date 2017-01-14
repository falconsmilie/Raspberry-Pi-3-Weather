from operator import itemgetter
from os import path, remove
from pathlib import Path as path_lib
from requests import get
import csv
import gzip
import json


class CityListManager(object):

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
        # Local location of country CSV list
        self._country_list_filename_csv = 'countrylist.csv'

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
                create_csv = self.json_to_csv(json_path)
            else:
                raise Exception('Error with City List CSV Conversion')

            if create_csv:
                self.create_csv_countries()
                self.create_csv_city_lists()

        except Exception as e:
            raise Exception(e)

    def download(self):
        """ Downloadds GZIP from server """
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
        """ Unpacks GZIP then returns contents """
        unpacked = False

        if path_lib(compressed_path).is_file():
            uncompressed_file = gzip.open(compressed_path, 'rb')
            unpacked = uncompressed_file.read()
            uncompressed_file.close()
            remove(compressed_path)

        return unpacked

    def json_to_file(self, file_to_write):
        """ Accepts data for writing to JSON file """
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
        """ Convert JSON to CSV and write to file """
        csv_path = path.join(
            path.dirname(path.realpath('__file__')),
            self._config_folder,
            self._city_list_filename_csv
        )
        csv_file_to_read = open(csv_path, 'w')
        csv_file = csv.writer(csv_file_to_read)

        # JSON is not in correct format
        with open(json_path, 'r') as f:
            for line in f:
                json_data = json.loads(line)
                csv_file.writerow([
                    json_data['_id'],
                    json_data['name'],
                    json_data['country']
                    #json_data['coord']['lon'],
                    #json_data['coord']['lat']
                ])
        csv_file_to_read.close()
        f.close()

        remove(json_path)

        return True

    def create_csv_countries(self):
        """ Creates list of Countries from CSV, writes to file """
        csv_path = path.join(
            path.dirname(path.realpath('__file__')),
            self._config_folder,
            self._city_list_filename_csv
        )

        countries = []

        with open(csv_path, 'rU') as csv_file:
            for line in csv_file:
                splits = line.split(',')
                code = splits[2].rstrip('\n')
                # There can be dodgy data in the downloaded file :\
                if code not in countries and len(code) == 2:
                    countries.append(code)
        csv_file.close()

        csv_countries_path = path.join(
            path.dirname(path.realpath('__file__')),
            self._config_folder,
            self._country_list_filename_csv
        )

        csv_file = csv.writer(open(csv_countries_path, 'w'))
        csv_file.writerows([sorted(countries)])

    def create_csv_city_lists(self):
        """ Create list of files by country, containing city data """

        countrycities = self.get_country_cities_list()

        for country, cities in countrycities.items():

            sorted_cities = sorted(cities.items(), key=itemgetter(1))
            seen = set()
            unique_cities = []

            for city_data in sorted_cities:
                if city_data[1] not in seen:
                    seen.add(city_data[1])
                    unique_cities.append(city_data)

            csv_path = path.join(
                path.dirname(path.realpath('__file__')),
                self._config_folder,
                country + '-cities.csv'
            )
            csv_file_open = open(csv_path, 'w')
            csv_file = csv.writer(csv_file_open)

            for cityid, city in unique_cities:
                csv_file.writerow([cityid, city])

            csv_file_open.close()

        return True

    def get_country_cities_list(self):
        """ Create Dict of Countries, assigned with City data """
        csv_countries_path = path.join(
            path.dirname(path.realpath('__file__')),
            self._config_folder,
            self._country_list_filename_csv
        )

        countries_file = open(csv_countries_path)
        countries_data = countries_file.read()
        countries_file.close()
        countries_data.rstrip('\n')
        countries = countries_data.split(',')

        csv_path = path.join(
            path.dirname(path.realpath('__file__')),
            self._config_folder,
            self._city_list_filename_csv
        )

        countrycities = {}
        with open(csv_path, 'rU') as csv_file:
            for line in csv_file:

                splits = line.split(',')
                splits[2] = splits[2].rstrip('\n')

                if splits[2] in countries:
                    countrycities \
                        .setdefault(splits[2], {}) \
                        .setdefault(splits[0], splits[1])
        csv_file.close()
        remove(csv_path)

        return countrycities
