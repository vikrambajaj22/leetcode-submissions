class Solution(object):
    def hasDuplicates(self, num_list):
        ''' checks if a list of number strings has duplicates (not counting the '.' char) '''
        num_list = [n for n in num_list if n != '.']
        return len(set(num_list)) != len(num_list)


    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        valid = ['.'] + [str(n) for n in range(1, 10)]
        
        # checking for duplicates in rows
        for i in range(len(board)):
            if not self.hasDuplicates(board[i]):
                # no duplicates in row
                continue
            else:
                return False
            
        # checking for duplicates in columns
        for i in range(len(board[0])):
            col = []
            for j in range(len(board)):
                col.append(board[j][i])
            if not self.hasDuplicates(col):
                continue
            else:
                return False
            
        # checking if squares are valid (no duplicates)
        for m in (0, 3, 6):
            for n in (0, 3, 6):
                square = []
                for i in range(m, m+3):
                    for j in range(n, n+3):
                        square.append(board[i][j])
                if not self.hasDuplicates(square):
                    continue
                else:
                    return False
                
        return True