class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # cannot use greedy approach of always choosing local minima
        # can lead to skipping of other minumums in the row

        # instead use a bottom-up approach, and update the tringle as you go

        for i in range(len(triangle)-2, -1, -1):  # start from second-last row
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]  # will contain minimum sum
