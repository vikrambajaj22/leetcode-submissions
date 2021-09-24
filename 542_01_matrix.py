class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])

        # reverse the problem, and start with 0s
        # add all 0s to queue and visited
        # then, look in all 4 directions for each queue item (current cell),
        # and if not in visited, must be land
        # so, update that cell to be current cell + 1, and add to queue and visited

        queue = []
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        while queue:
            curr_r, curr_c = queue.pop(0)  # bfs
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # 4 directions
                new_r, new_c = curr_r+x, curr_c+y
                if 0 <= new_r < rows and 0 <= new_c < cols and \
                        (new_r, new_c) not in visited:
                    mat[new_r][new_c] = mat[curr_r][curr_c] + 1
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c))

        return mat
