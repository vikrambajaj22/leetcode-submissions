class WordDictionary(object):

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        t = self.trie
        for ch in word:
            if ch not in t:
                t[ch] = {}
            t = t[ch]
        t['is_end'] = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.search_from(self.trie, word)
    
    
    def search_from(self, t, word):
        for i, ch in enumerate(word):
            if ch == '.':
                for k in t:
                    if k != 'is_end':
                        if self.search_from(t[k], word[i+1:]):
                            return True
                return False
            elif ch not in t:
                return False
            t = t[ch]
        
        return 'is_end' in t
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)