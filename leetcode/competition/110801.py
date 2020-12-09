
def getMaximumGenerated(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    nums = [0, 1]
    for i in range(2, n+1):
        if i % 2 ==0:
            nums.append(nums[i//2])
        else:
            nums.append(nums[i//2] + nums[i//2 + 1])
    return max(nums)

print(getMaximumGenerated(7))