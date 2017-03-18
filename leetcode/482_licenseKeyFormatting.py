"""
    482 - License Key Formatting
    @author oneshan
    @version 1.0 3/17/2017
"""


class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-', '')
        rb = (len(S) - 1) % K + 1
        chunk = [S[:rb]] + [S[i:i + K] for i in range(rb, len(S), K)]
        return "-".join(chunk)
