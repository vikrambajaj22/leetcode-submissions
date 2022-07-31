class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # greedy algo: interval scheduling problem
        
        # sort in asc order of end times
        intervals = sorted(intervals, key = lambda i:i[1])
        
        count = 0  # count of intervals to remove
        curr_lowest_end = -float('inf')

        for s, e in intervals:
            if s < curr_lowest_end:
                # interval starts before current lowest end
                count += 1  # remove overlapping interval
            else:
                # update curr_lowest_end
                curr_lowest_end = e
                
        return count
            
        
        