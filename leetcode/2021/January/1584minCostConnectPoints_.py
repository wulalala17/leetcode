# 1584.连接所有点的最小费用
# 给你一个points数组，表示2D平面上的一些点，其中points[i] = [xi, yi] 。
# 连接点[xi, yi]和点[xj, yj]的费用为它们之间的曼哈顿距离 ： | xi - xj | + | yi - yj | ，其中 | val | 表示val的绝对值。
# 请你返回将所有点连接的最小总费用。只有任意两点之间有且仅有一条简单路径时，才认为所有点都已连接。
# 示例1：
# 输入：points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
# 输出：20
# 解释：我们可以按照上图所示连接所有点得到最小总费用，总费用为20 。注意到任意两个点之间只有唯一一条路径互相到达。
#
# 示例2：
# 输入：points = [[3, 12], [-2, 5], [-4, 1]]
# 输出：18
#
# 示例3：
# 输入：points = [[0, 0], [1, 1], [1, 0], [-1, 1]]
# 输出：4
#
# 示例4：
# 输入：points = [[-1000000, -1000000], [1000000, 1000000]]
# 输出：4000000
#
# 示例5：
# 输入：points = [[0, 0]]
# 输出：0
#
# 提示：
# 1 <= points.length <= 1000
# -106 <= xi, yi <= 106
# 所有点(xi, yi)两两不同。


def minCostConnectPoints(points):  # Kruskal算法，已经忘了
    """
    :type points: List[List[int]]
    :rtype: int
    """
    n = len(points)
    if n <= 1:
        return 0
    dist = []  # 两个点之间的距离
    edges, res = 0, 0  # 边数 结果
    f = [i for i in range(n)]  # 并查集数组
    for i in range(n):
        for j in range(i + 1, n):
            dist.append([i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])])
    dist.sort(key=lambda x: x[2])

    def find(x):
        if f[x] != x:
            f[x] = find(f[x])
        return f[x]

    for i in range(len(dist)):
        a, b = find(dist[i][0]), find(dist[i][1])
        if a != b:
            f[b] = a
            res += dist[i][2]
            edges += 1
        if edges == n - 1:
            break
    return res

# https://leetcode-cn.com/problems/min-cost-to-connect-all-points/solution/python3-kruskalshi-xian-zui-xiao-sheng-c-5qvx/
p = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(minCostConnectPoints(p))
