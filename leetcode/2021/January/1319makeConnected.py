# 1319. 连通网络的操作次数
# 用以太网线缆将n台计算机连接成一个网络，计算机的编号从0到n - 1。线缆用connections表示，其中connections[i] = [a, b]连接了计算机a和b。
# 网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。
# 给你这个计算机网络的初始布线connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。
# 请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 - 1 。
#
# 示例1：
# 输入：n = 4, connections = [[0, 1], [0, 2], [1, 2]]
# 输出：1
# 解释：拔下计算机1和2之间的线缆，并将它插到计算机1和3上。
#
# 示例2：
# 输入：n = 6, connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
# 输出：2
#
# 示例3
# 输入：n = 6, connections = [[0, 1], [0, 2], [0, 3], [1, 2]]
# 输出：-1
# 解释：线缆数量不足。
#
# 示例4：
# 输入：n = 5, connections = [[0, 1], [0, 2], [3, 4], [2, 3]]
# 输出：0
#
# 提示：
# 1 <= n <= 10 ^ 5
# 1 <= connections.length <= min(n * (n - 1) / 2, 10 ^ 5)
# connections[i].length == 2
# 0 <= connections[i][0], connections[i][1] < n
# connections[i][0] != connections[i][1]
# 没有重复的连接。
# 两台计算机不会通过多条线缆连接。

class Solution(object):  # 并查集入门题，用python写，难得一次时间超过100%
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        l = len(connections)
        if l < n - 1:
            return -1
        f = [i for i in range(n)]

        def find(x):
            if x == f[x]:
                return x
            f[x] = find(f[x])
            return f[x]

        def union(x1, x2):
            y1, y2 = find(x1), find(x2)
            if y1 != y2:
                f[y1] = y2

        res = 0
        for c in connections:
            union(c[0], c[1])
        for i in range(n):
            if f[i] == i:
                res += 1
        return res - 1


