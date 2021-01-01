# 327. 区间和的个数
# 给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
# 区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
# 说明:
# 最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。
# 示例:
# 输入: nums = [-2,5,-1], lower = -2, upper = 2,
# 输出: 3
# 解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。
def countRangeSum(nums, lower, upper):
    # nums = sorted(nums)
    res = 0
    if len(nums) == 1:
        if lower <= sum(nums[:]) <= upper:
            return 1
        else:
            return 0
    for i in range(len(nums)):
        s = 0
        for j in range(i, len(nums)):
            s += nums[j]
            if lower <= s <= upper:
                res += 1
    return res

a = [-2,5,-1]
b = [2147483647, -2147483648, -1, 0]
print(countRangeSum(b, -1, 0))