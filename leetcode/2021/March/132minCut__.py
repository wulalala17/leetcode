# 132. 分割回文串 II
#  给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。 返回符合要求的 最少分割次数 。
#  示例 1：
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成["aa", "b"] 这样两个回文子串。
#
# 示例 2：
# 输入：s = "a"
# 输出：0
#
# 示例 3：
# 输入：s = "ab"
# 输出：1
#
# 提示：
# 1 <= s.length <= 2000
# s 仅由小写英文字母组成

class Solution(object):  # 昨天的回溯加上计数是肯定超时的
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 0
        if len(s) == 2:
            if s[0] != s[1]:
                return 1
            else:
                return 0
        def dfs(s):
            if len(s) == 0:
                return [[]]
            if len(s) == 1:
                return [[s]]
            res = []
            for i in range(1, len(s)+1):
                left = s[:i]
                right = s[i:]
                if left == left[::-1]:
                    r = dfs(right)
                    for i in range(len(r)):
                        res.append([left]+r[i])
            return res
        ans = dfs(s)
        res = len(s)
        for a in ans:
            if len(a) < res:
                res = len(a)
        return res - 1


# class Solution(object):  # 官方题解，DP
#     def minCut(self, s):
#     n = len(s)
#     g = [[True] * n for _ in range(n)]
#
#     for i in range(n - 1, -1, -1):
#         for j in range(i + 1, n):
#             g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]
#
#     f = [float("inf")] * n
#     for i in range(n):
#         if g[0][i]:
#             f[i] = 0
#         else:
#             for j in range(i):
#                 if g[j + 1][i]:
#                     f[i] = min(f[i], f[j] + 1)
#
#     return f[n - 1]
#
#
# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / palindrome - partitioning - ii / solution / fen - ge - hui - wen - chuan - ii - by - leetcode - solu - norx /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


