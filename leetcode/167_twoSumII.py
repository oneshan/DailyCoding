"""
    167 - Two Sum II - Input Array is sorted
    @author oneshan
    @version 1.0 2/18/2017
"""


class Solution(object):
    """ Binary Search """
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers) - 1):
            value = target - numbers[i]
            left, right = i + 1, len(numbers) - 1
            while (left <= right):
                mid = (left + right + 1) / 2
                if numbers[mid] == value:
                    return [i + 1, mid + 1]
                if numbers[mid] < value:
                    left = mid + 1
                else:
                    right = mid - 1


class Solution_2(object):
    """ Dictionary """
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for i in range(len(numbers)):
            value = target - numbers[i]
            if value in table:
                return [table[value] + 1, i + 1]
            table[numbers[i]] = i


class Solution_3(object):
    """ Two pointer """
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            value = numbers[i] + numbers[j]
            if value == target:
                return [i + 1, j + 1]
            elif value > target:
                j -= 1
            else:
                i += 1
