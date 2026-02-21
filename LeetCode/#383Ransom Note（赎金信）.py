class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count = {}

        # 1. 统计 magazine 中的字母状态
        for char in magazine:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        # 2. 消耗 ransomNote 中的字母
        for char in ransomNote:
            if char in count and count[char] > 0:
                count[char] -= 1

            #    如果某个字母不够，立刻 return False
            else:
                return False
        return True