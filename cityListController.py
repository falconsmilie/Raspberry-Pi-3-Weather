from models.locationsManager import LocationsManager

try:
    locations = LocationsManager()
    locations.create()

except Exception as e:
    print(e)
