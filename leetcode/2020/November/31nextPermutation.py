# 31. 下一个排列
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

def nextPermutation(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    start, end = -1, -1
    if len(nums) == 2:
        nums[0], nums[1] = nums[1], nums[0]
        return nums
    if len(nums) <= 1:
        return nums
    for i in range(len(nums) - 1, 0, -1):
        if nums[i - 1] < nums[i]:
            start = i - 1
            break
    if start == -1:
        nums.sort()
        return nums
    for i in range(len(nums) - 1, start, -1):
        if nums[i] > nums[start]:
            end = i
            break
    nums[start], nums[end] = nums[end], nums[start]
    y = sorted(nums[start + 1:])
    k = 0
    for i in range(start + 1, len(nums)):
        nums[i] = y[k]
        k += 1
    return nums

a = [1, 3, 2]
print(nextPermutation(a))

