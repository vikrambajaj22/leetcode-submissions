class Solution(object):
    def reverse(self, word):
        """
        reverses a word
        :param word: word to be reversed
        :return: reversed word
        """
        left = 0
        right = len(word) - 1

        word = list(word)  # convert to list since strings are immutable

        while left < right:
            temp = word[left]
            word[left] = word[right]
            word[right] = temp

            left += 1
            right -= 1

        return ''.join(word)

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')  # split at single space

        return ' '.join(self.reverse(word) for word in words)
