# 52.N皇后II
# n皇后问题研究的是如何将n个皇后放置在n×n的棋盘上，并且使皇后彼此之间不能相互攻击。上图为8皇后问题的一种解法。
# 给定一个整数n，返回n皇后不同的解决方案的数量。
# 示例:
# 输入: 4
# 输出: 2
# 解释: 4
# 皇后问题存在如下两个不同的解法。
# [
#     [".Q..", // 解法 1
#     "...Q",
#     "Q...",
#     "..Q."],
# ["..Q.", // 解法2
# "Q...",
# "...Q",
# ".Q.."]
# ]
def totalNQueens(n):
    col = [0 for _ in range(n)]  # 记录某列是否已有皇后摆放
    dia1 = [0 for _ in range(2*n-1)]  # 记录某条正对角线（左上右下）是否已有皇后摆放（某条对角线对应的摆放位置为 x - y + n - 1）
    dia2 = [0 for _ in range(2 * n - 1)]   # 记录某条斜对角线（左下右上）是否已有皇后摆放（某条对角线对应的摆放位置为 x + y）


    def backtrack(n, index):  # @param n     待摆放皇后个数  @param index 已摆放皇后个数
        res = 0
        if index == n:
            return 1

        for i in range(n):  # 表示在 index 行的第 i 列尝试摆放皇后
            if col[n] == 0 and dia1[i-index+n-1] == 0 and dia2[i+index] == 0:
                col[i] = 1
                dia1[i - index + n - 1] = 1
                dia2[i + index] = 1
                res += backtrack(n, index+1)
                col[i] = 0
                dia1[i - index + n - 1] = 0
                dia2[i + index] = 0
        return res
    r = backtrack(n, 0)
    return r




