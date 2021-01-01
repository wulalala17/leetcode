def maxLengthBetweenEqualCharacters(s):
    m = [0 for _ in range(26)]
    n = []  # 记录下标
    for i in s:
        m[ord(i)-97] += 1
    flag = 0
    for i in m:
        if i >= 2:
            flag = 1
    if flag == 0:
        return -1
