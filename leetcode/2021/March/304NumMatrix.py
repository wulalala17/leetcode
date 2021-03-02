# 304. 二维区域和检索 - 矩阵不可变
# 给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为(row1, col1) ，右下角为(row2, col2) 。
# 上图子矩阵左上角(row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。
# 示例：
# 给定
# matrix = [
#     [3, 0, 1, 4, 2],
#     [5, 6, 3, 2, 1],
#     [1, 2, 0, 1, 5],
#     [4, 1, 0, 1, 7],
#     [1, 0, 3, 0, 5]
# ]
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
#
# 提示：
# 你可以假设矩阵不可变。 会多次调用 sumRegion 方法。
# 你可以假设 row1 ≤ row2 且col1 ≤ col2 。

class NumMatrix(object):  # 还是不够优化，不能像一维的那样算每一行的，而是应该保存左上角到i,j的元素和

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        s = [[0 for col in range(len(matrix[0])+1)] for row in range(len(matrix))]
        for i in range(len(matrix)):
            # s[i][0] = matrix[i][0]
            for j in range(1, len(matrix[0])+1):
                s[i][j] = s[i][j-1] + matrix[i][j-1]
        self.s = s


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for i in range(row1, row2+1):
            res += self.s[i][col2+1] - self.s[i][col1]
            # if col1 == 0:
            #     res += self.s[i][col2]
            # else:
            #     res += self.s[i][col2] - self.s[i][col1-1]
        return res




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# class NumMatrix:  # 评论区的正确做法
#
#     def __init__(self, matrix: List[List[int]]):
#         if not matrix:
#             return
#         # 继续前缀和，保存每个point往左上角的方向的总和
#         m,n = len(matrix),len(matrix[0])
#         self.sum_matrix = [[0] * n for _ in range(m)]
#         for i in range(m):
#             row_sum = 0 # 单独记录当行的和
#             for j in range(n):
#                 row_sum += matrix[i][j]
#                 if i==0:
#                     self.sum_matrix[i][j] = row_sum
#                 else:
#                     self.sum_matrix[i][j] = self.sum_matrix[i-1][j] + row_sum
#
#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         s1 = self.sum_matrix[row2][col2]
#         s2 = self.sum_matrix[row2][col1-1] if col1>0 else 0
#         s3 = self.sum_matrix[row1-1][col2] if row1>0 else 0
#         s4 = self.sum_matrix[row1-1][col1-1] if col1>0 and row1>0 else 0
#         return s1-s2-s3+s4