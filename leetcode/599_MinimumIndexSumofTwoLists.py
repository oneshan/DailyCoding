"""
    599 - Minimum Index Sum of Two Lists
    @author oneshan
    @version 1.0 5/30/2017
"""


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        minSum, ans = float("inf"), []
        table = {}
        for idx, res in enumerate(list1):
            table[res] = idx
        for idx, res in enumerate(list2):
            if res not in table:
                continue
            idxSum = idx + table[res]
            if minSum > idxSum:
                minSum, ans = idxSum, [res]
            elif minSum == idxSum:
                ans.append(res)
        return ans
