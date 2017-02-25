class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def distance(p1, p2):
            return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])

        ans = 0
        for p1 in points:
            table = {}
            for p2 in points:
                dist = distance(p1, p2)
                table[dist] = 1 + table.get(dist, 0)
            for key in table:
                ans += table[key] * (table[key] - 1)
        return ans
