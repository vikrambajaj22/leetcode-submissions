class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        
        while matrix:
            if matrix[0]:
                res.extend(matrix.pop(0))  # first row (left to right)
            
            # add last elements of remaining rows (top to bottom)
            if matrix:
                for row in matrix:
                    if row:
                        res.append(row.pop())
                    
            # last row in reverse (right to left)
            if matrix:
                res.extend(matrix.pop()[::-1])
                
            # first elements of remaining rows in reverse (bottom to top)
            if matrix:
                for row in matrix[::-1]:
                    if row:
                        res.append(row.pop(0))
                    
        return res
