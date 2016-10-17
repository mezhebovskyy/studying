import requests
import json
import urllib
import datetime
from weathergeo import *
from weathersettings import Settings

class URLbuilder:
    def __init__(self):
        self.geoProvider = GeoProvider()

    def getUrl(self):
        location = self.geoProvider.getgeo()
        URL = Settings().initurl + "lat=" + str(location.lat) + "&lon=" + str(location.lon) + "&units=metric" + Settings().api
        return URL

class WeatherResponse:
    def __init__(self, info):
        self.city=info.get('name'),
        self.country=info.get('sys').get('country'),
        self.temp=int(info.get('main').get('temp')),
        self.temp_max=int(info.get('main').get('temp_max')),
        self.temp_min=int(info.get('main').get('temp_min')),
        self.humidity=info.get('main').get('humidity'),
        self.pressure=info.get('main').get('pressure'),
        self.sky=info['weather'][0]['description'],
        self.wind=info.get('wind').get('speed'),
        self.cloudiness=info.get('clouds').get('all')

class WeatherReader:
    def getWeatherResponse(self):
        output = requests.get(URLbuilder().getUrl())
        info = json.loads(output.text)
        response = WeatherResponse(info)
        return response

class WeatherPrinter:
    def pprint(self, data):
        data['m_symbol'] = ' \xb0' + 'C,'
        s = '''---------------------------------------
        Current weather in: {city}, {country}:
        {temp}{m_symbol}{sky}
        Max: {temp_max}, Min: {temp_min}

        Wind Speed: {wind} m/s
        Humidity: {humidity}%
        Cloud: {cloudiness}%
        Pressure: {pressure} hpa
        ---------------------------------------'''
        print(s.format(**data))

reader = WeatherReader()
response = reader.getWeatherResponse()
print(response.__dict__)
WeatherPrinter().pprint(response.__dict__)

