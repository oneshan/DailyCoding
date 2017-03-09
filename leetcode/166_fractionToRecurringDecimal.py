"""
    166 - Fraction to Recurring Decimal
    @author oneshan
    @version 1.0 3/8/2017
"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        # Note: -50 / 8 = -6.25
        isNeg = (numerator * denominator) < 0
        numerator = abs(numerator)
        denominator = abs(denominator)

        q = numerator / denominator
        r = numerator % denominator

        # Case 1 -- without fractional part
        if r == 0:
            return ('', '-')[isNeg] + str(q)

        ans = [str(q), '.']
        table = {}
        idx = len(ans)

        while True:
            # Case 2 -- the fractional part does not repeat
            if r == 0:
                break

            r *= 10
            q = r / denominator

            # Case 3 -- the fractional part is repeating
            if r in table:
                ans.insert(table[r], '(')
                ans.append(')')
                break

            ans.append(str(q))
            table[r] = idx
            idx += 1
            r = r % denominator

        return ('', '-')[isNeg] + "".join(ans)
