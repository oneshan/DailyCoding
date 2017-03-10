class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n1, n2, n3 = None, None, None
        for num in nums:
            # ignore duplicate integer
            if num in (n1, n2, n3):
                continue

            if n1 is None or num > n1:
                n1, n2, n3 = num, n1, n2
            elif n2 is None or num > n2:
                n2, n3 = num, n2
            elif n3 is None or num > n3:
                n3 = num

        # return the maximum if the third maximum does not exist
        if n3 is None:
            return n1

        return n3
