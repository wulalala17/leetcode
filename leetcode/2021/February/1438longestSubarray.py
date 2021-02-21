# 1438. 绝对差不超过限制的最长连续子数组
# 给你一个整数数组nums ，和一个表示限制的整数limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于limit 。
# 如果不存在满足条件的子数组，则返回0 。
# 示例 1：
# 输入：nums = [8, 2, 4, 7], limit = 4
# 输出：2
# 解释：所有子数组如下：
# [8] 最大绝对差 | 8 - 8 | = 0 <= 4.
# [8, 2] 最大绝对差 | 8 - 2 | = 6 > 4.
# [8, 2, 4] 最大绝对差 | 8 - 2 | = 6 > 4.
# [8, 2, 4, 7] 最大绝对差 | 8 - 2 | = 6 > 4.
# [2] 最大绝对差 | 2 - 2 | = 0 <= 4.
# [2, 4] 最大绝对差 | 2 - 4 | = 2 <= 4.
# [2, 4, 7] 最大绝对差 | 2 - 7 | = 5 > 4.
# [4] 最大绝对差 | 4 - 4 | = 0 <= 4.
# [4, 7] 最大绝对差 | 4 - 7 | = 3 <= 4.
# [7] 最大绝对差 | 7 - 7 | = 0 <= 4.
# 因此，满足题意的最长子数组的长度为 2 。

# 示例2：
# 输入：nums = [10, 1, 2, 4, 7, 2], limit = 5
# 输出：4
# 解释：满足题意的最长子数组是[2, 4, 7, 2]，其最大绝对差 | 2 - 7 | = 5 <= 5 。
#
# 示例3：
# 输入：nums = [4, 2, 2, 2, 4, 4, 2, 2], limit = 0
# 输出：3
#
# 提示：
# 1 <= nums.length <= 10 ^ 5
# 1 <= nums[i] <= 10 ^ 9
# 0 <= limit <= 10 ^ 9
from collections import deque


class Solution(object):  # 不知道怎么用单调队列，看的官方题解
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(nums)
        queMax, queMin = deque(), deque()
        left = right = ret = 0

        while right < n:
            while queMax and queMax[-1] < nums[right]:
                queMax.pop()
            while queMin and queMin[-1] > nums[right]:
                queMin.pop()

            queMax.append(nums[right])
            queMin.append(nums[right])

            while queMax and queMin and queMax[0] - queMin[0] > limit:
                if nums[left] == queMin[0]:
                    queMin.popleft()
                if nums[left] == queMax[0]:
                    queMax.popleft()
                left += 1

            ret = max(ret, right - left + 1)
            right += 1

        return ret
