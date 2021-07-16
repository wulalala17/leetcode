# 剑指Offer53 - I.在排序数组中查找数字I
#
# 统计一个数字在排序数组中出现的次数。
# 示例1:
# 输入: nums = [5, 7, 7, 8, 8, 10], target = 8
# 输出: 2
#
# 示例2:
# 输入: nums = [5, 7, 7, 8, 8, 10], target = 6
# 输出: 0
#
# 限制：
# 0 <= 数组长度 <= 50000
#
# 注意：本题与主站34题相同（仅返回值不同）：https: // leetcode - cn.com / problems / find - first - and -last - position - of - element - in -sorted - array /


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    def binarySearch(nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l
    idx = binarySearch(nums, target)
    res = 0
    if idx >= len(nums) or idx < 0:
        return res
    while idx < len(nums) and nums[idx] == target:
        idx += 1
        res += 1
    return res
