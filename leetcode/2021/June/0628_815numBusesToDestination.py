# 815. 公交路线
#
# 给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。
#
# 例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... 这样的车站路线行驶。
# 现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。
# 求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 - 1 。
#
# 示例 1：
# 输入：routes = [[1, 2, 7], [3, 6, 7]], source = 1, target = 6
# 输出：2
# 解释：最优策略是先乘坐第一辆公交车到达车站 7, 然后换乘第二辆公交车到车站 6 。
#
# 示例 2：
# 输入：routes = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], source = 15, target = 12
# 输出：-1
#
# 提示：
# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 105
# routes[i] 中的所有值 互不相同
# sum(routes[i].length) <= 105
# 0 <= routes[i][j] < 106
# 0 <= source, target < 106
from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # 每个车站可以乘坐的公交车
        stations = defaultdict(set)
        for i, stops in enumerate(routes):
            for stop in stops:
                stations[stop].add(i)
        # 每个公交车线路可以到达的车站
        routes = [set(x) for x in routes]

        q = deque([(source, 0)])
        # 已经乘坐了的公交车
        buses = set()
        # 已经到达了的车站
        stops = {source}
        while q:
            pos, cost = q.popleft()
            if pos == target:
                return cost
            # 当前车站中尚未乘坐的公交车
            for bus in stations[pos] - buses:
                # 该公交车尚未到达过的车站
                for stop in routes[bus] - stops:
                    buses.add(bus)
                    stops.add(stop)
                    q.append((stop, cost + 1))
        return -1

# class Solution(object):  # 自己写的BFS超时了
#     def numBusesToDestination(self, routes, source, target):
#         """
#         :type routes: List[List[int]]
#         :type source: int
#         :type target: int
#         :rtype: int
#         """
#         visited = [source]
#         used = [0 for i in range(len(routes))]
#         now = [source]
#         res = 0
#         if target == source:
#             return 0
#         while now:
#             l = len(now)
#             res += 1
#             for i in range(l):
#                 cur = now.pop(0)
#                 for j in range(len(routes)):
#                     if used[j] == 1 or cur not in routes[j]:  # 用过了或者不包括当前车站
#                         continue
#                     else:
#                         used[j] = 1
#                         for cc in routes[j]:
#                             if cc in visited:
#                                 continue
#                             if cc == target:
#                                 return res
#                             if cc != cur:
#                                 visited.append(cc)
#                                 now.append(cc)
#         return -1