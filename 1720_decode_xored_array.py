class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        # if a ^ b = c, then b = a ^ c (commutative)
        arr = [first]
        for num in encoded:
            arr.append(arr[-1] ^ num)

        return arr
