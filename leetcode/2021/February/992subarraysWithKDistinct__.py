# 992. K个不同整数的子数组
# 给定一个正整数数组A，如果A的某个子数组中不同整数的个数恰好为K，则称 A的这个连续、不一定独立的子数组为好子数组。
# （例如，[1, 2, 3, 1, 2]中有3个不同的整数：1，2，以及3。）返回A中好子数组的数目。
# 示例1：
# 输入：A = [1, 2, 1, 2, 3], K = 2
# 输出：7
# 解释：恰好由2个不同整数组成的子数组：[1, 2], [2, 1], [1, 2], [2, 3], [1, 2, 1], [2, 1, 2], [1, 2, 1, 2].
#
# 示例2：
# 输入：A = [1, 2, 1, 3, 4], K = 3
# 输出：3
# 解释：恰好由3个不同整数组成的子数组：[1, 2, 1, 3], [2, 1, 3], [1, 3, 4].
#
# 提示：
# 1 <= A.length <= 20000
# 1 <= A[i] <= A.length
# 1 <= K <= A.length

class Solution:  # py3能过 2就不行
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        if len(set(A)) < K:
            return 0
        res = 0
        for i in range(len(A) - K + 1):
            s = set(A[i:i+K])
            for j in range(i + K - 1, len(A)):
                if len(s) == K:
                    res += 1
                if j+1 < len(A):
                    s.add(A[j+1])
                if len(s) > K:
                    break
        return res


# class Solution(object):
#     def subarraysWithKDistinct(self, A, K):
#         """
#         :type A: List[int]
#         :type K: int
#         :rtype: int
#         """
#         return self.atMostK(A, K) - self.atMostK(A, K - 1)
#
#     def atMostK(self, A, K):
#         N = len(A)
#         left, right = 0, 0
#         counter = collections.Counter()
#         distinct = 0
#         res = 0
#         while right < N:
#             if counter[A[right]] == 0:
#                 distinct += 1
#             counter[A[right]] += 1
#             while distinct > K:
#                 counter[A[left]] -= 1
#                 if counter[A[left]] == 0:
#                     distinct -= 1
#                 left += 1
#             res += right - left + 1
#             print(left, right, res)
#             right += 1
#         return res
#
#
# 作者：fuxuemingzhu
# 链接：https: // leetcode - cn.com / problems / subarrays -
# with-k - different - integers / solution / cong - zui - jian - dan - de - wen - ti - yi - bu - bu - tuo - 7f4v /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。