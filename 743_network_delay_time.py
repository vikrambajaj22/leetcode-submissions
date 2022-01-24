class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # use dijkstra's algo to get the shortest times to each node from source k
        # and then return the longest of these paths

        # graph is an adjacency map of the form 'u1': {'v1':t1, 'v2':t2, ...}
        graph = {u: {} for u in range(1, n+1)}
        for item in times:
            u, v, t = item
            graph[u][v] = t

        visited = set()
        # set distances to inf initially for all nodes 1-n
        distances = {i: float('inf') for i in range(1, n+1)}

        distances[k] = 0  # reset distance of source to itself to be 0
        heap = [(0, k)]  # min-heap to keep track of lowest distance

        while heap:
            curr_distance, curr_node = heapq.heappop(heap)
            if curr_node in visited:
                continue
            visited.add(curr_node)

            for node in graph[curr_node]:
                if node in visited:
                    continue
                if curr_distance + graph[curr_node][node] < distances[node]:
                    distances[node] = curr_distance + \
                        graph[curr_node][node]
                    heapq.heappush(heap, (distances[node], node))

        # checking for unreachable nodes
        if len(visited) < len(distances):
            return -1

        # return max of individual distances from source as the total time for the signal to propagate through the network
        return max(distances.values())
