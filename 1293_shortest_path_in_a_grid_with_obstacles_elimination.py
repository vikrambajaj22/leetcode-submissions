class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        
        if rows == 1 and cols == 1:
            return 0
        
        queue = [(0, 0, k, 0)]  # (r, c, k, steps)
        visited = set((0, 0, k))  # (r, c, k)
        
        while queue:
            r, c, k, steps = queue.pop(0)
            for x, y in [(0,1), (0,-1), (1, 0), (-1,0)]:
                new_r, new_c = r+x, c+y
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if grid[new_r][new_c] == 1 and k>0 and (new_r, new_c, k-1) not in visited:
                        queue.append((new_r, new_c, k-1, steps+1))
                        visited.add((new_r, new_c, k-1))
                    if grid[new_r][new_c] == 0 and (new_r, new_c, k) not in visited:
                        if new_r == rows-1 and new_c == cols-1:
                            # reached end
                            return steps + 1
                        queue.append((new_r, new_c, k, steps+1))
                        visited.add((new_r, new_c, k))
                        
        return -1
