# 697.数组的度
# 给定一个非空且只包含非负数的整数数组nums，数组的度的定义是指数组里任一元素出现频数的最大值。
# 你的任务是在nums中找到与nums拥有相同大小的度的最短连续子数组，返回其长度。

# 示例1：
# 输入：[1, 2, 2, 3, 1]
# 输出：2
# 解释：
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
#
# 示例2：
# 输入：[1, 2, 2, 3, 1, 4, 2]
# 输出：6
#
# 提示：
# nums.length在1到 50, 000 区间范围内。
# nums[i]是一个在0到49, 999范围内的整数。
class Solution(object):  # 字典，然后暴力
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in range(len(nums)):
            n = nums[i]
            if n not in d:
                d[n] = [1, i, i]
            else:
                d[n][0] += 1
                d[n][2] = i
        x = sorted(d.items(), key = lambda x : x[1][0], reverse = True)
        # print(x)
        r = x[0][1][0]
        res = x[0][1][2] - x[0][1][1]
        for xx in x:
            if xx[1][0] != r:
                break
            res = min(res, xx[1][2]-xx[1][1])
        return res+1