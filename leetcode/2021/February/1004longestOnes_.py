# 1004.最大连续1的个数III
# 给定一个由若干0和1组成的数组A，我们最多可以将K个值从0变成1 。
# 返回仅包含1的最长（连续）子数组的长度。
# 示例1：
# 输入：A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], K = 2
# 输出：6
# 解释：[1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1]粗体数字从0翻转到1，最长的子数组长度为6。
#
# 示例2：
# 输入：A = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], K = 3
# 输出：10
# 解释：[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]粗体数字从0翻转到1，最长的子数组长度为10。
#
# 提示：
# 1 <= A.length <= 20000
# 0 <= K <= A.length
# A[i]为0或1


class Solution(object):  # 看了题解才知道滑窗模板这么用
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res = 0
        l, r = 0, 0
        zeros = 0
        while r < len(A):
            if A[r] == 0:
                zeros += 1
            while zeros > K:
                if A[l] == 0:
                    zeros -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res


        # while l < len(A) and r < len(A):
        #     if A[r] == 1 or K > 0:
        #         if A[r] == 0:
        #             K -= 1
        #         r += 1
        #     else:
        #         if A[l] == 0:
        #             r += 1
        #         l += 1
        #     res = max(res, r-l)
        # return res


