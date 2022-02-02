class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0  # no primes before 2

        # is_prime[i]=1 if i is prime (initially setting all numbers as prime)
        is_prime = [1] * n
        is_prime[0] = is_prime[1] = 0  # 0 and 1 are not prime

        for i in range(2, int(math.sqrt(n))+1):
            # if i is prime, set all multiples after i^2 till n to 0
            # note: we only need to loop till sqrt(n) above because we need to update non-primes from i^2 to n
            # and i^2 would be greater than n if i > sqrt(n)
            if is_prime[i] == 1:
                for m in range(i*i, n, i):
                    is_prime[m] = 0

        return sum(is_prime)
