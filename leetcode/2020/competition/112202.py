def getSmallestString(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    res = []
    for i in range(n):
        res.append(26)
    shang = k // 26
    yushu = k % 26
    fs = shang
    s = ""
    if shang == 0:
        res[0] = yushu - (n-1)
        for i in range(1, n):
            res[i] = 1
        for j in range(n-1, -1, -1):
            s += chr(res[j] + 96)
        return s

    while yushu < n - shang:
        yushu += 26
        shang -= 1

    if shang <= len(res):
        res[shang] = yushu - (n - shang - 1)
        for i in range(shang + 1, len(res)):
            res[i] = 1
        print(res)
    for j in range(n - 1, -1, -1):
        s += chr(res[j] + 96)
    return s

n = 3
k = 27
print(getSmallestString(80, 576))