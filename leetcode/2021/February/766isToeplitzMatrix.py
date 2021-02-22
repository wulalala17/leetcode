# 766. 托普利茨矩阵
# 给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。
# 如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是托普利茨矩阵 。
#
# 示例 1：
# 输入：matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
# 输出：true
# 解释：
# 在上述矩阵中, 其对角线为:"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。各条对角线上的所有元素均相同, 因此答案是True 。
#
# 示例2：
# 输入：matrix = [[1, 2], [2, 2]]
# 输出：false
# 解释：
# 对角线"[1, 2]"上的元素不同。
#
#
#
# 提示：
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 20
# 0 <= matrix[i][j] <= 99
#
# 进阶：
# 如果矩阵存储在磁盘上，并且内存有限，以至于一次最多只能将矩阵的一行加载到内存中，该怎么办？
# 如果矩阵太大，以至于一次只能将不完整的一行加载到内存中，该怎么办？

class Solution(object):  # 很绕，写得很慢
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):  # 从第一行往右遍历
            j = 0
            cur = matrix[j][j + i]  # 第一个元素
            while j < m and j + i < n:
                if matrix[j][j + i] != cur:
                    return False
                j += 1
        for i in range(1, m):  # 从第一列往下遍历
            j = i
            cur = matrix[j][j - i]
            while j < m and j - i < n:
                if matrix[j][j - i] != cur:
                    return False
                j += 1
        return True
# 评论里大神的做法：
# 只需判断：前行中除最后一个元素外剩余的元素完全等于后行中除第一个元素外剩余的元素。
#
# class Solution:
#     def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
#         col_len = len(matrix) #3
#         row_len = len(matrix[0]) #4
#         if col_len == 1 or row_len == 1:
#             return True
#         for i in range(len(matrix) - 1):
#             if matrix[i][:-1] != matrix[i + 1][1:]:
#                 return False
#         return True



