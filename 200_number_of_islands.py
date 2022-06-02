class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r, c):
            visited.add((r, c))
            for x, y in [(0,1), (0,-1), (1,0), (-1,0)]:
                new_r, new_c = r+x, c+y
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c]=='1' and (new_r, new_c) not in visited:
                    dfs(new_r, new_c)
            
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    count += 1
                    
        return count