"""
    204 - Count Primes
    @author oneshan
    @version 1.0 2/5/2017
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        isPrime = [1 for _ in range(n)]
        isPrime[0] = 0
        isPrime[1] = 0

        for i in range(2, n):
            if not isPrime[i]:
                continue
            multiple = 2
            while (i * multiple < n):
                isPrime[i * multiple] = 0
                multiple += 1

        return sum(isPrime)
