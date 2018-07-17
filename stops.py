import urllib.request as urllib2
import json

class bus_stops_class(object):
    def __init__(self, url):
        self.stops_maps = {}
        self.stops_maps_names = {}
        self.stops_URL = url+"stops"
        self.json_obj = urllib2.urlopen(self.stops_URL)
        self.data = json.load(self.json_obj)
    
    def fetch_stops_details(self):
        for stops_details in self.data:
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
    
    def fetch_stops_details_names(self):
        for stops_details in self.data:
            self.stops_maps_names[stops_details['name']] = {
                'id':stops_details['id'],
                'description':stops_details['description'],
                'lat':stops_details['lat'],
                'lon':stops_details['lon'],
                'buddy':stops_details['buddy']
            }
        return self.stops_maps_names

