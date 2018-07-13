from stops import bus_stops_class
from routes import routes_class
from buses import bus_class
import time
class DoubleMap(object):
    def __init__(self):
        self.url = "https://bloomington.doublemap.com/map/v2/"
        # self.routes = self.returnRouteDetails(self.url)

    def returnURL(self):
        return self.url
    
    def returnStopsDetails(self, url):
        # get the stops details
        stopsDetailsObj = bus_stops_class(url)
        stopsDetails = stopsDetailsObj.fetch_stops_details()
        return stopsDetails
    
    def returnRouteDetails(self, url):
        # get the route details
        routeDetailsObj = routes_class(url)
        routeDetails = routeDetailsObj.fetch_routes_details()
        return routeDetails
    
    def returnBusDetails(self, url):
        # get the bus details
        busDetailsObj = bus_class(getURL)
        busDetails = busDetailsObj.fetch_bus_details()
        return busDetails


if __name__ == "__main__":
    doubleMapObj = DoubleMap()
    #return the url and while passing add the revelent addition to the URL
    getURL = doubleMapObj.returnURL()
    # print(doubleMapObj.returnBusDetails(getURL))
    # print(doubleMapObj.routes)
 