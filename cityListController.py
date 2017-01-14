from models.cityListManager import CityListManager

try:
    city_request = CityListManager()
    city_request.download_city_list()

except Exception as e:
    print(e)
