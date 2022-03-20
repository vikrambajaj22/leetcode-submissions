class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []  # (min-heap) always stores k elements

        for n in nums:
            if len(heap) == k:
                # compare n against smallest item in heap
                if n > heap[0]:
                    # remove smallest element from heap
                    heapq.heappop(heap)
                    # add n to heap
                    heapq.heappush(heap, n)
            else:
                heapq.heappush(heap, n)

        # since it is a min-heap (default), first element will be kth largest
        return heap[0]
