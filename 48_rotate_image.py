class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # first row becomes last column
        # second row becomes second-last column etc

        # first reverse, so first row becomes last row, second row becomes second-last row etc
        # matrix = matrix[::-1]  # works in terminal but not on leetcode
        matrix.reverse()

        # then transpose, so first row (original last row) becomes first column etc
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
