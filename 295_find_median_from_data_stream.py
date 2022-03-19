class MedianFinder(object):

    def __init__(self):
        self.lower = []  # max-heap to store lower half of numbers
        self.upper = []  # min-heap to store upper half of numbers
        # logic: since median is the middle value for which half the numbers are lower and half are higher than it, we do not need to continually sort the lower and upper halves but simply need the max of the lower half and min of upper half to compute the median
        # the max-heap (lower) must always have at most one element more than the min-heap (upper) to keep the halves balanced
        # in Python, heapq implements a min-heap, so we store numbers as negative to achieve a max-heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.lower, -num)
        lower_max = -heapq.heappop(self.lower)

        heapq.heappush(self.upper, lower_max)

        if len(self.upper) > len(self.lower):
            # pop from upper and put onto lower
            upper_min = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -upper_min)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.lower) == len(self.upper):
            # even number of elements, so take average of lower_max and upper_min
            # needs to return float
            return (-self.lower[0]+self.upper[0]) / 2.0
        else:
            # return max of lower, because it has at most one element more than upper
            # and this element is the median
            return -self.lower[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
