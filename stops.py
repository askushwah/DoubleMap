import urllib.request as urllib2
import json

class bus_stops_class(object):
    def __init__(self, url):
        self.stops_maps = {}
        self.stops_URL = url+"stops"
    
    def fetch_stops_details(self):
        json_obj = urllib2.urlopen(self.stops_URL)
        data = json.load(json_obj)
        for stops_details in data:
            #self.stops_maps.append(stops_details)
            self.stops_maps[stops_details['id']] = {
                'name':stops_details['name'],
                'description':stops_details['description'],
                'lat':stops_details['lat'],
                'lon':stops_details['lon'],
                'buddy':stops_details['buddy']
                # stops_details['fields']
            }
        return self.stops_maps
