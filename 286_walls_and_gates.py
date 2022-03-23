class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        # very similar to the 01 matrix problem
        rows = len(rooms)
        cols = len(rooms[0])

        # place all 0 locations (gates) in the queue and visited
        visited = set()
        queue = []

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    visited.add((r, c))
                    queue.append((r, c))

        while queue:
            r, c = queue.pop(0)
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = r+x, c+y
                if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited and rooms[new_r][new_c] == 2147483647:
                    rooms[new_r][new_c] = rooms[r][c] + 1
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c))

        return rooms
