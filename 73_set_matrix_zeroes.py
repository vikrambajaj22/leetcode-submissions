class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # O(m+n) space complexity: use a set to store all row and column numbers where any element is 0; then, make those row and col elements all 0s
        # O(1) space complexity: below
        
        # check if first row and first col have any zeros in the original matrix
        # simultaneously, if any matrix[r][c] is 0, set matrix[r][0] and matrix[0][c] to 0
        # so, instead of using an additional set, we use the first row and first column to keep track of rows and cols that need to be set to 0s
        first_row_has_zero = False
        first_col_has_zero = False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0: first_row_has_zero = True
                    if c == 0: first_col_has_zero = True
                    matrix[r][0] = 0
                    matrix[0][c] = 0
                    
        # from the second row and col, use first row and first column markers to set those rows and cols to 0
        for r in range(1, rows):
            for c in range(1, cols):
                matrix[r][c] = 0 if matrix[r][0]==0 or matrix[0][c]==0 else matrix[r][c]
                
        # now, based on first_row_has_zero and first_col_has_zero, set first row and col to 0
        if first_row_has_zero:
            for c in range(cols):
                matrix[0][c] = 0
                
        if first_col_has_zero:
            for r in range(rows):
                matrix[r][0] = 0