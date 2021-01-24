# 674. 最长连续递增序列
# 给定一个未经排序的整数数组，找到最长且连续递增的子序列，并返回该序列的长度。
# 连续递增的子序列可以由两个下标l和r（l < r）确定，如果对于每个l <= i < r，都有
# nums[i] < nums[i + 1] ，那么子序列[nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]就是连续递增子序列。
#
# 示例1：
# 输入：nums = [1, 3, 5, 4, 7]
# 输出：3
# 解释：最长连续递增序列是[1, 3, 5], 长度为3。尽管[1, 3, 5, 7]也是升序的子序列, 但它不是连续的，因为5和 7在原数组里被4隔开。
#
# 示例2：
# 输入：nums = [2, 2, 2, 2, 2]
# 输出：1
# 解释：最长连续递增序列是[2], 长度为1。
#
# 提示：
# 0 <= nums.length <= 104
# -109 <= nums[i] <= 109

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return 1
        res, cur = 0, 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                cur += 1
            else:
                cur = 1
            if cur > res:
                res = cur
        return res
