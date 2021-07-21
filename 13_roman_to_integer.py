class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # replace double roman characters
        replacements = {'IV': 'a', 'IX': 'b',
                        'XL': 'c', 'XC': 'd', 'CD': 'e', 'CM': 'f'}

        int_val = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'a': 4, 'b': 9, 'c': 40, 'd': 90, 'e': 400, 'f': 900
        }

        for r in replacements:
            s = s.replace(r, replacements[r])

        s = list(s)  # split into characters
        value = sum(int_val[x] for x in s)

        return value
