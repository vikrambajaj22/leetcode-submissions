class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols = len(image[0])

        original_color = image[sr][sc]

        if newColor == original_color:
            return image

        def dfs(r, c):
            if image[r][c] == original_color:
                image[r][c] = newColor
                if r-1 >= 0:
                    dfs(r-1, c)
                if r+1 < rows:
                    dfs(r+1, c)
                if c-1 >= 0:
                    dfs(r, c-1)
                if c+1 < cols:
                    dfs(r, c+1)

        dfs(sr, sc)
        return image
