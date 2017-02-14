"""
    228 - Summary Ranges
    @author oneshan
    @version 1.0 2/13/2017
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        ans = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start != nums[i - 1]:
                    ans.append("%d->%d" % (start, nums[i - 1]))
                else:
                    ans.append(str(start))
                start = nums[i]

        if start != nums[-1]:
            ans.append("%d->%d" % (start, nums[-1]))
        else:
            ans.append(str(start))

        return ans
