import requests
import json
from weathersettings import Settings

class GeoProvider:
    def getgeo(self):
        r = requests.get(Settings().geourl)
        j = json.loads(r.text)
        lat = j['latitude']
        lon = j['longitude']
        return GeoLocation(lat,lon)

class GeoLocation:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon