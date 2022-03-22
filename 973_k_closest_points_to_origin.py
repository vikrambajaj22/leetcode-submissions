class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
#         # storing all points at a certain distance from origin together, using distance as dict key

#         points_at_distance = {}

#         for [x, y] in points:
#             dist = x**2 + y**2  # no need of sqrt
#             if dist not in points_at_distance:
#                 points_at_distance[dist] = [[x, y]]
#             else:
#                 points_at_distance[dist].append([x, y])

#         k_closest = []

#         sorted_distances = sorted(list(points_at_distance.keys()))

#         print(points_at_distance)

#         for dist in sorted_distances:
#             for point in points_at_distance[dist]:
#                 if len(k_closest) == k:
#                     break
#                 k_closest.append(point)

#         return k_closest

        # using a heap (max-heap)
        heap = []  # will store (-dist, point) tuples
        # since heap is a min-heap by default, we store -dist to convert it to a max-heap

        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            if len(heap) == k:
                if dist < -heap[0][0]:
                    # comparing with distance of farthest point in heap i.e. first item in heap
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-dist, point))
            else:
                heapq.heappush(heap, (-dist, point))

        # return points in heap
        return [p[1] for p in heap]
