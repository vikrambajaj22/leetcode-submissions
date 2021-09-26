class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        mins = 0
        fresh = set()
        rotten = []  # queue

        # put all fresh and rotten ones in lists
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                elif grid[r][c] == 2:
                    rotten.append((r, c, mins))

        while rotten:
            r, c, mins = rotten.pop(0)
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = r+x, c+y
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                    grid[new_r][new_c] = 2
                    # add to rotten
                    rotten.append((new_r, new_c, mins+1))
                    # remove from fresh
                    fresh.remove((new_r, new_c))

        # if fresh still has elements, it wasn't possible to make all rotten
        # i.e. some 1s were not 4-directionally connected
        if fresh:
            return -1
        else:
            return mins
