def maxValue(n, index, maxSum):  # 从index往左右两边填 当时没想到
    """
    :type n: int
    :type index: int
    :type maxSum: int
    :rtype: int
    """
    # nums = [maxSum // n for i in range(n)]
    # r = maxSum % n
    # for i in range(index, 2, n):
    #     if r > 0:
    #         nums[i] += 1
    #         r -= 1
    #     if r == 0:
    #         break
    # for i in range(0, 2, index+1):
    #     if r > 0:
    #         nums[i] += 1
    #         r -= 1
    #     if r == 0:
    #         break
    # return nums[index]
    left = index
    right = index
    res = 1
    diff = maxSum - n
    if diff == 0:
        return 1
    while diff >= right - left + 1:
        diff -= (right - left + 1)
        if left > 0:
            left -= 1
        if right < n-1:
            right += 1
        res += 1
        if left == 0 and right == n-1:
            res += diff // n
            return res
    return res

n = 4
index = 2
maxSum = 6
print(maxValue(n,index,maxSum))