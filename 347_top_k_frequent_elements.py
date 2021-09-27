class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # return [x for x,_ in Counter(nums).most_common(k)]

        # using a heap
        from heapq import heappush, heappop

        # create a list of (freq, val)
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        # push first k nums i.e. (freq, num) tuples onto heap
        nums = list(freq.keys())
        heap = []  # minheap by default

        for i in range(k):
            heappush(heap, (freq[nums[i]], nums[i]))

        for i in range(k, len(nums)):
            if freq[nums[i]] >= heap[0][0]:
                heappop(heap)  # removes smallest (topmost) element
                heappush(heap, (freq[nums[i]], nums[i]))

        # return heap elements (heap will have k elements)
        return [heappop(heap)[1] for _ in range(k)]
