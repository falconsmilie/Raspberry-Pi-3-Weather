from requests import get

class WeatherRequest(object):

    def __init__(self):
        self.location = None


    def set_location(self, location):
        self.location = location
        

    def get_weather(self):
        
        url = 'http://api.openweathermap.org/data/2.5/weather?id=6553173&APPID=eb413f0e77c9f8176ead6e79fa8b004d'
        weather = get(url).json()
