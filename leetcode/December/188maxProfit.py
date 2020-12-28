# 188.买卖股票的最佳时机IV
# 给定一个整数数组prices ，它的第i个元素prices[i]是一支给定的股票在第i天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成k笔交易。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 示例1：
# 输入：k = 2, prices = [2, 4, 1]
# 输出：2
# 解释：在第1天(股票价格=2)的时候买入，在第 2天(股票价格=4)的时候卖出，这笔交易所能获得利润 = 4 - 2 = 2 。

# 示例2：
# 输入：k = 2, prices = [3, 2, 6, 5, 0, 3]
# 输出：7
# 解释：在第2天(股票价格=2)的时候买入，在第3天(股票价格=6)的时候卖出, 这笔交易所能获得利润 = 6 - 2 = 4 。随后，在第5天(股票价格=0)的时候买入，在第6天(股票价格=3)
# 的时候卖出, 这笔交易所能获得利润 = 3 - 0 = 3 。

# 提示：
# 0 <= k <= 109
# 0 <= prices.length <= 1000
# 0 <= prices[i] <= 1000


def maxProfit(k, prices):  # 想当然的错误解法，没考虑到在区间[i,j]次数不一样，最大利益也不一样
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2:
        return 0
    res = []
    f = 0  # 0买进 1卖出
    buy = prices[0]
    sell = 0
    for i in range(1, len(prices)):
        if f == 0:
            if prices[i] <= buy:
                buy = prices[i]
                continue
            else:
                sell = prices[i]
                f = 1
        else:
            if prices[i] >= sell:
                sell = prices[i]
                continue
            else:
                res.append(sell-buy)
                buy = prices[i]
                f = 0
    if f == 1:
        res.append(sell-buy)
    res.sort(reverse=True)
    j = 0
    r = 0
    if len(res) == 0 or k == 0:
        return 0
    while j < len(res) and j < k:
        r += res[j]
        j += 1
    return r

k = 2
prices = [1,2,4,2,5,7,2,4,9,0]
print(maxProfit(k, prices))


class Solution(object):  # 官方DP解法 好难
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        buy = [[0] * (k + 1) for _ in range(n)]
        sell = [[0] * (k + 1) for _ in range(n)]

        buy[0][0], sell[0][0] = -prices[0], 0
        for i in range(1, k + 1):
            buy[0][i] = sell[0][i] = float("-inf")

        for i in range(1, n):
            buy[i][0] = max(buy[i - 1][0], sell[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i]);

        return max(sell[n - 1])
