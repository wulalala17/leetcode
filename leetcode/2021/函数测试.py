def judge(num):
    return True if num == 0 or num & (num - 1) == 0 else False
print(judge(0))
print(judge(1))
print(judge(2))
print(judge(3))
print(judge(4))
print(judge(5))
print(judge(6))
print(judge(7))
print(judge(8))
n = 5
p1 = list(range(n))
p2 = [i for i in range(n)]
print(p1)
print(p2)
a = [1,2,3,3,4,110,110,110]
print(max(a, key=a.count))

def minCut(s):
    n = len(s)
    g = [[True] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]
    print(g)

def minCut2(s):
    n = len(s)
    g = [[True] * n for _ in range(n)]

    for i in range(0, n):
        for j in range(i + 1, n):
            g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]
    print(g)

minCut("abcddcba")
minCut2("abcddcba")