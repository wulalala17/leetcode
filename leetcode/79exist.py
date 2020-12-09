# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 示例:
# board =
# [
#     ['A', 'B', 'C', 'E'],
#     ['S', 'F', 'C', 'S'],
#     ['A', 'D', 'E', 'E']
# ]
# 给定  word = "ABCCED", 返回 true
# 给定  word = "SEE", 返回 true
# 给定  word = "ABCB", 返回 false
# 提示：
# board和word中只包含大写和小写英文字母。
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10 ^ 3
#
# 来源：力扣（LeetCode）
# 链接：https: // leetcode - cn.com / problems / word - search
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
def exist(board, word) -> bool:
    n1 = len(board)
    n2 = len(board[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # for _ in range(len(board[0])):
    #     f.append(0)
    # for _ in range(len(board)):
    #     flag.append(f)

    def dfs(i, j, word, flag): # 参考别人的
        '深度优先搜索'
        if len(word) == 1:
            return board[i][j] == word[0]
        elif board[i][j] != word[0]:
            return False
        flag[i][j] = 1
        for d in directions:
            cur_i, cur_j = i+d[0], j+d[1]
            if 0 <= cur_i <n1 and 0 <= cur_j < n2 and flag[cur_i][cur_j] == 0:
                if dfs(cur_i, cur_j, word[1:], flag):
                    return True
        flag[i][j] = 0

    flag = [[0 for i in range(n2)] for i in range(n1)]  # 记录是否被访问过
    for i in range(n1):
        for j in range(n2):
            if dfs(i, j, word, flag):
                return True
    print(flag)
    return False



    # def findchar(board, c, k):
    #     for i in range(n1):
    #         for j in range(n2):
    #             if board[i][j] == c and flag[i][j] == 0:
    #                 flag[i][j] = k
    #                 return True
    #     return False
    #
    # for i in range(len(word)):
    #     if not findchar(board, word[i], i+1):
    #         return False


board =[
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
print(exist(board, 'ABC'))


