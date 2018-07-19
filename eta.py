import urllib.request as urllib2
import json
import requests

class eta_class(object):
    def __init__(self, url):
        self.eta_map = {}
        self.stops_URL = url+"eta?stop="
    
    def fetch_eta_by_stop_details(self, stopID):
        complete_URL = self.stops_URL+str(stopID)
        eta_detail = requests.get(complete_URL).json()['etas'][str(stopID)]['etas']
        return eta_detail
            
