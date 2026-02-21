# class Solution(object):
#     def runningSum(self, nums):
#         RunningSum = []
#         for i in range(len(nums)):
#             if(i == 0):
#                 RunningSum.append(nums[i])
#             else:
#                 t = nums[i] + RunningSum[i-1]
#                 RunningSum.append(t)
#         return RunningSum
#
# class Solution(object):
#     def runningSum(self, nums):
#         RunningSum = nums[:]
#         for i in range(1,len(nums)):
#             RunningSum[i] = RunningSum[i]+RunningSum[i-1]
#         return RunningSum

# def update_sum(current, delta):
#     return current + delta
#
# class Solution(object):
#     def runningSum(self, nums):
#         s = 0
#         ans = []
#         for delta in range(len(nums)):
#             s = update_sum(s,nums[delta])
#             ans.append(s)
#         return ans

class Solution(object):
    def runningSum(self, nums):
        s = 0
        ans = []
        for v in nums:
            s += v
            ans.append(s)
        return ans
