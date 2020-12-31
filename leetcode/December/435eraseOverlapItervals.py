# 435. 无重叠区间
# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
# 注意:
#     可以认为区间的终点总是大于它的起点。
#     区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
#
# 示例 1:
# 输入: [ [1,2], [2,3], [3,4], [1,3] ]
# 输出: 1
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
#
# 示例 2:
# 输入: [ [1,2], [1,2], [1,2] ]
# 输出: 2
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
#
# 示例 3:
# 输入: [ [1,2], [2,3] ]
# 输出: 0
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

class Solution(object):  # 瞎JB贪心竟然过了
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) <= 1:
            return 0
        interval = sorted(intervals, key = lambda x: x[0])
        res = 0
        left, right = interval[0][0], interval[0][1]  # 当前左右端点
        for i in range(1, len(interval)):
            if interval[i][0] >= right:
                left = interval[i][0]
                right = interval[i][1]
            else:
                if interval[i][1] < right:
                    res += 1
                    left = interval[i][0]
                    right = interval[i][1]
                else:
                    res += 1
        return res
