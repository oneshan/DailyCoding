"""
    605 - Can Place Flowers
    @author oneshan
    @version 1.0 6/4/2017
"""


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        total, count = 0, 1
        for flower in flowerbed:
            if flower and count:
                total += (count - 1) >> 1
                count = 0
            else:
                count += 1
        if count:
            total += count >> 1
        return total >= n
