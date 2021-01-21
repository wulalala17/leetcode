# 1489.找到最小生成树里的关键边和伪关键边
# 给你一个n个点的带权无向连通图，节点编号为0到 n - 1 ，同时还有一个数组edges ，其中edges[i] = [fromi, toi, weighti]表示在fromi和toi
# 节点之间有一条带权无向边。最小生成树(MST)是给定图中边的一个子集，它连接了所有节点且没有环，而且这些边的权值和最小。
# 请你找到给定图中最小生成树的所有关键边和伪关键边。如果从图中删去某条边，会导致最小生成树的权值和增加，那么我们就说它是一条关键边。伪关键边则是可能会出现在某些最小生成树中但不会出现在所有最小生成树中的边。
# 请注意，你可以分别以任意顺序返回关键边的下标和伪关键边的下标。

# 示例1：
# 输入：n = 5, edges = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]
# 输出：[[0, 1], [2, 3, 4, 5]]
# 解释：上图描述了给定图。下图是所有的最小生成树。
# 注意到第0条边和第1条边出现在了所有最小生成树中，所以它们是关键边，我们将这两个下标作为输出的第一个列表。
# 边2，3，4和5是所有MST的剩余边，所以它们是伪关键边。我们将它们作为输出的第二个列表。
#
# 示例2 ：
# 输入：n = 4, edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]
# 输出：[[], [0, 1, 2, 3]]
# 解释：可以观察到4条边都有相同的权值，任选它们中的3条可以形成一棵MST 。所以4条边都是伪关键边。

# 提示：
# 2 <= n <= 100
# 1 <= edges.length <= min(200, n * (n - 1) / 2)
# edges[i].length == 3
# 0 <= fromi < toi < n
# 1 <= weighti <= 1000
# 所有(fromi, toi) 数对都是互不相同的。

class Solution(object):  # 看到图加并查集光速放弃
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        parent = list(range(n))

        def find(index):
            if index != parent[index]:
                parent[index] = find(parent[index])
            return parent[index]

        def union(index1, index2):
            parent[index2] = index1

        # 这里由小到大排序 就是 Kruskal 的思想
        # 在原有的edge中添加位置索引，方便排序后能得到在原edges中的位置
        sorted_edges = [[index] + i for index, i in enumerate(edges)]
        # 根据 weight 对边进行排序
        sorted_edges = sorted(sorted_edges, key=lambda x: x[-1])

        # 计算最小生成树的权值和 total
        total = 0
        for index, (_, x, y, w) in enumerate(sorted_edges):
            rx, ry = find(x), find(y)
            if rx != ry:
                union(rx, ry)
                total += w

        # 接下来 进行 最小生成树的构造 分为两种情况：
        # 1.先连接当前边，得到所有连通边的权值和 tmp_total1
        # 2.去掉当前边，得到所有连通边的权值和 tmp_total2
        #
        # 然后 total 、tmp_total1、 tmp_total2 进行比较
        # 若 total与tmp_total1 相等，则代表 该边为有效边， 否则为无效边直接跳过
        # 然后若 tmp_total1不等于tmp_total2，则代表该边为 关键边， 否则为 防关键边

        key_edge = []  # 关键边列表
        no_key_edge = []  # 非关键边列表
        for i, edge in enumerate(sorted_edges):
            (_, cx, cy, cw) = edge
            # 去掉当前边, 形成新的边列表
            tmp_edges = sorted_edges[:i] + sorted_edges[i + 1:]

            # 1.先连接当前边，得到连通边的权值和 tmp_total1
            total1 = cw
            parent = list(range(n))
            union(cx, cy)
            for index, (_, x, y, w) in enumerate(tmp_edges):
                rx, ry = find(x), find(y)
                if rx != ry:
                    union(rx, ry)
                    total1 += w

            # 2.去掉当前边，得到连通边的权值和 tmp_total2
            total2 = 0
            parent = list(range(n))
            for index, (_, x, y, w) in enumerate(tmp_edges):
                rx, ry = find(x), find(y)
                if rx != ry:
                    union(rx, ry)
                    total2 += w

            # 然后 total 、total1、 total2 进行比较
            # 若 total与total1 相等，则代表 该边为有效边， 否则为无效边直接跳过
            # 然后若 total1不等于total2，则代表该边为 关键边， 否则为 伪关键边
            if total1 == total:
                if total1 != total2:
                    key_edge.append(edge[0])
                else:
                    no_key_edge.append(edge[0])

        return [key_edge, no_key_edge]

# 作者：SmileTM
# 链接：https: // leetcode - cn.com / problems / find - critical - and -pseudo - critical - edges - in -minimum - spanning - tree / solution / python3 - kruskalbing - cha - ji - by - smiletm - jt9y /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。