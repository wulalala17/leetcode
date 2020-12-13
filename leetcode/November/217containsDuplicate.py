# 217.存在重复元素
# 给定一个整数数组，判断是否存在重复元素。如果任意一值在数组中出现至少两次，函数返回true 。如果数组中每个元素都不相同，则返回false。
# 示例1:
# 输入: [1, 2, 3, 1]
# 输出: true
# 示例2:
# 输入: [1, 2, 3, 4]
# 输出: false
# 示例3:
# 输入: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# 输出: true



class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        d = {}
        for i in range(len(nums)):
            if d.get(nums[i], 0) == 1:
                return True
            d[nums[i]] = 1
        return False

        # return len(set(nums)) != len(nums) 一行版本