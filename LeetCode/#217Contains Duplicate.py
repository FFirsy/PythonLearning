# class Solution(object):
#     def containsDuplicate(self, nums):
#         if len(set(nums)) == len(nums):
#             return False
#         else:
#             return True

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()          # 状态：到目前为止见过的所有元素

        for v in nums:
            if v in seen:     # 状态判断
                return True  # 提前结束（结果已经确定）
            seen.add(v)       # 状态更新

        return False          # 循环结束仍无重复
