# 665. 非递减数列
# 给你一个长度为n的整数数组，请你判断在最多改变1个元素的情况下，该数组能否变成一个非递减数列。
# 我们是这样定义一个非递减数列的： 对于数组中所有的i(0 <= i <= n - 2)，总满足nums[i] <= nums[i + 1]。
# 示例1:
# 输入: nums = [4, 2, 3]
# 输出: true
# 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
#
# 示例2:
# 输入: nums = [4, 2, 1]
# 输出: false
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
# 说明：
# 1 <= n <= 10 ^ 4
# - 10 ^ 5 <= nums[i] <= 10 ^ 5
class Solution(object):  # 面向测试用例编程，特殊情况要多加考虑
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = 0
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                res += 1
                idx = i
                if res == 2:
                    return False

        if res == 1:  # 把不符合规范的数单独拿出来讨论
            if idx == len(nums) - 1 or idx == 1:  # 只需修改一个数
                return True
            if nums[idx - 1] > nums[idx + 1] and nums[idx] < nums[idx - 2]:  # 5 7 4 6 只能修改7或者4
                return False
        return True