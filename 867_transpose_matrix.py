class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        res = [[0]*rows for _ in range(cols)]
        
        for i in range(cols):
            for j in range(rows):
                res[i][j] = matrix[j][i]
                
        return res