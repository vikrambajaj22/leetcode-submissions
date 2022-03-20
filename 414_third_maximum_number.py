class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # non-heap solution
        # unique = list(set(nums))
        # if len(unique) < 3:
        #     return max(unique)
        # return sorted(unique)[len(unique)-3]

        # heap solution
        nums = list(set(nums))

        heap = []

        for n in nums:
            if len(heap) == 3:
                if n > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, n)
            else:
                heapq.heappush(heap, n)

        if len(heap) < 3:
            return heap[-1]
        else:
            return heap[0]
