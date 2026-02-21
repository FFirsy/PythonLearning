# def add_result(result,value):
#     result.append(value)
#
# class Solution(object):
#     def kidsWithCandies(self, candies, extra):
#         n = max(candies)
#         result = []
#         for v in candies:
#             add_result(result,v+extra >= n)
#         return result


def add_result(result,value):
    result.append(value)

class Solution(object):
    def kidsWithCandies(self, candies, extra):
        n = max(candies)
        reslut = []
        for v in candies:
            add_result(reslut,v+extra >= n)
        return reslut

