# 389.找不同
# 给定两个字符串s和t，它们只包含小写字母。字符串t由字符串s随机重排，然后在随机位置添加一个字母。请找出在t中被添加的字母。
# 示例1：
# 输入：s = "abcd", t = "abcde"
# 输出："e"
# 解释：'e'是那个被添加的字母。
# 示例2：
# 输入：s = "", t = "y"
# 输出："y"
# 示例3：
# 输入：s = "a", t = "aa"
# 输出："a"
# 示例4：
# 输入：s = "ae", t = "aea"
# 输出："a"
# 提示：
# 0 <= s.length <= 1000  t.length == s.length + 1
# s和t只包含小写字母
class Solution(object):  #
    def findTheDifference(self, s, t):  # 字典
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        for char in s:
            if not char in d:
                d[char] = 1
            else:
                d[char] += 1
        for char in t:
            if char not in d:
                return char
            else:
                d[char] -= 1
                if d[char] == -1:
                    return char


# 大佬们的优秀一行题解
# return (collections.Counter(t) - collections.Counter(s)).popitem()[0]
# return chr(reduce(xor, map(ord, s+t)))
# return chr(sum(map(ord, t)) - sum(map(ord, s)))  # Python 1行 ASCII 和之差