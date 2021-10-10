class Solution(object):
    def __init__(self):
        self.perimeter = 0
        self.visited = set()

    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        def compute(r, c):
            self.visited.add((r, c))
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = r+x, c+y
                if new_r < 0 or new_r >= rows:
                    # first row or last row
                    self.perimeter += 1
                if new_c < 0 or new_c >= cols:
                    # first col or last col
                    self.perimeter += 1

                if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in self.visited:
                    if grid[new_r][new_c] == 0:
                        self.perimeter += 1
                    else:
                        self.visited.add((new_r, new_c))
                        compute(new_r, new_c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:  # find first 1
                    compute(r, c)
                    return self.perimeter
