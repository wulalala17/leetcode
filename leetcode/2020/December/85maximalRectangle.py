# 85.最大矩形
#
# 给定一个仅包含0和1 、大小为rows x cols的二维二进制矩阵，找出只包含1的最大矩形，并返回其面积。
# 示例
# 1：
# 输入：matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
# 输出：6
# 解释：最大矩形如上图所示。
#
# 示例2：
# 输入：matrix = []
# 输出：0
#
# 示例3：
# 输入：matrix = [["0"]]
# 输出：0
#
# 示例4：
# 输入：matrix = [["1"]]
# 输出：1
#
# 示例5：
# 输入：matrix = [["0", "0"]]
# 输出：0
#
# 提示：
# rows == matrix.length
# cols == matrix[0].length
# 0 <= row, cols <= 200
# matrix[i][j]为'0'或'1'


def maximalRectangle(matrix):  # 看了官方题解才知道怎么暴力写，复杂度m**2 * n 击败5%
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    n = len(matrix)
    if n == 0:
        return 0
    m = len(matrix[0])
    leftArea = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '0':
                leftArea[i][j] = 0
            else:
                if j == 0:
                    leftArea[i][j] = 1
                else:
                    leftArea[i][j] = leftArea[i][j - 1] + 1
    res = 0
    for i in range(n):
        for j in range(m):
            if leftArea[i][j] != 0:
                r = 0
                k = 99999
                if i == n - 1:
                    r = leftArea[i][j]
                for ii in range(i, n):
                    k = min(leftArea[ii][j], k)
                    height = ii - i + 1
                    r = max(r, height * k)
                res = max(r, res)
    return res

print(maximalRectangle([["0","1"],["1","0"]]))



