# https://leetcode-cn.com/problems/snakes-and-ladders/ 909. 蛇梯棋
from collections import deque


class Solution(object):  # 自己写的不知道错哪了，思路没问题
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        queue, vis = deque([(1, 0)]), {1}
        while queue:
            u, step = queue.popleft()
            for v in range(u+1, u+7):
                i, j = divmod(v-1, n)
                x, y = n-1-i,  n-1-j if i % 2 else j
                v = board[x][y] if board[x][y] != -1 else v
                if v == n*n:
                    return step+1
                if v not in vis:
                    vis.add(v)
                    queue.append((v, step+1))
        return -1