def getMaxNeighbour(self, value_matrix, row, col):
    n = len(value_matrix)
    matrix = [[0] * n for _ in range(n)]
    cur = -1
    for value in value_matrix:  # 读出矩阵的值
        cur += 1
        v = value.strip('"').split(',')
        for i in range(n):
            matrix[cur][i] = int(v[i])
    neighbour = [-10086 for _ in range(8)]  # 初始化邻居的值
    cur = 0
    i = row
    j = col
    if i > 0 and j > 0:
        neighbour[cur] = matrix[i-1][j-1]  # 左上
        cur += 1
    if i > 0:
        neighbour[cur] = matrix[i - 1][j]  # 上
        cur += 1
    if i > 0 and j + 1 < n:
        neighbour[cur] = matrix[i - 1][j + 1]  # 右上
        cur += 1
    if j > 0:
        neighbour[cur] = matrix[i][j - 1]  # 左
        cur += 1
    if j + 1 < n:
        neighbour[cur] = matrix[i][j + 1]  # 右
        cur += 1
    if i + 1 < n and j > 0:
        neighbour[cur] = matrix[i + 1][j - 1]  # 左下
        cur += 1
    if i + 1 < n:
        neighbour[cur] = matrix[i + 1][j]  # 下
        cur += 1
    if i + 1 < n and j + 1 < n:
        neighbour[cur] = matrix[i + 1][j + 1]  # 右下
        cur += 1
    return max(neighbour)
va = ["6,2,8,6,7", "5,8,1,4,9", "1,3,5,2,1","4,1,1,4,1","3,6,5,2,1"]
print(getMaxNeighbour(va, 4, 4))


#  6 2 8 6 7
#  5 8 1 4 9
#  1 3 5 2 1
#  4 1 1 4 1
#  3 6 5 2 1