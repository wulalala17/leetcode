def minOperations(nums, x):
    """
    :type nums: List[int]
    :type x: int
    :rtype: int
    """
    if min(nums) > x or sum(nums) < x:
        return -1
    l1 = 0
    l2 = len(nums) - 1
    sumofx = 0
    res = 0

    while sumofx < x:
        sumofx += nums[l1]
        res += 1
        if sumofx > x:
            break
        l1 += 1
        if sumofx == x:
            return res
    sumofx -= nums[l1]
    l1 -= 1
    res -= 1
    while l1 >= 0:
        if sumofx == x:
            return res
            break
        sumofx += nums[l2]
        res += 1


        if sumofx > x:
            sumofx -= nums[l1]
            l1 -= 1
            res -= 1
        else:
            l2 -= 1
    return res

a = [3,2,20,1,1,3]
b = 10
c = [1,1,4,2,3]
print(minOperations(c, 5))


def minOperation(nums, x):  # 别人的哈希与前缀和写法
    leftsum = 0  # 左前缀和
    ld = {}
    for i in range(len(nums)):
        leftsum += nums[i]
        if leftsum > x:
            break
        ld[leftsum] = i + 1

    rightsum = 0  # 右前缀和
    rd = {}
    for i in range(len(nums) - 1, -1, -1):
        rightsum += nums[i]
        if rightsum > x:
            break
        rd[rightsum] = len(nums) - i
    cur = min(ld.get(x, float('inf')), rd.get(x, float('inf')))  # 比较只取一边满足条件的步长
    for lsum in ld:
        if x-lsum in rd:
            lrc = rd[x-lsum] + ld[lsum]
            if lrc <= len(nums):
                cur = min(cur, lrc)
    return cur if cur != float('inf') else -1