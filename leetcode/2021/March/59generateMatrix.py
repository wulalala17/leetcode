# 59. 螺旋矩阵 II
# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
# 示例 1：
# 输入：n = 3
# 输出：[[1, 2, 3], [8, 9, 4], [7, 6, 5]]
#
# 示例 2：
# 输入：n = 1
# 输出：[[1]]
#
# 提示：
# 1 <= n <= 20

class Solution(object):  # 用的昨天评论区大佬的写法
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for _ in range(n)]
        bl = [[1] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1

        for x in range(n * n):
            # r.append(matrix[i][j])
            res[i][j] = x + 1
            bl[i][j] = 0
            if bl[(i + di) % n][(j + dj) % n] == 0:
                di, dj = dj, -di
            i += di
            j += dj
        return res
