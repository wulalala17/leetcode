# 724. 寻找数组的中心索引
# 给定一个整数类型的数组nums，请编写一个能够返回数组 “中心索引” 的方法。
# 我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。
# 如果数组不存在中心索引，那么我们应该返回 - 1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。
# 示例1：
# 输入：nums = [1, 7, 3, 6, 5, 6]
# 输出：3
# 解释：索引3(nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11) 相等。同时, 3 也是第一个符合要求的中心索引。
#
# 示例2：
# 输入：nums = [1, 2, 3]
# 输出：-1
# 解释：数组中不存在满足此条件的中心索引。
#
# 说明：
# nums的长度范围为[0, 10000]。
# 任何一个nums[i]将会是一个范围在[-1000, 1000]的整数。

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) == 0:
        #     return -1
        # if 0 == sum(nums[1:]):
        #     return 0
        # for i in range(1, len(nums) - 1):
        #     if sum(nums[:i]) == sum(nums[i+1:]):
        #         return i
        # if 0 == sum(nums[:-1]):
        #     return len(nums) - 1
        # return -1

        s = sum(nums)
        i = 0
        leftsum = 0
        while i < len(nums):
            if leftsum * 2 == s - nums[i]:
                return i
            leftsum += nums[i]
            i += 1
        return -1