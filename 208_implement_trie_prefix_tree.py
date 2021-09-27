class Trie(object):

    def __init__(self):
        self.trie = {}

    def insert(self, word):
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
        t = self.trie
        for ch in word:
            if ch not in t:
                return False
            t = t[ch]

        return 'is_end' in t

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        t = self.trie
        for ch in prefix:
            if ch not in t:
                return False
            t = t[ch]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
