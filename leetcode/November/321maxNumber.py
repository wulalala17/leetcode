# 321. 拼接最大数
# 给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
# 求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
# 说明: 请尽可能地优化你算法的时间和空间复杂度。
# 示例 1:
# 输入:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# 输出:
# [9, 8, 6, 5, 3]
# 示例 2:
# 输入:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# 输出:
# [6, 7, 6, 0, 4]
# 示例 3:
# 输入:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# 输出:
# [9, 8, 9]
# https://leetcode-cn.com/problems/create-maximum-number/solution/pin-jie-zui-da-shu-by-leetcode-solution/
class Solution(object):  # 又是单调栈，又是合并的，太难了，官方题解
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        m, n = len(nums1), len(nums2)
        maxSubsequence = [0] * k
        start, end = max(0, k - n), min(k, m)

        for i in range(start, end + 1):
            subsequence1 = self.getMaxSubsequence(nums1, i)
            subsequence2 = self.getMaxSubsequence(nums2, k - i)
            curMaxSubsequence = self.merge(subsequence1, subsequence2)
            if self.compare(curMaxSubsequence, 0, maxSubsequence, 0) > 0:
                maxSubsequence = curMaxSubsequence

        return maxSubsequence

    def getMaxSubsequence(self, nums, k):
        stack = [0] * k
        top = -1
        remain = len(nums) - k

        for i, num in enumerate(nums):
            while top >= 0 and stack[top] < num and remain > 0:
                top -= 1
                remain -= 1
            if top < k - 1:
                top += 1
                stack[top] = num
            else:
                remain -= 1

        return stack

    def merge(self, subsequence1, subsequence2):
        x, y = len(subsequence1), len(subsequence2)
        if x == 0:
            return subsequence2
        if y == 0:
            return subsequence1

        mergeLength = x + y
        merged = list()
        index1 = index2 = 0

        for _ in range(mergeLength):
            if self.compare(subsequence1, index1, subsequence2, index2) > 0:
                merged.append(subsequence1[index1])
                index1 += 1
            else:
                merged.append(subsequence2[index2])
                index2 += 1

        return merged

    def compare(self, subsequence1, index1, subsequence2, index2):
        x, y = len(subsequence1), len(subsequence2)
        while index1 < x and index2 < y:
            difference = subsequence1[index1] - subsequence2[index2]
            if difference != 0:
                return difference
            index1 += 1
            index2 += 1

        return (x - index1) - (y - index2)

# def maxNumber(nums1, nums2, k):
#     """
#     :type nums1: List[int]
#     :type nums2: List[int]
#     :type k: int
#     :rtype: List[int]
#     """
#     n1 = len(nums1)
#     n2 = len(nums2)
#     res = []
#     i, j =0, 0
#     while k > 0:
#         max1 = max(nums1[i:])
#         max2 = max(nums2[j:])
#         i1 = nums1[i:].index(max1)
#         j1 = nums2[j:].index(max2)
#         if (n1 - i1) + (n2 - j1) >= k:
#             if max1 > max2:
#                 res.append(max1)
#                 i = i1
#                 k -= 1
#             else:
#                 res.append(max2)
#                 j = j1
#                 k -=1
#     return res