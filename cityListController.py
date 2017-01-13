from models.cityList import CityList

try:
    city_request = CityList()
    city_request.download_city_list()

except Exception as e:
    print(e)
