"""
    412 - Fizz Buzz
    @author oneshan
    @version 1.0 2/23/2017
"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []

        ans = map(str, range(1, n + 1))

        idx = 2
        while idx < n:
            ans[idx] = "Fizz"
            idx += 3

        idx = 4
        while idx < n:
            ans[idx] = "Buzz"
            idx += 5

        idx = 14
        while idx < n:
            ans[idx] = "FizzBuzz"
            idx += 15

        return ans


class Solution_2(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ["Fizz" * (i % 3 == 0) + "Buzz" * (i % 3 == 0) or str(i)
                for i in range(1, n + 1)]
