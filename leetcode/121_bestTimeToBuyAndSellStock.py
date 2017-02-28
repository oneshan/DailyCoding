"""
    121 - Best Time to Buy and Sell Stock
    @author oneshan
    @version 1.0 2/27/2017
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        minV = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            if prices[i] > minV:
                maxProfit = max(maxProfit, prices[i] - minV)
            else:
                minV = prices[i]

        return maxProfit
