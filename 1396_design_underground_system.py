class UndergroundSystem(object):

    def __init__(self):
        self.check_in_map = {}  # id: (source, check-in time)
        self.route_map = {}  # (source, dest): {total_time, route_count}
        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.check_in_map[id] = (stationName, t)
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        check_in_station, check_in_time = self.check_in_map[id]
        route = (check_in_station, stationName)
        
        if route not in self.route_map:
            self.route_map[route] = {'total_time': 0, 'route_count': 0}
        
        self.route_map[route]['total_time'] += (t - check_in_time)
        self.route_map[route]['route_count'] += 1
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        route = (startStation, endStation)
        return self.route_map[route]['total_time'] / float(self.route_map[route]['route_count'])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)