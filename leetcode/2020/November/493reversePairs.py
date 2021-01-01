# 493. 翻转对
#
# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
#
# 你需要返回给定数组中的重要翻转对的数量。
#
# 示例 1:
#
# 输入: [1,3,2,3,1]
# 输出: 2
#
# 示例 2:
#
# 输入: [2,4,3,5,1]
# 输出: 3
#
# 注意:
#
#     给定数组的长度不会超过50000。
#     输入数组中的所有数字都在32位整数的表示范围内。


# 不会写 参考https://leetcode-cn.com/problems/reverse-pairs/solution/zui-jian-dan-yi-shi-xian-de-fang-fa-er-fen-cha-zha/
# from bisect import bisect
# 
#
# class Solution(object):
#     def reversePairs(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # if len(nums) <= 1:
#         #     return 0
#         # res = 0
#         # for i in range(len(nums)-1):
#         #     for j in range(i+1, len(nums)):
#         #         if nums[i] > 2*nums[j]:
#         #             res += 1
#         # return res
#         ri, res, n = [], 0, len(nums)
#         for i in reversed(range(0, n)):
#             res += bisect.bisect_left(ri, nums[i])
#             bisect.insort(ri, 2 * nums[i])
#         return res