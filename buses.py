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
            #self.bus_maps.append(bus_details)
            self.bus_maps.setdefault(bus_details['route'], [])
            if bus_details['route'] not in self.bus_maps:
                self.bus_maps[bus_details['route']] = {
                    'id': bus_details['id'],
                    'name': bus_details['name'], 
                    'lat': bus_details['lat'], 
                    'lon': bus_details['lon'], 
                    'lastUpdate':bus_details['lastUpdate'], 
                    'heading': bus_details['heading'],
                    'lastStop':bus_details['lastStop']
                    }
            else:
                self.bus_maps[bus_details['route']].append(
                    {
                    'id': bus_details['id'],
                    'name': bus_details['name'], 
                    'lat': bus_details['lat'], 
                    'lon': bus_details['lon'], 
                    'lastUpdate':bus_details['lastUpdate'], 
                    'heading': bus_details['heading'],
                    'lastStop':bus_details['lastStop']
                    }
                )
                
        return self.bus_maps

# details = bus_class("https://bloomington.doublemap.com/map/v2/")
# print(details.fetch_bus_details())


# {
#     1002255: [{'id': 1001573, 'name': '1573', 'lat': 39.16296, 'lon': -86.5004, 'lastUpdate': 1531833561, 'heading': 75, 'lastStop': 45601}],
#     1002245: [{'id': 1009727, 'name': '0551', 'lat': 39.16458, 'lon': -86.56401, 'lastUpdate': 1531833561, 'heading': 270, 'lastStop': 45135}, 
#             {'id': 1009736, 'name': '0350', 'lat': 39.16783, 'lon': -86.57572, 'lastUpdate': 1531833562, 'heading': 181, 'lastStop': 45717}, 
#             {'id': 1009739, 'name': '1675', 'lat': 39.16443, 'lon': -86.57206, 'lastUpdate': 1531833562, 'heading': 93, 'lastStop': 45376}], 
#     1002232: [{'id': 1009743, 'name': '762', 'lat': 39.17678, 'lon': -86.51881, 'lastUpdate': 1531833561, 'heading': 3, 'lastStop': 45333}], 
#     1002260: [{'id': 1009746, 'name': '1778', 'lat': 39.17028, 'lon': -86.53495, 'lastUpdate': 1531833559, 'heading': 0, 'lastStop': 45491}], 
#     1002251: [{'id': 1000967, 'name': '967', 'lat': 39.14682, 'lon': -86.51554, 'lastUpdate': 1531833561, 'heading': 272, 'lastStop': 45624}], 
#     1002239: [{'id': 1000761, 'name': '0761', 'lat': 39.17883, 'lon': -86.5526, 'lastUpdate': 1531833561, 'heading': 185, 'lastStop': 45308}], 
#     1002271: [{'id': 1009748, 'name': '1781', 'lat': 39.17162, 'lon': -86.50927, 'lastUpdate': 1531833559, 'heading': 268, 'lastStop': 45267}, 
#             {'id': 1009744, 'name': '1780', 'lat': 39.16115, 'lon': -86.49794, 'lastUpdate': 1531833559, 'heading': 166, 'lastStop': 45440}], 
#     1002241: [{'id': 1000864, 'name': '864', 'lat': 39.163, 'lon': -86.50218, 'lastUpdate': 1531833561, 'heading': 273, 'lastStop': 45636}, 
#             {'id': 1009726, 'name': '1574', 'lat': 39.15506, 'lon': -86.49695, 'lastUpdate': 1531833562, 'heading': 104, 'lastStop': 45441}], 
#     1002234: [{'id': 1000866, 'name': '0866', 'lat': 39.16366, 'lon': -86.53358, 'lastUpdate': 1531833561, 'heading': 360, 'lastStop': 45384}, 
#             {'id': 1000968, 'name': '968', 'lat': 39.14697, 'lon': -86.53248, 'lastUpdate': 1531833561, 'heading': 267, 'lastStop': 45226}], 
#     1002253: [{'id': 1009729, 'name': '0969', 'lat': 39.16429, 'lon': -86.51762, 'lastUpdate': 1531833562, 'heading': 271, 'lastStop': 45275}], 
#     1002249: [{'id': 1001371, 'name': '1371', 'lat': 39.16034, 'lon': -86.55079, 'lastUpdate': 1531833562, 'heading': 351, 'lastStop': 45539}], 
#     1002237: [{'id': 1000865, 'name': '865', 'lat': 39.14121, 'lon': -86.54517, 'lastUpdate': 1531833561, 'heading': 265, 'lastStop': 45578}], 
#     1002257: [{'id': 1009745, 'name': '1777', 'lat': 39.18522, 'lon': -86.53804, 'lastUpdate': 1531833561, 'heading': 270, 'lastStop': 45240}, 
#             {'id': 1000554, 'name': '0554', 'lat': 39.16102, 'lon': -86.47175, 'lastUpdate': 1531833561, 'heading': 75, 'lastStop': 45359}], 
#     1002273: [{'id': 1009740, 'name': '1676', 'lat': 39.16185, 'lon': -86.49791, 'lastUpdate': 1531833561, 'heading': 174, 'lastStop': 45314}], 
#     2000637: [{'id': 2000668, 'name': '668', 'lat': 39.16853, 'lon': -86.51235, 'lastUpdate': 1531833562, 'heading': 328, 'lastStop': 75}], 
#     2000630: [{'id': 2000661, 'name': '661', 'lat': 39.17161, 'lon': -86.5257, 'lastUpdate': 1531833562, 'heading': 91, 'lastStop': 131}, 
#             {'id': 2000662, 'name': '662', 'lat': 39.17981, 'lon': -86.52691, 'lastUpdate': 1531833562, 'heading': 340, 'lastStop': 35}], 
#     2000639: [{'id': 2000664, 'name': '664', 'lat': 39.17765, 'lon': -86.51246, 'lastUpdate': 1531833558, 'heading': 3, 'lastStop': 75}]}