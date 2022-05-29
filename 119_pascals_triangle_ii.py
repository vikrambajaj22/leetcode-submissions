class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangle = [[1], [1,1]]
        
        for i in range(2, rowIndex+1):
            row = [1]
            for j in range(len(triangle[i-1])-1):
                row.append(triangle[i-1][j]+triangle[i-1][j+1])
            row.append(1)
            triangle.append(row)
            
        return triangle[rowIndex]