def sumOddLengthSubarrays(arr):
    def sumofl(l, n):
        s = 0
        k = len(l)-n # 最后一位
        for i in range(k+1):
            f = 1
            m = i
            while f<=n:
                s += l[m]
                f += 1
                m += 1
        return s

    res = []
    maxl = len(arr)
    if len(arr)%2==0:
        maxl = len(arr)-1
    for i in range(1, maxl+1, 2):
        res.append(sumofl(arr, i))
    ss = 0
    for i in res:
        ss += i
    return ss


# [1,4,2,5,3]
# [1,2]
# [10,11,12]
print(sumOddLengthSubarrays([10,11,12]))


