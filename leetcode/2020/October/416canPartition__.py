# 416.分割等和子集
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 注意:
# 每个数组中的元素不会超过100  数组的大小不会超过200
# 示例
# 1:
# 输入: [1, 5, 11, 5]
# 输出: tru
# 解释: 数组可以分割成[1, 5, 5]
# 和[11].
# 示例
# 2:
# 输入: [1, 2, 3, 5]
# 输出: false
# 解释: 数组不能分割成两个元素和相等的子集.
def canPartition(nums):
    def sumoflist(nums):
        sum = 0
        for i in nums:
            sum += i
        return sum
    s = sumoflist(nums)
    if s % 2 !=0:
        return False
    halfofsum = s//2
    nums = sorted(nums)

    res = []
    def baceTrace(l, target, sum, startIndex): # 超时
        if sum > target:
            return
        if sum == target:
            res.append(1)
            return
        for i in range(startIndex, len(l)):
            sum += l[i]
            if 1 in res:
                return
            baceTrace(l, target, sum, i+1)
            sum -= l[i]
            if 1 in res:
                return
    baceTrace(nums, halfofsum, 0, 0)
    if 1 in res:
        return True
    else:
        return False


    # k = 0
    # for i in range(len(nums)-1, -1, -1):
    #     k += nums[i]
    #     if k == halfofsum:
    #         return True
    #     elif k < halfofsum:
    #         continue
    #     else:
    #         return False

a = [1,5,11,5]
b = [1,1,2,2]
print(canPartition(b))


# class Solution: 官方题解
#     def canPartition(self, nums: List[int]) -> bool:
#         n = len(nums)
#         if n < 2:
#             return False
#
#         total = sum(nums)
#         if total % 2 != 0:
#             return False
#
#         target = total // 2
#         dp = [True] + [False] * target
#         for i, num in enumerate(nums):
#             for j in range(target, num - 1, -1):
#                 dp[j] |= dp[j - num]
#
#         return dp[target]

# 看起来更牛逼的解法
# https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/0-1bei-bao-wen-ti-by-jhmgo/