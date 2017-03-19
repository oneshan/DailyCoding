class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        k = len(primes)
        p_list = [0] * k
        n_list = [primes[i] for i in range(k)]

        ugly = [0] * n
        ugly[0] = 1

        for i in range(1, n):
            ugly[i] = min(n_list)
            for j in range(k):
                if ugly[i] == n_list[j]:
                    p_list[j] += 1
                    n_list[j] = ugly[p_list[j]] * primes[j]

        return ugly[-1]
