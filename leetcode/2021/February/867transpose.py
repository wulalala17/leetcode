# 867. 转置矩阵
# 给你一个二维整数数组matrix， 返回matrix的转置矩阵 。
# 矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
# 示例 1：
# 输入：matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 输出：[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#
# 示例2：
# 输入：matrix = [[1, 2, 3], [4, 5, 6]]
# 输出：[[1, 4], [2, 5], [3, 6]]
#
# 提示：
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 105
# -109 <= matrix[i][j] <= 109

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        res = []
        for i in range(n):
            r = []
            for j in range(m):
                r.append(matrix[j][i])
            res.append(r)
        return res
