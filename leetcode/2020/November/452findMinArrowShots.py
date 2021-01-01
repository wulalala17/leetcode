# 452.
# 用最少数量的箭引爆气球
# 在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以纵坐标并不重要，因此只要知道开始和结束的横坐标就足够了。开始坐标总是小于结束坐标。
# 一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处射出一支箭，若有一个气球的直径的开始和结束坐标为xstart，xend， 且满足
# xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。
# 给你一个数组points ，其中points[i] = [xstart, xend] ，返回引爆所有气球所必须射出的最小弓箭数。
# 示例
# 1：
# 输入：points = [[10, 16], [2, 8], [1, 6], [7, 12]]
# 输出：2
# 解释：对于该样例，x = 6可以射爆[2, 8], [1, 6]两个气球，以及x = 11射爆另外两个气球
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        def intersection(x, y):
            if x[0] > y[0]:
                x, y = y, x
            if x[1] >= y[0]:
                return True
            else:
                return False
        res, n = len(points), len(points)
        if n <= 1:
            return n
        p = sorted(points, key=lambda x: x[0])
        x = [p[0][0], p[0][1]]  # 记录交集
        for i in range(1, n):
            if intersection(p[i], x):  # 有交集就更新交集大小
                res -= 1
                if p[i][0] < x[0]:
                    if p[i][1] < x[1]:
                        x[1] = p[i][1]
                else:
                    x[0] = p[i][0]
                    if p[i][1] < x[1]:
                        x[1] = p[i][1]
            else:  # 没有交集就让交集变成新的这个点
                x[0] = p[i][0]
                x[1] = p[i][1]
        return res