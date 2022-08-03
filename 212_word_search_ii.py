# this solution is optimal, but can get TLE
# a more optimal solution involves pruning the trie (not doing)
class Trie(object):
    def __init__(self):
        self.trie = {}
        
    
    def insert(self, word):
        t = self.trie
        for ch in word:
            if ch not in t:
                t[ch] = {}
            t = t[ch]
            
        t['is_end'] = True
    
    
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # could do # 79 word search for each word
        # the solution for # 79 does a dfs (with backtracking) from each cell of the grid
        # if we do this for each word in the word list, it will be very inefficient
        # instead, use a trie to determine which cells to perform dfs (with backtracking) from
        
        # start by inserting all words into the trie
        t = Trie()
        for word in words:
            t.insert(word)
            
        found = []
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, trie, substr):
            if 'is_end' in trie:
                found.append(substr)
                # since the word is found, remove it from the trie (by deleting is_end) to prevent unnecessary dfs in the future attempting to find the word again
                del trie['is_end']
                
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and board[r][c] in trie:
                visited.add((r, c))
                dfs(r-1, c, trie[board[r][c]], substr+board[r][c])
                dfs(r+1, c, trie[board[r][c]], substr+board[r][c])
                dfs(r, c-1, trie[board[r][c]], substr+board[r][c])
                dfs(r, c+1, trie[board[r][c]], substr+board[r][c])
                visited.remove((r, c))
            
        visited = set()
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, t.trie, '')
                
        return found