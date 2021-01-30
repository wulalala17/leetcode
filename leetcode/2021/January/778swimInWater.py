# 778. 水位上升的泳池中游泳
# 在一个NxN的坐标方格grid中，每一个方格的值grid[i][j]表示在位置(i, j)的平台高度。
# 现在开始下雨了。当时间为t时，此时雨水导致水池中任意位置的水位为t。
# 你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。
# 当然，在你游泳的时候你必须待在坐标方格里面。你从坐标方格的左上平台(0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台(N - 1, N - 1)？
# 示例1:
# 输入: [[0, 2], [1, 3]]
# 输出: 3
# 解释:时间为0时，你位于坐标方格的位置为(0, 0)。此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为0时的水位。
# 等时间到达3时，你才可以游向平台(1, 1).因为此时的水位是3，坐标方格中的平台没有比水位3更高的，所以你可以游向坐标方格中的任意位置
#
# 示例2:
# 输入: [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
# 输出: 16
# 解释:最终的路线用加粗进行了标记。我们必须等到时间为16，此时才能保证平台(0, 0)和(4, 4)是连通的
#
# 提示:
# 2 <= N <= 50.
# grid[i][j]是[0, ..., N * N - 1]的排列。

class Solution(object):  # 改了昨天的代码，把节点间的距离变成两个点的最大值（雨水能覆盖）
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def find(x):
            if f[x] == x:
                return x
            f[x] = find(f[x])
            return f[x]

        def union(x, y):
            fx, fy = find(x), find(y)
            if fx != fy:
                f[fx] = fy

        def isValid(x, y):
            if 0 <= x < m and 0 <= y < n:
                return True
            return False

        n, m = len(grid[0]), len(grid)  # 列数，行数
        f = [i for i in range(n * m)]
        edges = []
        for i in range(m):
            for j in range(n):
                nx, ny = i + 1, j
                if isValid(nx, ny):
                    d = max(grid[i][j], grid[nx][ny])
                    edges.append((i * n + j, nx * n + ny, d))
                nx, ny = i, j + 1
                if isValid(nx, ny):
                    d = max(grid[i][j], grid[nx][ny])
                    edges.append((i * n + j, nx * n + ny, d))
        edges.sort(key=lambda x: x[2])
        cost = 0
        for e in edges:
            if find(0) == find(n * m - 1):
                break
            x, y, d = e
            if find(x) != find(y):
                union(x, y)
                cost = max(cost, d)
        return cost

