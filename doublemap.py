from stops import bus_stops_class
from routes import routes_class
from buses import bus_class
from eta import eta_class
from datetime import datetime

class DoubleMap(object):
    def __init__(self):
        self.url = "https://bloomington.doublemap.com/map/v2/"
        self.routes = self.returnRouteDetails(self.url)[0]
        self.routesDetailsByID = self.returnRouteDetailsById(self.url)
        self.stops = self.returnStopsDetails(self.url)
        self.shortnames = self.returnRouteDetails(self.url)[1]
        self.stopNames = self.returnStopNames(self.url)


    def returnURL(self):
        return self.url
    
    def returnStopsDetails(self, url):
        # get the stops details
        stopsDetailsObj = bus_stops_class(url)
        stopsDetails = stopsDetailsObj.fetch_stops_details()
        return stopsDetails
    def returnRouteDetailsById(self, url):
        routeDetailByIdObj = routes_class(url)
        routeDetialsByID = routeDetailByIdObj.fetch_routes_details_by_id()
        return routeDetialsByID
    
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
    
    def returnStopNames(self, url):
        stopNameObj = bus_stops_class(url)
        stopNameDetails = stopNameObj.fetch_stops_details_names()
        return stopNameDetails
    
    def returnEtaByStop(self, url, stopID):
        etaObj = eta_class(url)
        etabByStopDetail = etaObj.fetch_eta_by_stop_details(stopID)
        return etabByStopDetail

    def getCurrentLocationOfBus(self, shortName):
        count = 0
        route_list = list()
        lastStopID = []
        if len(self.shortnames) == 0:
            print("The buses have ended or not started yet!")
            return
        if shortName not in self.shortnames:
            print("Please enter a valid bus name")
            return
        else:
            route_list = self.routes[shortName]
            print(route_list)
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
    
    def etaByStop(self, stopName):
        stopName = stopName.lower()
        for name, values in self.stopNames.items():
            if stopName in name.lower():
                etaDetails = self.returnEtaByStop(self.returnURL(), values['id'])
                for eta in etaDetails:
                    print("{} will arrive at {} in {} mins".format(self.routesDetailsByID[eta['route']]['short_name'],  name, eta['avg']))
                break



if __name__ == "__main__":
    doubleMapObj = DoubleMap()
    #return the url and while passing add the revelent addition to the URL
    getURL = doubleMapObj.returnURL()
    # t1 = datetime.now()
    # doubleMapObj.getCurrentLocationOfBus("3")
    # t2 = datetime.now()
    # delta = t2 - t1
    # print("Time elapsed: ",delta.seconds + delta.microseconds/1E6)
    # t1 = datetime.now()
    # doubleMapObj.getCurrentLocationOfBus("6")
    # t2 = datetime.now()
    # delta = t2 - t1
    # print("Time elapsed: ",delta.seconds + delta.microseconds/1E6)
    t1 = datetime.now()
    doubleMapObj.etaByStop("fountain park")
    t2 = datetime.now()
    delta = t2 - t1
    print("Time elapsed: ",delta.seconds + delta.microseconds/1E6)