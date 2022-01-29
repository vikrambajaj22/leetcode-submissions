class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        # construct a bi-directional graph in the form of an adjacency map
        # {u: {v: p}}

        graph = {u: {} for u in range(n)}
        for i, edge in enumerate(edges):
            u, v = edge

            graph[u][v] = succProb[i]
            graph[v][u] = succProb[i]

        visited = set()
        prob = {i: -1 for i in range(n)}  # nodes are 0-indexed from 0-(n-1)
        # modified dijkstra's since we want max probability instead of 'shortest' distance (in which case we would set initial distances to inf, so setting initial prob to -1 because 0<=prob<=1)

        # reset probability of start node (to itself) to 1 i.e. max-prob
        prob[start] = 1

        # heapq is min-heap but we need a max-heap, so converting value to negative
        heap = [(-1, start)]

        while heap:
            curr_prob, curr_node = heapq.heappop(heap)
            curr_prob = -curr_prob  # making it positive to get original value for calc below
            if curr_node in visited:
                continue
            visited.add(curr_node)

            if curr_node == end:
                return curr_prob  # early break in case end is visited since we don't need probabilities from source to all nodes, just the end node

            for node in graph[curr_node]:
                if node in visited:
                    continue
                if curr_prob * graph[curr_node][node] > prob[node]:
                    prob[node] = curr_prob * graph[curr_node][node]
                    heapq.heappush(heap, (-prob[node], node))

        return 0  # end was not visited
