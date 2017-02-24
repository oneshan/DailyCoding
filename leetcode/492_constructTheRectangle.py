"""
    492 - Construct the Rectangle
    @author oneshan
    @version 1.0 2/23/2017
"""


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        for W in range(int(math.sqrt(area)), 0, -1):
            if area % W == 0:
                return [area / W, W]
