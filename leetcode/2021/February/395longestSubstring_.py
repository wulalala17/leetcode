# 395. 至少有K个重复字符的最长子串
# 给你一个字符串s和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。
#
# 示例1：
# 输入：s = "aaabb", k = 3
# 输出：3
# 解释：最长子串为"aaa" ，其中'a'重复了3 次。
#
# 示例2：
# 输入：s = "ababbc", k = 2
# 输出：5
# 解释：最长子串为"ababb" ，其中'a'重复了 2次， 'b'重复了3次。
#
# 提示：
# 1 <= s.length <= 104
# s仅由小写英文字母组成 1 <= k <= 105

class Solution:  # 看了题解才知道分治要这么写
    def longestSubstring(self, s: str, k: int) -> int:
        def dfs(s, l, r, k):
            cha = [0 for i in range(26)]
            for i in range(l, r + 1):
                cha[ord(s[i]) - 97] += 1
            split = '-'
            for i in range(26):
                if cha[i] > 0 and cha[i] < k:
                    split = chr(i + 97)
                    break
            if split == '-':
                return r - l + 1
            i = l
            res = 0
            while i <= r:
                while i <= r and s[i] == split:
                    i += 1
                if i > r:
                    break
                start = i
                while i <= r and s[i] != split:
                    i += 1
                le = dfs(s, start, i - 1, k)
                res = max(res, le)
            return res

        return dfs(s, 0, len(s) - 1, k)


# class Solution(object):  # 自己想当然的写法，不行的
#     def longestSubstring(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: int
#         """
#         def isTrue(words):
#             dic = {}
#             for w in words:
#                 if w not in dic:
#                     dic[w] = 1
#                 else:
#                     dic[w] += 1
#             re = sorted(dic.items(), key = lambda x: x[1])
#             if len(re) == 0:
#                 return False
#             if re[0][1] < k:
#                 return False
#             else:
#                 return True
#         d = {}
#         a = {}
#         for w in s:
#             if w not in d:
#                 d[w] = 1
#             else:
#                 d[w] += 1
#         for key in d:
#             if d[key] >=k:
#                 a[key] = 1
#         res = 0
#         i, j = 0, 0
#         while j < len(s):
#             if s[j] not in a:
#                 if i == j:
#                     i += 1
#                     j += 1
#                     continue
#                 else:
#                     if isTrue(s[i:j]):
#                         res = max(res, j-i)
#                     j += 1
#             else:
#                 j += 1
#                 if isTrue(s[i:j]):
#                     res = max(res, j-i)
#         return res