def stoneGameVII(stones):
    """
    :type stones: List[int]
    :rtype: int
    """
    alice, bob = 0, 0
    dp = [[0]*len(stones) for i in range(len(stones))]
    n = len(stones)
    for i in range(n-1):
        dp[i][i+1] = max(stones[i], stones[i+1])
    d = {}
    for i in range(2, n):  # 二者差值
        for j in range(n-i):  # 第一维坐标
            if d.get((j+1, j+i+1), -1) == -1:
                d[(j+1, j+i+1)] = sum(stones[j+1:j+i+1])
            if d.get((j, j+i), -1) == -1:
                d[(j, j+i)] = sum(stones[j:j+i])
            k1 = d[(j+1, j+i+1)] - dp[j+1][j+i]  # 选第一个数
            k2 = d[(j, j+i)] - dp[j][j+i-1]  # 选最后一个数
            dp[j][j+i] = max(k1, k2)
    return dp[0][n-1]
s = [1, 3, 5, 7, 9]
b = [5,3,1,4,2]
a = [7,90,5,1,100,10,10,2]
print(stoneGameVII(a))

    





