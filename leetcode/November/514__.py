def findRotateSteps(ring, key):
    """
    :type ring: str
    :type key: str
    :rtype: int
    """
    res = 0
    cur = 0
    i = 0
    while i < len(key):
        l, r = cur, cur
        while ring[l] != key[i] and ring[r] != key[i]:
            res += 1
            if l == 0:
                l = len(ring) - 1
            else:
                l -= 1
            if r == len(ring) - 1:
                r = 0
            else:
                r += 1
        if ring[l] == key[i]:
            cur = l
            res += 1
        else:
            cur = r
            res += 1
        i += 1
a = 'godding'
b = 'gd'
c = 'iotfo'
d = 'fioot'
print(findRotateSteps(c, d))

# ringDict = collections.defaultdict(list)  官方题解 DP 不会写
# for i, v in enumerate(ring):
#     ringDict[v].append(i)
#
# n, m = len(key), len(ring)
# dp = [[sys.maxsize for _ in range(m)] for _ in range(n)]
#
# for i in ringDict[key[0]]:
#     dp[0][i] = min(i, m - i) + 1
#
# for i in range(1, n):
#     for j in ringDict[key[i]]:
#         for k in ringDict[key[i - 1]]:
#             dp[i][j] = min(dp[i][j], dp[i - 1][k] + min(int(math.fabs(j - k)), m - int(math.fabs(j - k))) + 1)
# ans = sys.maxsize
# for v in dp[n - 1]:
#     ans = min(ans, v)
# return ans