class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = [[1], [1, 1]]

        if numRows in [1, 2]:
            return pascal[:numRows]

        for i in range(3, numRows + 1):
            prev = pascal[-1]
            current = [1]
            for j in range(len(prev)-1):
                current.append(prev[j] + prev[j+1])
            current.append(1)
            pascal.append(current)

        return pascal
