class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        heap = []  # max-heap with k elements (-distance, item)
        
        for item in arr:
            if len(heap) == k:
                if abs(x-item) < -heap[0][0] or (abs(x-item) == -heap[0][0] and item < heap[0][1]):
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-abs(x-item), item))  # negative because max_heap   
            else:
                heapq.heappush(heap, (-abs(x-item), item))
                
        return sorted([item[1] for item in heap])