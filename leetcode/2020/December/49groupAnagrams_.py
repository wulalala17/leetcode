# 49. 字母异位词分组
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 示例:
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 说明：
#     所有输入均为小写字母。
#     不考虑答案输出的顺序。

import collections


class Solution(object):  # 倒数第二个用例超时了，想不出优化的方法
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def same(a, b):
            if len(a) != len(b):
                return False
            c1 = collections.Counter(a)
            c2 = collections.Counter(b)
            for c in a:
                if c1[c] != c2.get(c, 0):
                    return False
            return True
        res = []
        d = {}
        for s in strs:
            n = len(s)
            b = 0
            if d.get(n, -1) == -1:
                d[n] = []
                d[n].append([s])
                continue
            for r in d[n]:
                if same(r[0], s):
                    r.append(s)
                    b = 1
                    break
            if b == 0:
                d[n].append([s])
        for key in d:
            for k in d[key]:
                res.append(k)
        return res

    # class Solution:  # 看了评论后知道的排序写法
    #     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #         d = {}
    #         res = []
    #         for s in strs:
    #             sorted_s = "".join(sorted(s))
    #             if sorted_s not in d:
    #                 d[sorted_s] = [s]
    #             else:
    #                 d[sorted_s].append(s)
    #         for keys in d:
    #             res.append(d[keys])
    #         return res

