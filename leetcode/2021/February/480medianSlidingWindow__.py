# 480. 滑动窗口中位数
# 中位数是有序序列最中间的那个数。如果序列的大小是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。
# 例如：
# [2, 3, 4]，中位数是3
# [2, 3]，中位数是(2 + 3) / 2 = 2.5
# 给你一个数组nums，有一个大小为k的窗口从最左端滑动到最右端。窗口中有k个数，每次窗口向右移动1位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。
#
# 示例：
# 给出nums = [1, 3, -1, -3, 5, 3, 6, 7]，以及k = 3。
# 因此，返回该滑动窗口的中位数数组[1, -1, -1, 3, 5, 6]。
# 提示：
# 你可以假设k始终有效，即：k始终小于输入的非空数组的元素个数。与真实值误差在10 ^ -5以内的答案将被视作正确答案。


# def medianSlidingWindow(nums, k):  暴力
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: List[float]
#     """
#     res = []
#     if k % 2 == 0:
#         n1, n2 = k // 2, k // 2 - 1
#     else:
#         n = k // 2
#     l, r = 0, k
#     if k % 2 == 0:
#         while r <= len(nums):
#             s = sorted(nums[l:r])
#             res.append((s[n1] + s[n2]) / 2)
#             l += 1
#             r += 1
#         return res
#     if k % 2 != 0:
#         while r <= len(nums):
#             s = sorted(nums[l:r])
#             res.append(s[n])
#             l += 1
#             r += 1
#         return res

class Solution:  # 正确做法 优先队列
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        window = []

        ans = []
        for i in range(n):
            idx = bisect_left(window, nums[i])
            window[idx:idx] = [nums[i]]

            if len(window) > k:
                q = nums[i - k]
                idx = bisect_left(window, q)
                window[idx : idx + 1] = []

            if len(window) == k:
                median = (window[k // 2] + window[(k - 1) // 2]) / 2
                ans.append(median)

        return ans

# print(medianSlidingWindow([1,4,2,3], 4))


