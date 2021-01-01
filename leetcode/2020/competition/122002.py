#
# def maximumUniqueSubarray(nums): # 疯狂超时
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     d = {}
#     res = 0
#     i = 0
#     j = 0
#     set = set(nums)
#     nm = sum(set)
#     while i <= len(nums)-1:
#         if nums[i] not in d:
#             d[nums[i]] = i
#             i += 1
#         else:
#             s = sum(nums[j:i])
#             if s == nm:
#                 return s
#             if s > res:
#
#                 res = s
#             j = d[nums[i]] + 1
#             d = {}
#             for k in range(j, i+1):
#                 d[nums[k]] = k
#             i += 1
#
#     if sum(nums[j:]) > res:
#         res = sum(nums[j:])
#     return res


def maximumUniqueSubarray(nums):  # 改成这样才过了，但是耗时很久
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    res, j, k = 0, 0, 0
    for i in range(1, len(nums)):
        if nums[i] not in nums[j:i]:
            continue
        else:
            k = sum(nums[j:i])
            if k > res:
                res = k
            j = nums.index(nums[i], j, i) + 1
    k = sum(nums[j:])
    if k > res:
        res = k
    return res

print(maximumUniqueSubarray([5,2,2,2,2,2,2,2]))