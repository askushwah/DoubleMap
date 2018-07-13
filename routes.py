import urllib.request as urllib2
import json

class routes_class(object):
    def __init__(self, url):
        self.route_maps = []
        self.route_URL = url+"routes"
        self.shortname = []

    def fetch_routes_details(self):
        json_obj = urllib2.urlopen(self.route_URL)
        data = json.load(json_obj)
        for route_details in data:
            self.shortname.append(route_details['short_name'])
            self.route_maps.append(route_details)
            # self.route_maps[route_details['id']] = {
            #     'name': route_details['name'], 
            #     'short_name': route_details['short_name'], 
            #     'description':route_details['description'], 
            #     'color':route_details['color'],
            #     'path':route_details['path'], 
            #     'stops':route_details['stops']
            # }
        return self.route_maps

