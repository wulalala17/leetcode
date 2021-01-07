# 547.省份数量
# 有n个城市，其中一些彼此相连，另一些没有相连。如果城市a与城市b直接相连，且城市b与城市c直接相连，那么城市a与城市c间接相连。省份是一组直接或间接相连的城市，组内不含其他没有相连的城市。
# 给你一个nxn的矩阵isConnected ，其中isConnected[i][j] = 1表示第i个城市和第j个城市直接相连，而isConnected[i][j] = 0表示二者不直接相连。
# 返回矩阵中省份的数量。
# 示例1：
# 输入：isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# 输出：2
#
# 示例2：
# 输入：isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# 输出：3
#
# 提示：
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j]为1或0
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

class Solution(object):  # 对DFS还不够熟练，看了评论才知道怎么写
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        def dfs(i, visited, isConnected):
            for j in range(len(isConnected)):
                visited[i] = 1
                if (isConnected[i][j] == 1 and visited[j] == 0):
                    dfs(j, visited, isConnected)

        res = 0
        visited = [0] * len(isConnected)
        for i in range(len(isConnected)):
            if visited[i] == 0:
                res += 1
                dfs(i, visited, isConnected)
        return res

        # for i in range(len(isConnected)):
        #     for j in range(len(isConnected[0])):
        #         if isConnected[i][j] == 1:
        #             f = 0
        #             for r in res:
        #                 if i in r:
        #                     if not j in r:
        #                         f = 1
        #                         r.append(j)
        #                         break
        #                     else:
        #                         f = 1
        #                         break
        #                 else:
        #                     if j in r:
        #                         r.append(i)
        #                         f = 1
        #                         break
        #             if f == 0:
        #                 if i == j:
        #                     res.append([i])
        #                 else:
        #                     res.append([i, j])
        # return len(res)

