# 135. 分发糖果
# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
# 你需要按照以下要求，帮助老师给这些孩子分发糖果：
#
#     每个孩子至少分配到 1 个糖果。
#     相邻的孩子中，评分高的孩子必须获得更多的糖果。
#
# 那么这样下来，老师至少需要准备多少颗糖果呢？
# 示例 1:
# 输入: [1,0,2]
# 输出: 5
# 解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
#
# 示例 2:
# 输入: [1,2,2]
# 输出: 4
# 解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
#      第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
class Solution(object):  # 贪心两次，分别处理递增和递减的状况，看了评论才想出来，为什么自己想得那么复杂
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 1:
            return 1
        if n == 0:
            return 0
        res = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i+1]+1, res[i])
        return sum(res)