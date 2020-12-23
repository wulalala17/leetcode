# 387.字符串中的第一个唯一字符
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 - 1。
# 示例：
# s = "leetcode"  返回0
# s = "loveleetcode" 返回2
#
# 提示：你可以假定该字符串只包含小写字母。

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for c in s:
            if not c in d:
                d[c] = 1
            else:
                d[c] += 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1

# class Solution:  # 官方题解的代码，同一个思想，用Counter和enumerate更优雅
#     def firstUniqChar(self, s: str) -> int:
#         frequency = collections.Counter(s)
#         for i, ch in enumerate(s):
#             if frequency[ch] == 1:
#                 return i
#         return -1
#
# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string/solution/zi-fu-chuan-zhong-de-di-yi-ge-wei-yi-zi-x9rok/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。