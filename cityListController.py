from models.locationsManager import LocationsManager

try:
    locations = LocationsManager()

    # Download and create config files for locations
    # locations.create()

    # Gets list of countries
    countries = locations.get_countries()
    print(countries)

    # gets list of cities based on country code


except Exception as e:
    print(e)
