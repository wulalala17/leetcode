# 765. 情侣牵手
# N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。 一次交换可选择任意两人，让他们站起来交换座位。
# 人和座位用 0 到 2N-1 的整数表示，情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2N-2, 2N-1)。
# 这些情侣的初始座位  row[i] 是由最初始坐在第 i 个座位上的人决定的。
#
# 示例 1:
# 输入: row = [0, 2, 1, 3]
# 输出: 1
# 解释: 我们只需要交换row[1]和row[2]的位置即可。
#
# 示例 2:
# 输入: row = [3, 2, 0, 1]
# 输出: 0
# 解释: 无需交换座位，所有的情侣都已经可以手牵手了。
#
# 说明:
#     len(row) 是偶数且数值在 [4, 60]范围内。
#     可以保证row 是序列 0...len(row)-1 的一个全排列。

class Solution(object):  # 暴力居然能过
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        res = 0
        for i in range(0, len(row), 2):
            p1 = row[i]
            if p1 % 2 == 0:
                p2 = p1 + 1
            else:
                p2 = p1 - 1
            if p2 != row[i+1]:
                p = row.index(p2)
                row[i+1], row[p] = row[p], row[i+1]
                res += 1
        return res


# class Solution:  # 并查集
#     def minSwapsCouples(self, row: List[int]) -> int:
#         # 好吧，并查集再爱我一次吧
#         # 思路，如果相邻的是一对，那么相邻的都隶属于一个结点，如果不属于一个节点，则说明需要交换，而且最终会形成一个连通域，那么这条连通域的节点数目就是最终需要交换的数目。
#         n = len(row)
#         uf = UnionFind(n // 2)
#         for i in range(0, n, 2):
#             # 如row[i]和row[i+1]是一对，则是一个孤立的结点，如0，1 or 3，2
#             # 如row[i]和row[i+1]不是一对， 则需要连通起来， 如0,3 or 1, 2
#             l1 = row[i] // 2
#             l2 = row[i + 1] // 2
#             uf.union(l1, l2)
#
#         return uf.count
#
#
# class UnionFind:
#     def __init__(self, n):
#         self.parent = [-1] * n
#         self.count = 0
#
#     def find(self, x):
#         root = x
#         while self.parent[root] != -1:
#             root = self.parent[root]
#
#         while x != root:
#             last = self.parent[x]
#             self.parent[x] = root
#             x = last
#
#         return root
#
#     def union(self, x, y):
#         p_x = self.find(x)
#         p_y = self.find(y)
#         if p_x != p_y:
#             self.parent[p_x] = p_y
#             self.count += 1


