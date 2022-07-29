class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.dfs(board, word, r, c, set(), 0):
                    return True
                
        return False
    
    
    def dfs(self, board, word, r, c, visited, index):
        if index == len(word):
            return True
        
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or (r, c) in visited or board[r][c] != word[index]:
            return False
        
        visited.add((r, c))
        
        res = self.dfs(board, word, r-1, c, visited, index+1) or self.dfs(board, word, r+1, c, visited, index+1) or self.dfs(board, word, r, c-1, visited, index+1) or self.dfs(board, word, r, c+1, visited, index+1)
        
        visited.remove((r, c))
        
        return res