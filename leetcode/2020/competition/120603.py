def concatenatedBinary(n):
    """
    :type n: int
    :rtype: int
    """
    res = ''
    for i in range(1, n+1):
        n = str(bin(i))
        for i in range(2, len(n)):
            res += n[i]
    k = int(res, 2)
    k = k % (10 ** 9 + 7)
    return k
print(concatenatedBinary(3))