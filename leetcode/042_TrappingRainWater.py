"""
    042 - Trapping Rain Water
    @author oneshan
    @version 1.0 6/27/2017
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0

        left, right, water = 0, 0, []

        for i in range(len(height)):
            left = max(left, height[i])
            water += left,

        for i in range(len(height) - 1, -1, -1):
            right = max(right, height[i])
            water[i] = min(water[i], right) - height[i]

        return sum(water)


class Solution_2(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
        i, j = 0, len(height) - 1
        l_max, r_max = height[i], height[j]
        ans = 0
        while i < j:
            if l_max <= r_max:
                ans += l_max - height[i]
                i += 1
                l_max = max(height[i], l_max)
            else:
                ans += r_max - height[j]
                j -= 1
                r_max = max(height[j], r_max)
        return ans
