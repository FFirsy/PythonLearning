def count_even_n(n):
    count = 0
    while n > 0 :
        n = n // 10
        count += 1
    return count %2 == 0

def count_odd_n(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count %2 == 1


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        for v in nums:
            if count_even_n(v):
                n += 1
        return n