# 643. 子数组最大平均数I
# 给定n个整数，找出平均数最大且长度为k的连续子数组，并输出该最大平均数。
# 示例：
# 输入：[1, 12, -5, -6, 50, 3], k = 4
# 输出：12.75
# 解释：最大平均数(12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
#
# 提示：
# 1 <= k <= n <= 30, 000。
# 所给数据范围[-10, 000，10, 000]。

def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    # res = 0
    # l = 0
    # r = k
    # while r <= len(nums):
    #     s = sum(nums[l:r])
    #     res = max(s, res)
    #     l += 1
    #     r += 1
    # return res / k

    res = -10000 * k  # 一开始初始化为0，老是错误，不能定性思维啊
    l = 0
    r = k
    s = sum(nums[l:r])
    while r < len(nums):
        res = max(res, s)
        s -= nums[l]
        l += 1
        if r == len(nums):
            break
        s += nums[r]
        r += 1
    res = max(res, s)
    return res / k

print(findMaxAverage([0,1,1,3,3], 4))