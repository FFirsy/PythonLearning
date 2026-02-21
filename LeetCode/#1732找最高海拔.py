# class Solution(object):
#     def largestAltitude(self, gain):
#         """
#         :type gain: List[int]
#         :rtype: int
#         """
#         t = 0
#         max = 0
#         for i in range(len(gain)):
#             t = gain[i] + t
#             if max < t:
#                 max = t
#                 continue
#         return max


# def update_height(current, delta):
#     return current + delta
#
# class Solution(object):
#     def largestAltitude(self, gain):
#         h = 0
#         mh = 0
#         for delta in gain:
#             h = update_height(h,delta)
#             if mh < h:
#                 mh = h
#         return mh

class Solution(object):
    def largestAltitude(self, gain):
        current  = 0
        max_value = 0
        for v in gain:
            current += v
            max_value = max(max_value, current)
        return max_value