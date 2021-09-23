class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # https://www.youtube.com/watch?v=KE5Axm7uzok
        reversed_bits = []  # stores bits in reversed order

        for _ in range(32):
            # by doing n & 1, we get the last bit of n
            reversed_bits.append(n & 1)
            # then, shift n 1 bit ahead to discard last bit
            n = n >> 1

        # combine reversed bits into result
        res = 0
        for bit in reversed_bits:
            # shift res one bit backward to make space for new bit
            res = res << 1
            # the | operation adds the new bit to res
            res = res | bit

        return res
