# 1423. 可获得的最大点数
# 几张卡牌排成一行，每张卡牌都有一个对应的点数。点数由整数数组cardPoints给出。
# 每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿k张卡牌。
# 你的点数就是你拿到手中的所有卡牌的点数之和。
# 给你一个整数数组cardPoints和整数k，请你返回可以获得的最大点数。
# 示例1：
# 输入：cardPoints = [1, 2, 3, 4, 5, 6, 1], k = 3
# 输出：12
# 解释：第一次行动，不管拿哪张牌，你的点数总是1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为1 + 6 + 5 = 12 。
#
# 示例2：
# 输入：cardPoints = [2, 2, 2], k = 2
# 输出：4
# 解释：无论你拿起哪两张卡牌，可获得的点数总是4 。
#
# 示例3：
# 输入：cardPoints = [9, 7, 7, 9, 7, 7, 9], k = 7
# 输出：55
# 解释：你必须拿起所有卡牌，可以获得的点数为所有卡牌的点数之和。
#
# 示例4：
# 输入：cardPoints = [1, 1000, 1], k = 1
# 输出：1
# 解释：你无法拿到中间那张卡牌，所以可以获得的最大点数为1 。
#
# 示例5：
# 输入：cardPoints = [1, 79, 80, 1, 1, 1, 200, 1], k = 3
# 输出：202
#
# 提示：
# 1 <= cardPoints.length <= 10 ^ 5
# 1 <= cardPoints[i] <= 10 ^ 4
# 1 <= k <= cardPoints.length

class Solution(object):  # 前缀和 只击败10%
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        if len(cardPoints) == 0:
            return 0
        if len(cardPoints) == 1 and k >= 1:
            return cardPoints[0]
        if len(cardPoints) <= k:
            return sum(cardPoints)
        prefix = [cardPoints[0]]
        suffix = [cardPoints[-1]]
        for i in range(1, len(cardPoints)):
            prefix.append(prefix[-1] + cardPoints[i])
        for i in range(len(cardPoints) - 2, -1, -1):
            suffix.append(suffix[-1] + cardPoints[i])
        res = 0
        i = 0
        while i < k:
            if i == k - 1:
                res = max(res, prefix[i])
                break
            res = max(res, prefix[i] + suffix[k - i - 2])
            i += 1
        res = max(res, suffix[k - 1])
        return res


