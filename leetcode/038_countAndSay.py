"""
    038 - Count and Say
    @author oneshan
    @version 1.0 2/26/2017
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = "1"
        for i in range(n - 1):
            temp, count, pre = "", 0, ans[0]
            for ch in ans:
                if ch == pre:
                    count += 1
                else:
                    temp += str(count) + pre
                    pre = ch
                    count = 1
            if count:
                temp += str(count) + pre
            ans = temp

        return ans
