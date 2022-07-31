class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        # inserting the new interval into the pre-sorted intervals list
        if newInterval[0] < intervals[0][0]:
            intervals = [newInterval] + intervals
        else:
            inserted = False
            for i in range(len(intervals)-1):
                if intervals[i][0] <= newInterval[0] <= intervals[i+1][0]:
                    intervals = intervals[:i+1] + [newInterval] + intervals[i+1:]
                    inserted = True
                    break
                    
            if not inserted:
                # start of newInterval must be greater than all existing intervals
                intervals.append(newInterval)
                
        # merging overlapping intervals
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                # overlap exists, perform merge
                intervals[i] = [intervals[i][0], max(intervals[i][1], intervals[i+1][1])]
                intervals.pop(i+1)
            else:
                i += 1
                
        return intervals