# 1631. 最小体力消耗路径
# 你准备参加一场远足活动。给你一个二维rowsxcolumns的地图heights ，其中heights[row][col]表示格子(row, col)的高度。
# 一开始你在最左上角的格子(0, 0) ，且你希望去最右下角的格子(rows - 1, columns - 1) （注意下标从0开始编号）。
# 你每次可以往上，下，左，右四个方向之一移动，你想要找到耗费体力最小的一条路径。
# 一条路径耗费的体力值是路径上相邻格子之间高度差绝对值的 最大值决定的。
# 请你返回从左上角走到右下角的最小体力消耗值 。
# 示例1：
# 输入：heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
# 输出：2
# 解释：路径[1, 3, 5, 3, 5]连续格子的差值绝对值最大为2 。
# 这条路径比路径[1, 2, 2, 2, 5]更优，因为另一条路径差值最大值为3 。
#
# 示例2：
#
# 输入：heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
# 输出：1
# 解释：路径[1, 2, 3, 4, 5]的相邻格子差值绝对值最大为1 ，比路径[1, 3, 5, 3, 5]更优。
#
# 示例3：
# 输入：heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
# 输出：0
# 解释：上图所示路径不需要消耗任何体力。
#
#
#
# 提示：
# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 106

class Solution(object):  # 想了半天发现不是dp，看了评论才知道可以并查集
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
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

        n, m = len(heights[0]), len(heights)  # 列数，行数
        f = [i for i in range(n * m)]
        edges = []
        for i in range(m):
            for j in range(n):
                nx, ny = i + 1, j
                if isValid(nx, ny):
                    d = abs(heights[i][j] - heights[nx][ny])
                    edges.append((i * n + j, nx * n + ny, d))
                nx, ny = i, j + 1
                if isValid(nx, ny):
                    d = abs(heights[i][j] - heights[nx][ny])
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




