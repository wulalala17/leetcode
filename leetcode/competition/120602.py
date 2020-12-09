def maxOperations(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums = sorted(nums)
    i, j =0, len(nums)-1
    res = 0
    while i < j:
        if nums[i] + nums[j] < k:
            i += 1
            continue
        if nums[i] + nums[j] == k:
            res += 1
            i += 1
            j -= 1
            continue
        if nums[i] + nums[j] > k:
            j -= 1
            continue
    return res
    # def findx(nums, start, n):
    #     for i in range(start, len(nums)):
    #         if nums[i] == n:
    #             return i
    #     return -1
    #
    # n = len(nums)
    # i = 0
    # res = 0
    # while i < n:
    #     r = k - nums[i]
    #     if r in nums:
    #         idx = findx(nums, i+1, r)
    #         if idx != -1:
    #             nums.remove(nums[i])
    #             nums.remove(r)
    #             res += 1
    #             n = len(nums)
    #             continue
    #     i += 1
    # return res

a = [3,1,3,4,3]
b = 6
c = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
d = 2
print(maxOperations(c,d))