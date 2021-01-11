# 1202. 交换字符串中的元素
# 给你一个字符串s，以及该字符串中的一些「索引对」数组pairs，其中pairs[i] = [a, b]表示字符串中的两个索引（编号从0开始）。
# 你可以任意多次交换在pairs中任意一对索引处的字符。返回在经过若干次交换后，s可以变成的按字典序最小的字符串。
# 示例1:
# 输入：s = "dcab", pairs = [[0, 3], [1, 2]]
# 输出："bacd"
# 解释：交换s[0]和s[3], s = "bcad"交换s[1]和s[2], s = "bacd"

# 示例2：
# 输入：s = "dcab", pairs = [[0, 3], [1, 2], [0, 2]]
# 输出："abcd"
# 解释：交换s[0]和s[3], s = "bcad"交换s[0]和s[2], s = "acbd"交换s[1]和s[2], s = "abcd"
#
# 示例3：
# 输入：s = "cba", pairs = [[0, 1], [1, 2]]
# 输出："abc"
# 解释：交换s[0]和s[1], s = "bca"交换s[1]和s[2], s = "bac"交换s[0]和s[1], s = "abc"
# 提示：
# 1 <= s.length <= 10 ^ 5
# 0 <= pairs.length <= 10 ^ 5
# 0 <= pairs[i][0], pairs[i][1] < s.length
# s中只含有小写英文字母
from collections import defaultdict


def smallestStringWithSwaps(s, pairs):  # 不知道合并的地方哪里错了
    """
    :type s: str
    :type pairs: List[List[int]]
    :rtype: str
    """
    fa = [i for i in range(len(s))]

    def findf(x ,fa):
        if fa[x] == x:
            return x
        else:
            fa[x] = findf(fa[x], fa)
            return fa[x]

    def merge(x, y, fa):
        fx, fy = findf(x, fa), findf(y, fa)
        if fx != fy:
            fa[fx] = fy

    r = ['*' for _ in range(len(s))]
    d = {}
    for p in pairs:
        merge(p[0], p[1], fa)
    print(fa)
    for i in range(len(s)):
        if fa[i] not in d:
            d[fa[i]] = [(i, s[i])]
        else:
            d[fa[i]].append((i, s[i]))
    print(d)
    for k in d:
        d1 = sorted(d[k], key=lambda x: x[1])
        d2 = sorted(d[k], key=lambda x: x[0])
        # print(d1)
        # print(d2)
        for i in range(len(d1)):
            r[d2[i][0]] = d1[i][1]

    res = ''
    res = res.join(r)
    return res

s = "dcab"
pairs = [[0,3],[1,2],[0,2]]
# pairs = [[0,3],[1,2]]
smallestStringWithSwaps(s, pairs)


# def find(u, parents):
#     # 路径压缩
#     if parents[u] == u:
#         return u
#     parents[u] = find(parents[u], parents)
#     return parents[u]
# def union(u, v, ranks, parents):
#     # 按秩合并
#     pu, pv = find(u, parents), find(v, parents)
#     if pu == pv:
#         return False
#     ru, rv = ranks[u], ranks[v]
#     if ru > rv:
#         parents[pv] = pu
#     elif rv > ru:
#         parents[pu] = pv
#     else:
#         parents[pv] = pu
#         ranks[pu] += 1
#     return True

# class Solution:
#     def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
#         parents = [i for i in range(len(s))]
#         ranks = [0] * len(s)
#
#         for u, v in pairs:
#             union(u, v, ranks, parents)  # 合并
#
#         groups = {} # 存放各个集合下的元素，key为集合代表，value为26个字母的列表
#         for i in range(len(s)):
#             groups.setdefault(find(i, parents), [0]*26)[ord(s[i])-ord('a')] += 1
#
#         res = [None] * len(s)
#         for index, boss in enumerate(parents):
#             for i in range(26):
#                 if groups[boss][i] > 0:
#                     tmp = chr(i+97)
#                     res[index] = tmp         # 填值
#                     groups[boss][i] -= 1
#                     break
#
#         return "".join(res)
#
# 作者：zhou-pen-cheng
# 链接：https://leetcode-cn.com/problems/smallest-string-with-swaps/solution/bing-cha-ji-ji-shu-pai-xu-he-bing-cha-xu-8gd8/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
