# 189. 旋转数组
#
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#
# 示例 2:
#
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
#
# 说明:
#
#     尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
#     要求使用空间复杂度为 O(1) 的 原地 算法。

def rotate(nums, k):  # 还是用了额外空间
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    if len(nums) <= 1 or k == 0:
        return
    nums = nums + nums[:n-k]
    nums = nums[n-k:]
    return nums


    # def reverse(nums, start, end):  三次翻转
    #     while start < end:
    #         nums[start], nums[end] = nums[end], nums[start]
    #         start += 1
    #         end -= 1
    #
    #
    # n = len(nums)
    # k = k % n
    # if len(nums) <= 1 or k == 0:
    #     return
    # reverse(nums, 0, n - 1)
    # reverse(nums, 0, k - 1)
    # reverse(nums, k, n - 1)

a = [1,2,3,4,5,6,7]
k = 3
print(rotate(a, k))


