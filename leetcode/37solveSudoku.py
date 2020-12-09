# 编写一个程序，通过已填充的空格来解决数独问题。
#
# 一个数独的解法需遵循如下规则：
#
#     数字 1-9 在每一行只能出现一次。
#     数字 1-9 在每一列只能出现一次。
#     数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
#
# 空白格用 '.' 表示。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sudoku-solver
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
def solveSudoku(board):
    row = [set(i for i in range(1, 10)) for _ in range(9)]  # 每行还能用的数字
    col = [set(i for i in range(1, 10)) for _ in range(9)]  # 每列还能用的数字
    block = [set(i for i in range(1, 10)) for _ in range(9)]  # 每块还能用的数字
    empty = []  # 记录空白位置
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':  # 不是空白
                val = int(board[i][j])
                row[i].remove(val)  # 删除val对应的行、列、块里的数字
                col[j].remove(val)
                block[(i//3)*3 + j//3].remove(val)
            else:
                empty.append((i, j))

    def backTrace(iter = 0):
        if len(empty) == iter:
            print(board)
            return True
        i, j = empty[iter]
        for val in row[i]&col[j]&block[(i//3)*3 + j//3]:  #取交集
            row[i].remove(val)
            col[j].remove(val)
            block[(i//3)*3 + j//3].remove(val)
            board[i][j] = str(val)
            if backTrace(iter+1):
                return True
            row[i].add(val)
            col[j].add(val)
            block[(i//3)*3 + j//3].add(val)
        return False
    backTrace()


board = [[5, 3, '.', '.', 7, '.', '.', '.', '.'], [6, '.', '.', 1, 9, 5, '.', '.', '.'], ['.', 9, 8, '.', '.', '.', '.', 6,'.'], [8, '.', '.', '.', 6, '.', '.', '.', 3], [4, '.', '.', 8, '.', 3, '.', '.', 1], [7, '.', '.', '.', 2, '.', '.', '.', 6], ['.', 6, '.', '.', '.', '.', 2, 8, '.'], ['.', '.', '.', 4, 1, 9, '.', '.', 5], ['.', '.', '.', '.', 8, '.', '.', 7, 9]]
solveSudoku(board)
# 3row = [set(i for i in range(1, 10)) for _ in range(9)]
# print(row)