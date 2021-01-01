# 140. 单词拆分 II
# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
# 说明：
#     分隔时可以重复使用字典中的单词。
#     你可以假设字典中没有重复的单词。
# 示例 1：
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# 示例 2：
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
# 示例 3：
# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []


# def wordBreak(s, wordDict):  回溯 没写出来
#     def findFirst(s0, wordDict):
#         res = []
#         for i in range(len(s0)):
#             s1 = s0[:i]
#             if s1 in wordDict:
#                 res.append(i)
#         return res
#     realres = []
#     r = findFirst(s, wordDict)
#     realres.append(r)
#     while realres:
#         for re in realres:
#             for x in re:
#                 newr = findFirst(s[x+1:], wordDict)


#         n = len(s)
#         def backtrack(start):
#             ans = []
#             if start == n:
#                 ans.append('')
#             for i in range(start, n):
#                 if s[start:i + 1] in wordDict:
#                     if start == 0: temp = s[start:i + 1]
#                     else: temp = " " + s[start:i + 1]
#                     ps = backtrack(i + 1)
#                     for p in ps:
#                         ans.append(temp + p)
#             return ans
#         return backtrack(0)
#
# 作者：fe-lucifer
# 链接：https://leetcode-cn.com/problems/word-break-ii/solution/cong-hui-su-dao-di-qia-er-ji-ji-yi-hua-di-gui-140-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# def wordBreak(self, s: str, wordDict: List[str]) -> List[str]: 官方题解
#     @lru_cache(None)  缓存
#     def backtrack(index: int) -> List[List[str]]:
#         if index == len(s):
#             return [[]]
#         ans = list()
#         for i in range(index + 1, len(s) + 1):
#             word = s[index:i]
#             if word in wordSet:
#                 nextWordBreaks = backtrack(i)
#                 for nextWordBreak in nextWordBreaks:
#                     ans.append(nextWordBreak.copy() + [word])
#         return ans
#
#     wordSet = set(wordDict)
#     breakList = backtrack(0)
#     return [" ".join(words[::-1]) for words in breakList]
#
#
# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / word -
# break
# -ii / solution / dan - ci - chai - fen - ii - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


