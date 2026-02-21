class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for num in count:
            if count[num] == 1:
                sum += num
        return sum
