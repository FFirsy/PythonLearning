class Solution(object):
    def buildArray(self, nums):
        ans = []
        for i in range(len(nums)):  #遍历所有下标 i
            ans.append(nums[nums[i]])
        return ans






