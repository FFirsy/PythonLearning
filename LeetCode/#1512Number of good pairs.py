# class Solution(object):
#     def numIdenticalPairs(self, nums):
#         a = 0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] == nums[j]:
#                     a += 1
#         return a


'''拆成函数格式'''
def add_result(result):
    return result + 1

def compare(a1,a2):
    return a1 == a2

class Solution(object):
    def numIdenticalPairs(self, nums):
        a = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if compare(nums[i],nums[j]):
                    a = add_result(a)
        return a

