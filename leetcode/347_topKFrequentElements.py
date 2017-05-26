"""
    347 - Top K Frequent Elements
    @author oneshan
    @version 1.0 5/25/2017
"""
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        table = {}
        for num in nums:
            table[num] = table.get(num, 0) + 1

        heap = [(-value, key) for key, value in table.items()]
        topk = heapq.nsmallest(k, heap)
        return [key for value, key in topk]
