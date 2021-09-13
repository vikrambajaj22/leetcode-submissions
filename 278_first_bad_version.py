# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # brute-force is to check all numbers till API returns True
        # efficient way: Binary search
        low = 1
        high = n

        while low < high:
            mid = (low + high) // 2

            if isBadVersion(mid):
                # either mid or any previous version could be the first bad one
                high = mid

            else:
                # every version up to and including mid is good
                low = mid + 1

        # terminating condition: when low == high, that's the first bad version
        return low
