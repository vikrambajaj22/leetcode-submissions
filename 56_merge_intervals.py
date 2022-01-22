class Solution(object):
    def intervals_overlap(self, interval_1, interval_2):
        return interval_1[1] >= interval_2[0]
    
    
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda i:i[0])
        
        i = 0
        while i < len(intervals)-1:
            if self.intervals_overlap(intervals[i], intervals[i+1]):
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
            else:
                i += 1
                
        return intervals