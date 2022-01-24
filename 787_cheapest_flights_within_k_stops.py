class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        graph = {i: {} for i in range(n)}
        for flight in flights:
            u, v, p = flight
            graph[u][v] = p

        prices = {i: float('inf') for i in range(n)}
        prices[src] = 0
        visited = {}

        heap = [(0, src, -1)]

        while heap:
            curr_price, curr_city, curr_stops = heapq.heappop(heap)
            if curr_city == dst and curr_stops <= k:
                return curr_price
            if curr_stops > k:
                continue

            if curr_city not in visited or visited[curr_city] > curr_stops:
                visited[curr_city] = curr_stops

            for city in graph[curr_city]:
                if city not in visited or visited[city] > curr_stops:
                    prices[city] = curr_price + graph[curr_city][city]
                    heapq.heappush(heap, (prices[city], city, curr_stops+1))

        return -1
