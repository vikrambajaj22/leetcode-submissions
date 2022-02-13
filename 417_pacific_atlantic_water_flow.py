class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        # logic: start from the borders and work inwards, using bfs to find cells with height >= current cell

        rows = len(heights)
        cols = len(heights[0])

        flows_atlantic = []  # queue for cells that can flow into atlantic
        flows_pacific = []  # queue for cells that can flow into pacific

        # adding border cells to appropriate queues
        for r in range(rows):
            flows_atlantic.append((r, cols-1))
            flows_pacific.append((r, 0))

        for c in range(cols):
            flows_atlantic.append((rows-1, c))
            flows_pacific.append((0, c))

        def bfs(queue):
            visited = set()

            while queue:
                r, c = queue.pop(0)
                visited.add((r, c))

                for x, y in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    new_r, new_c = r+x, c+y
                    if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited and heights[new_r][new_c] >= heights[r][c]:
                        queue.append((new_r, new_c))

            return visited

        atlantic = bfs(flows_atlantic)
        pacific = bfs(flows_pacific)

        # return list of cells that can flow into both i.e. intersection
        return list(set(atlantic).intersection(set(pacific)))
