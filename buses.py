import urllib.request as urllib2
import json

class bus_class(object):
    def __init__(self, url):
        self.bus_maps = {}
        self.bus_URL = url+"buses"
    
    def fetch_bus_details(self):
        json_obj = urllib2.urlopen(self.bus_URL)
        data = json.load(json_obj)
        for bus_details in data:
            self.bus_maps[bus_details['id']] = {
                'name': bus_details['name'], 
                'lat': bus_details['lat'], 
                'lon': bus_details['lon'], 
                'route': bus_details['route'],
                'lastUpdate':bus_details['lastUpdate'], 
                'heading': bus_details['heading'],
                'lastStop':bus_details['lastStop']
            }
        return self.bus_maps
