class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        
        def dfs(r, c, index, visited):
            if index == len(word):
                return True
            
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or board[r][c] != word[index]:
                return False
            
            visited.add((r, c))
            res = dfs(r-1, c, index+1, visited) or dfs(r+1, c, index+1, visited) or dfs(r, c-1, index+1, visited) or dfs(r, c+1, index+1, visited)
            visited.remove((r, c))
            
            return res
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()): return True
                    
        return False