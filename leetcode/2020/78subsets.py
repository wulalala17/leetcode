# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。
# 示例:
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


def subsets(nums):
    res = []
    res.append([])
    if len(nums) == 0:
        return res
    def f(l, n, curres):
        if len(curres) == n:
            res.append(curres[:]) # 注意这里不要写curres 不然会一直加入空集
            return
        for i in range(len(l)):
            curres.append(l[i])
            f(l[i+1:], n, curres)
            curres.pop()
        return res
    for j in range(1, len(nums)+1):
        f(nums, j, [])
        print("现在结果：", res)
    return res

# 别人的写法
# def subsets(self, nums):
#     res = [[]]
#     for i in range(len(nums) - 1, -1, -1):
#         for subres in res[:]: res.append(subres + [nums[i]])
#
#     return res





subsets([1,2,3])