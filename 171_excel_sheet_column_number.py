class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        letters = list(columnTitle)

        values = {k: i+1 for i, k in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}

        columnValue = 0

        i = len(letters) - 1

        while i >= 0:
            columnValue += 26**(len(letters)-1-i) * values[letters[i]]
            i -= 1

        # logic: AB = 26^1 * A + 26^0 * B = 28; ZY = 26^1 * Z + 26^0 * Y = 701
        # i.e. same as binary to decimal but base 26

        return columnValue
