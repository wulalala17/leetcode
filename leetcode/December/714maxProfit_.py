# 714. 买卖股票的最佳时机含手续费
# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
# 返回获得利润的最大值。
# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
# 示例 1:
# 输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出: 8
# 解释: 能够达到的最大利润:
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# 注意:
#     0 < prices.length <= 50000.
#     0 < prices[i] < 50000.
#     0 <= fee < 50000.

class Solution(object):  # 看评论才知道怎么写的贪心
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        minimum = prices[0]
        res = 0
        for i in range(1, len(prices)):  # 完成两次交易的条件是 D-C+B-A-2*fee > D-A-fee 等价于 B > C + fee ，即第二次买入股票价格要比第一次卖出价格更少fee，才买入
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                res += prices[i] - minimum - fee
                minimum = prices[i] - fee
        return res

# class Solution: 官方题解
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#         n = len(prices)
#         sell, buy = 0, -prices[0]
#         for i in range(1, n):
#             sell, buy = max(sell, buy + prices[i] - fee), max(buy, sell - prices[i])
#         return sell
#
# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-han-sh-rzlz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。