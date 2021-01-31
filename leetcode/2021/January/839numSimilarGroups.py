# 839. 相似字符串组
# 如果交换字符串X中的两个不同位置的字母，使得它和字符串Y相等，那么称X和Y两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。
# 例如，"tars"和"rats"是相似的(交换 0与2的位置)； "rats"和"arts"也是相似的，但是"star"不与"tars"，"rats"，或"arts"相似。
# 总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"}和{"star"}。注意，"tars"和 "arts"
# 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。
# 给你一个字符串列表strs。列表中的每个字符串都是 strs中其它所有字符串的一个字母异位词。请问strs中有多少个相似字符串组？
# 示例1：
# 输入：strs = ["tars", "rats", "arts", "star"]
# 输出：2
#
# 示例2：
# 输入：strs = ["omv", "ovm"]
# 输出：1

# 提示：
# 1 <= strs.length <= 100
# 1 <= strs[i].length <= 1000
# sum(strs[i].length) <= 2 * 104
# strs[i]只包含小写字母。
# strs中的所有单词都具有相同的长度，且是彼此的字母异位词。
# 备注：
# 字母异位词（anagram），一种把某个字符串的字母的位置（顺序）加以改换所形成的新词。

class Solution(object):  # 被周赛虐死，每日的并查集模板题好歹还是写出来了
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        def find(x):
            if x == f[x]:
                return x
            f[x] = find(f[x])
            return f[x]

        def union(x, y):
            fx, fy = find(x), find(y)
            if fx != fy:
                f[fx] = fy

        def isSimilar(s1, s2):
            if s1 == s2:
                return True
            c1 = []
            c2 = []
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    c1.append(s1[i])
                    c2.append(s2[i])
                    if len(c1) > 2:
                        return False
            if len(c1) == 2 and c1[0] == c2[1] and c1[1] == c2[0]:
                return True
            return False

        n = len(strs)
        f = [i for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if isSimilar(strs[i], strs[j]):
                    union(i, j)
        res = 0
        for i in range(n):
            if i == f[i]:
                res += 1
        return res



