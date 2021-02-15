# 485. 最大连续1的个数
#
# 给定一个二进制数组， 计算其中最大连续1的个数。
#
# 示例 1:
#
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
#
# 注意：
#
#     输入的数组只包含 0 和1。
#     输入数组的长度是正整数，且不超过 10,000。

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        res, cur = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] == 1:
                cur += 1
                res = max(cur, res)
            else:
                cur = 0
        return res