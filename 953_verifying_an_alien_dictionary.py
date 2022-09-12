class Solution(object):
    def encode(self, word, dictionary):
        encoding = []
        for ch in word:
            encoding.append(dictionary[ch])
            
        return encoding
        
        
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dictionary = {ch: i for i, ch in enumerate(order)}
        encoded_words = [(word, self.encode(word, dictionary)) for word in words]
        encoded_words = sorted(encoded_words, key=lambda w:w[1])
        
        return words == [w[0] for w in encoded_words]