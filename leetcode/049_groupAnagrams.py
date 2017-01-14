"""
    49. Group Anagrams
    @author oneshan
    @version 1.0 1/13/2017
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictTable = {}
        for s in strs:
            key = "".join(sorted(s))
            dictTable[key] = [s] if key not in dictTable else dictTable[key] + [s]

        ans = []
        for key in dictTable:
            ans.append(dictTable[key])
        return ans
