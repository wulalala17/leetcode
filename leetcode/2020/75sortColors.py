# 75. 颜色分类
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
# 示例:
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
# 进阶：
#     一个直观的解决方案是使用计数排序的两趟扫描算法。
#     首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
#     你能想出一个仅使用常数空间的一趟扫描算法吗？



def sortColors(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1
    d0 = d.get(0, 0)
    d1 = d.get(1, 0)
    d2 = d.get(2, 0)
    for index in range(0, d0):
        nums[index] = 0
    for index in range(d0, d0 + d1):
        nums[index] = 1
    for index in range(d0 + d1, d0 + d1 + d2):
        nums[index] = 2

a = [2,0,2,1,1,0]
print(sortColors(a))

# class Solution: 一遍遍历 不用额外空间的写法 保证是2的时候往回走，而且当前指针不增加
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         p0, curr, p2 = 0, 0, len(nums) - 1
#         while curr <= p2:
#             if nums[curr] == 0: # 为0，做出决策
#                 nums[p0], nums[curr] = nums[curr], nums[p0]
#                 p0 += 1
#                 curr += 1
#             elif nums[curr] == 2:   # 为2，做出决策
#                 nums[p2], nums[curr] = nums[curr], nums[p2]
#                 p2 -= 1
#             else:                   # 为1，做出决策
#                 curr += 1
#
# 作者：HardCandy
# 链接：https://leetcode-cn.com/problems/sort-colors/solution/python-guan-fang-da-an-jie-xi-by-hardcandy/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。