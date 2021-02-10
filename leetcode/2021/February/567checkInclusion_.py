# 567. 字符串的排列
# 给定两个字符串s1和s2，写一个函数来判断 s2 是否包含s1的排列。
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。
# 示例1:
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2包含s1的排列之一("ba").
#
# 示例2:
# 输入: s1 = "ab" s2 = "eidboaoo"
# 输出: False
#
# 注意：
# 输入的字符串只包含小写字母
# 两个字符串的长度都在[1, 10, 000]之间

class Solution(object):  # 看了评论才知道要这样写，之前硬用字典是不行的
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        if len(s1) == 1:
            if s1 in s2:
                return True
            else:
                return False
        d1 = [0 for i in range(26)]
        d2 = [0 for i in range(26)]
        n = len(s1)
        for i in range(n):
            d1[ord(s1[i]) - 97] += 1
            d2[ord(s2[i]) - 97] += 1
        for i in range(n, len(s2)):
            if d1 == d2:
                return True
            d2[ord(s2[i]) - 97] += 1
            d2[ord(s2[i-n]) - 97] -= 1
        return d1 == d2