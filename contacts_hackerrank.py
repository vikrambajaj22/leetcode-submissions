# https://www.hackerrank.com/challenges/contacts/problem
''' add words to a contact book and find the number of words that start with a given prefix '''


class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        ''' insert word into trie '''
        t = self.trie
        for ch in word:
            if ch not in t:
                t[ch] = {}
                # initialize count of words that start with this ch to 0
                t[ch]['count'] = 0
            t = t[ch]
            t['count'] += 1  # update count
        t['is_end'] = True

    def search(self, word):
        ''' return True if word exists in trie, False otherwise '''
        t = self.trie
        for ch in word:
            if ch not in t:
                return False
            t = t[ch]
        return 'is_end' in t

    def starts_with(self, prefix):
        ''' return count of words that start with prefix '''
        t = self.trie
        for ch in prefix:
            if ch not in t:
                return 0
            t = t[ch]
        return t['count']

    def __str__(self):
        ''' overwriting the print() action '''
        return '{}'.format(self.trie)


if __name__ == '__main__':
    t = Trie()
    t.insert('ed')
    t.insert('eddie')
    t.insert('edward')
    print(t)
    print(t.starts_with('ed'))  # 3
    t.insert('edwina')
    print(t.starts_with('edw'))  # 2
    print(t.starts_with('a'))  # 0
    print(t.search('edw'))  # False
    print(t.search('edward'))  # True
