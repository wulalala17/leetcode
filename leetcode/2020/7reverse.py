def reverse(zhengshu):
    if zhengshu == 0:
        return 0
    f = 0
    n = str(zhengshu)
    if n[0] == '-':
        n = n[1:]
        f = 1
    while n[-1:] == '0':
        n = n[:-1]
    res = n[::-1]
    if int(res) >= 2 ** 31 - 1:
        return 0
    if f == 1:
        res = '-' + res
    return int(res)


k = input()
print(reverse(k))