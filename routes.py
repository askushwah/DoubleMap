import urllib.request as urllib2
import json

class routes_class(object):
    def __init__(self, url):
        self.route_maps = {}
        self.route_maps_by_id = {}
        self.route_URL = url+"routes"
        self.shortname = []

    def fetch_routes_details(self):
        json_obj = urllib2.urlopen(self.route_URL)
        data = json.load(json_obj)
        for route_details in data:
            self.shortname.append(route_details['short_name'])
            #self.route_maps.append(route_details)
            self.route_maps.setdefault(route_details['short_name'], [])
            if route_details['short_name']not in self.route_maps:
                self.route_maps[route_details['short_name']] = {
                    'id': route_details['id'], 
                    'name': route_details['name'], 
                    'description':route_details['description'], 
                    'color':route_details['color'],
                    'path':route_details['path'], 
                    'stops':route_details['stops']
                }
            else:
                self.route_maps[route_details['short_name']].append({
                    'id': route_details['id'], 
                    'name': route_details['name'], 
                    'description':route_details['description'], 
                    'color':route_details['color'],
                    'path':route_details['path'], 
                    'stops':route_details['stops']
                })
        return self.route_maps
    
    def fetch_routes_details_by_id(self):
        json_obj = urllib2.urlopen(self.route_URL)
        data = json.load(json_obj)
        for route_details in data:
            if route_details['id']not in self.route_maps_by_id:
                self.route_maps_by_id[route_details['id']] = {
                    'short_name': route_details['short_name'], 
                    'name': route_details['name']
                }
            else:
                self.route_maps_by_id[route_details['id']].append({
                    'short_name': route_details['short_name'], 
                    'name': route_details['name']
                })
        return self.route_maps_by_id


# details = routes_class("https://bloomington.doublemap.com/map/v2/")
# details.fetch_routes_details()
# print(details.shortname)
