# 131. 分割回文串
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 返回 s 所有可能的分割方案。
#
# 示例:
# 输入: "aab"
# 输出:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

class Solution(object):  # 看了评论才知道怎么写的回溯
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]
        res = []
        for i in range(1,len(s)+1):
            left = s[:i]
            right = s[i:]
            if left == left[::-1]:
                r = self.partition(right)
                for i in range(len(r)):
                    res.append([left] + r[i])
        return res