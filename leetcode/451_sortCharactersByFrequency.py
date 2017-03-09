"""
    451 - Sort Characters By Frequency
    @author oneshan
    @version 1.0 3/8/2017
"""


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = [0] * 256
        for ch in s:
            freq[ord(ch)] += 1

        ans = ""
        for i in range(256):
            maxIdx, maxFreq = 0, 0
            for j in range(1, 256):
                if freq[j] > maxFreq:
                    maxIdx, maxFreq = j, freq[j]
            ans += chr(maxIdx) * maxFreq
            freq[maxIdx] = 0
        return ans
