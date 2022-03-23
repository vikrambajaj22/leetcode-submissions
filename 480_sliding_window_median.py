class Solution(object):
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def add_num(self, num):
        heapq.heappush(self.max_heap, -num)
        max_heap_max = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_heap_max)

        # rebalance such that max heap has at most one element more than min heap
        if len(self.min_heap) > len(self.max_heap):
            min_heap_min = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_heap_min)

    def get_median(self):
        if len(self.min_heap) == len(self.max_heap):
            # k was even, return average of max of max_heap and min of min_heap
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            # k was odd, return max of max_heap
            return -self.max_heap[0]

    def remove_num(self, num):
        # find which heap the number is in
        if num > -self.max_heap[0]:
            # num is in min heap
            # removes first occurrence in case of duplicates
            self.min_heap.remove(num)
            heapq.heapify(self.min_heap)  # O(lg n)
        else:
            # num is in max heap
            self.max_heap.remove(-num)
            heapq.heapify(self.max_heap)

    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        curr = 0
        medians = []

        for i in range(len(nums)):
            self.add_num(nums[i])

            if i - curr + 1 == k:
                medians.append(self.get_median())
                curr += 1

                self.remove_num(nums[curr-1])

        return medians
