# 628. 三个数的最大乘积
# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
#
# 示例 1:
# 输入: [1,2,3]
# 输出: 6
#
# 示例 2:
# 输入: [1,2,3,4]
# 输出: 24
#
# 注意:
#
#     给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
#     输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。

class Solution(object):  # 考虑半天特殊情况 结果只要算5个数就好了，可以线性扫描，不用排序
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        return max(nums[0] * nums[-1] * nums[-2], nums[0] * nums[1] * nums[2])
        # if 0 not in nums:
        #     if nums[2] > 0 or nums[0] < 0: # +++ ---的情况
        #         return max(nums[0] * nums[-1] * nums[-2], nums[0] * nums[1] * nums[2])
        #     if nums[2] < 0: # +-- ++- 的情况
        #         return nums[0] * nums[-1] * nums[-2]
        # else:
        #     if nums[0] == 0:
        #         return 0
        #     else:
        #         return max(nums[0] * nums[-1] * nums[-2], nums[0] * nums[1] * nums[2])


