# 54. 螺旋矩阵
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 示例 1：
# 输入：matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 输出：[1, 2, 3, 6, 9, 8, 7, 4, 5]
#
# 示例 2：
# 输入：matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# 输出：[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
#
# 提示：
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

def spiralOrder(matrix):  # 写了半天才写对了
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """

    def finish(b):  # 判断是否全都遍历过了
        for i in range(len(b)):
            for j in range(len(b[0])):
                if b[i][j] == 0:
                    return True
        return False

    flag = ['right', 'down', 'left', 'up']
    bl = [[0] * len(matrix[0]) for j in range(len(matrix))]
    z = 0
    res = []
    x, y = 0, 0
    while finish(bl):
        index = z % 4
        z += 1
        if flag[index] == 'right':
            while 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                if bl[x][y] == 0:
                    res.append(matrix[x][y])
                    bl[x][y] = 1
                y += 1
                if y == len(matrix[0]):  # 不符合条件要先退回，再break
                    y -= 1
                    break
                if bl[x][y] == 1:
                    y -= 1
                    break

        elif flag[index] == 'down':
            while 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                if bl[x][y] == 0:
                    res.append(matrix[x][y])
                    bl[x][y] = 1
                x += 1
                if x == len(matrix):
                    x -= 1
                    break
                if bl[x][y] == 1:
                    x -= 1
                    break

        elif flag[index] == 'left':
            while 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                if bl[x][y] == 0:
                    res.append(matrix[x][y])
                    bl[x][y] = 1
                y -= 1
                if y == -1:
                    y += 1
                    break
                if bl[x][y] == 1:
                    y += 1
                    break

        else:
            while 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                if bl[x][y] == 0:
                    res.append(matrix[x][y])
                    bl[x][y] = 1
                x -= 1
                if x == -1:
                    x += 1
                    break
                if bl[x][y] == 1:
                    x += 1
                    break
    return res

m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(m))

# 评论里的优秀写法
# r, i, j, di, dj = [], 0, 0, 0, 1
# if matrix != []:
#     for _ in range(len(matrix) * len(matrix[0])):
#         r.append(matrix[i][j])
#         matrix[i][j] = 0
#         if matrix[(i + di) % len(matrix)][(j + dj) % len(matrix[0])] == 0:
#             di, dj = dj, -di
#         i += di
#         j += dj
# return r