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
        if shortName not in self.shortnames:
            print("Please enter a valid bus name")
            return
        else:
            for busdetails in self.routes:
                if shortName == busdetails['short_name']:
                    route_list.append([str(busdetails['id']),busdetails['name']])
                    count += 1
            if count > 1:
                print("There are two buses for the same route. Which one do you want?")
                print(route_list)
                var = input()
                for i in route_list:
                    if var in i:
                        routeID = int(i[0])
                        break
            else:
                routeID = int(route_list[0][0])
        busInfo = self.returnBusDetails(self.returnURL())
        for info in busInfo:
            if info['route'] == routeID:
                lastStopID.append(info['lastStop'])
        for lastStop in lastStopID:
            for stop_info in self.stops:
                if str(stop_info['id'])[-len(str(lastStop)):] == str(lastStop):
                    print("The bus is at: ", stop_info['name'])


if __name__ == "__main__":
    doubleMapObj = DoubleMap()
    #return the url and while passing add the revelent addition to the URL
    getURL = doubleMapObj.returnURL()
    # doubleMapObj.returnRouteDetails(getURL)
    # print(doubleMapObj.returnRouteDetails(getURL))
    # print(doubleMapObj.returnBusDetails(getURL))
    #print(doubleMapObj.stops)
    # print(doubleMapObj.shortnames)
    doubleMapObj.getCurrentLocationOfBus("6")