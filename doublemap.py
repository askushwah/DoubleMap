from stops import bus_stops_class
from routes import routes_class
from buses import bus_class
import time
class DoubleMap(object):
    def __init__(self):
        self.url = "https://bloomington.doublemap.com/map/v2/"
        self.routes = self.returnRouteDetails(self.url)[0]
        self.stops = self.returnStopsDetails(self.url)
        self.shortnames = self.returnRouteDetails(self.url)[1]

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
        shortNames = routeDetailsObj.shortname
        return routeDetails, shortNames
    
    def returnBusDetails(self, url):
        # get the bus details
        busDetailsObj = bus_class(getURL)
        busDetails = busDetailsObj.fetch_bus_details()
        return busDetails

    def getCurrentLocationOfBus(self, shortName):
        count = 0
        route_list = list()
        routeID = 0
        lastStopID = []
        if len(self.shortnames) == 0:
            print("The buses have ended or not started yet!")
            return
        if shortName not in self.shortnames:
            print("Please enter a valid bus name")
            return
        else:
            route_list = self.routes[shortName]
            routeid_list = []
            count = 0
            if len(route_list) > 1:
                while count < len(route_list):
                    routeid_list.append(route_list[count]['id'])
                    count += 1
            else:
                routeid_list.append(route_list[count]['id'])
            #print(routeid_list)
            busInfo = self.returnBusDetails(self.returnURL())
            lastStopID = []
            for route_id in routeid_list:
                temp_list = busInfo[route_id]
                for stopID in temp_list:
                    lastStopID.append(stopID['lastStop'])
            
            for lastStop in lastStopID:
                print("Bus {} is at {}".format(shortName, self.stops[int("10"+str(lastStop))]['name']))

if __name__ == "__main__":
    doubleMapObj = DoubleMap()
    #return the url and while passing add the revelent addition to the URL
    getURL = doubleMapObj.returnURL()
    doubleMapObj.getCurrentLocationOfBus("6")