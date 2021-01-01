def sortString(s):
    """
    :type s: str
    :rtype: str
    """
    co = [0 for _ in range(26)]
    for ch in s:
        co[ord(ch) - 97] += 1
    print(co)

    # c = collections.Counter(s)
    # l1 = list(c.keys())
    # l2 = list(c.values())
    res = ''

    def isZero(l):
        for ll in l:
            if ll != 0:
                return False
        return True

    while True:
        if isZero(co):
            break
        for i in range(26):
            if co[i] != 0:
                res += chr(i + 97)
                co[i] -= 1
            else:
                continue
        for i in range(25, -1, -1):
            if co[i] != 0:
                res += chr(i + 97)
                co[i] -= 1
            else:
                continue
    return res
print(sortString("aaabbbccc"))
