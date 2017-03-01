"""
    122 - Best Time to Buy and Sell Stock II
    @author oneshan
    @version 1.0 2/28/2017
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        totalProfit = 0
        minV = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > minV:
                totalProfit += prices[i] - minV
            minV = prices[i]

        return totalProfit
