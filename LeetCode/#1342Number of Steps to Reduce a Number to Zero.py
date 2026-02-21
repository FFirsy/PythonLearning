#class Solution(object):
#     def numberOfSteps(self, num):
#         i = 0
#         while num > 0:
#             if num % 2 == 0:
#                 num = num // 2
#                 i += 1
#             else:
#                 num -= 1
#                 i += 1
#         return i
#
#     def stepsTrace(num):
#         steps = 0
#         while num > 0:
#             print(num)
#             if num % 2 == 0:
#                 num //= 2
#             else:
#                 num -= 1
#             steps += 1
#         return steps
#
#

def next_step(value):
    if value % 2 == 0:
        return value // 2
    return value - 1

class Solution(object):
    def numberOfSteps(self, num):
        step = 0
        while num > 0:
            num = next_step(num)
            step += 1
        return step
