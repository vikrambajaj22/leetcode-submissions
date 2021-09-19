class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = []
        max_area = 0

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if (r, c) in visited or (r < 0 or r+1 > rows) or (c < 0 or c+1 > cols) or grid[r][c] == 0:
                return 0
            visited.append((r, c))
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:  # == 1
                    max_area = max(max_area, dfs(r, c))

        return max_area
