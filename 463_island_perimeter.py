class Solution(object):
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.visited = set()
        self.perimeter = 0
        
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.rows = len(grid)
        self.cols = len(grid[0])
        
        # find the first 1
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c]:  # == 1
                    self.computePerimeter(r, c, grid)
                    return self.perimeter
                    
    def computePerimeter(self, r, c, grid):
        self.visited.add((r, c))
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for x, y in directions:
            new_r, new_c = r+x, c+y
            
            if new_r < 0 or new_r >= self.rows:
                # first or last row
                self.perimeter += 1
            if new_c < 0 or new_c >= self.cols:
                # first or last column
                self.perimeter += 1

            if 0 <= new_r < self.rows and 0 <= new_c < self.cols and (new_r, new_c) not in self.visited:
                if grid[new_r][new_c] == 0:  # water
                    self.perimeter += 1
                else:
                    self.computePerimeter(new_r, new_c, grid)