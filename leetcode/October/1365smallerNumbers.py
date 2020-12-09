# 1365.有多少小于当前数字的数字
# 给你一个数组nums，对于其中每个元素nums[i]，请你统计数组中比它小的所有数字的数目。换而言之，对于每个nums[i]你必须计算出有效的j的数量，其中j满足j != i且nums[j] < nums[i] 。
# 以数组形式返回答案。
# 示例
# 1：
# 输入：nums = [8, 1, 2, 2, 3]
# 输出：[4, 0, 1, 1, 3]
# 解释：对于nums[0] = 8存在四个比它小的数字：（1，2，2和3）。对于nums[1] = 1不存在比它小的数字。对于nums[2] = 2存在一个比它小的数字：（1）。对于nums[3] = 2存在一个比它小的数字：（1）。对于nums[4] = 3存在三个比它小的数字：（1，2和2）。
#
# 示例2：
# 输入：nums = [6, 5, 4, 8]
# 输出：[2, 1, 0, 3]
# 示例3：
# 输入：nums = [7, 7, 7, 7]
# 输出：[0, 0, 0, 0]
# 提示：
# 2 <= nums.length <= 500
# 0 <= nums[i] <= 100
def smallerNumbersThanCurrent(nums):
    n = sorted(nums)
    d = {}
    res = []
    k = 0
    for i in n:
        if not i in d:
            d[i] = k
        k += 1
    for i in nums:
        res.append(d[i])
    return res

a=[8,1,2,2,3]
print(smallerNumbersThanCurrent(a))
