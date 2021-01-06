# 399.除法求值
# 给你一个变量对数组equations和一个实数值数组values作为已知条件，其中equations[i] = [Ai, Bi]和values[i]共同表示等式Ai / Bi = values[i] 。每个
# Ai或Bi是一个表示单个变量的字符串。另有一些以数组queries表示的问题，其中queries[j] = [Cj, Dj]表示第j个问题，请你根据已知条件找出Cj / Dj = ? 的结果作为答案。
# 返回所有问题的答案 。如果存在某个无法确定的答案，则用 - 1.0 替代这个答案。
# 注意：输入总是有效的。你可以假设除法运算中不会出现除数为0的情况，且不存在任何矛盾的结果。
#
# 示例1：
# 输入：equations = [["a", "b"], ["b", "c"]], values = [2.0, 3.0],
#       queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"],["x", "x"]]
# 输出：[6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
# 解释：
# 条件：a / b = 2.0, b / c = 3.0
# 问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# 结果：[6.0, 0.5, -1.0, 1.0, -1.0]
#
# 示例2：
# 输入：equations = [["a", "b"], ["b", "c"], ["bc", "cd"]], values = [1.5, 2.5, 5.0],
#       queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
# 输出：[3.75000, 0.40000, 5.00000, 0.20000]
#
# 示例3：
#
# 输入：equations = [["a", "b"]], values = [0.5], queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
# 输出：[0.50000, 2.00000, -1.00000, -1.00000]
#
# 提示：
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj由小写英文字母与数字组成
from collections import defaultdict


class Solution(object):  # 好难的中等题，知道要类似图的思路，但写不出来，直接看的题解
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph=defaultdict(dict)
        for (a,b),v in zip(equations,values):
            graph[a][b]=v
            graph[b][a]=1/v
        def dfs(s,e):
            if s not in graph or e not in graph:
                return -1
            if s==e:
                return 1
            visited.add(s)
            for i in graph[s]:
                if i==e:
                    return graph[s][i]
                if i not in visited:
                    ans=dfs(i,e)
                    if ans!=-1:
                        return graph[s][i]*ans
            return -1
        res=[]
        for a,b in queries:
            visited=set()
            res.append(dfs(a,b))
        return res