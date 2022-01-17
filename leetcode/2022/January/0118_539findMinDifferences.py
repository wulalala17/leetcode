# 539. 最小时间差
#
# 给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。
#
#
#
# 示例 1：
#
# 输入：timePoints = ["23:59","00:00"]
# 输出：1
#
# 示例 2：
#
# 输入：timePoints = ["00:00","23:59","00:00"]
# 输出：0
#
#
#
# 提示：
#
#     2 <= timePoints <= 2 * 104
#     timePoints[i] 格式为 "HH:MM"
class Solution(object):  # 简单题想得太复杂
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        l = []
        res = 24 * 60
        for t in timePoints:
            x1 = int(t[0:2]) * 60 + int(t[3:5])
            l.append(x1)
            if int(t[0:2]) <= 12:
                x1 = (int(t[0:2]) + 24) * 60 + int(t[3:5])
                l.append(x1)
        l = sorted(l)
        for i in range(1, len(l)):
            res = min(res, l[i] - l[i - 1])
        return res
