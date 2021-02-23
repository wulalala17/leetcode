# 1052. 爱生气的书店老板
# 今天，书店老板有一家店打算试营业customers.length分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
# 在某些时候，书店老板会生气。 如果书店老板在第i分钟生气，那么grumpy[i] = 1，否则
# grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。
# 书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续X分钟不生气，但却只能使用一次。
# 请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
#
# 示例：
# 输入：customers = [1, 0, 1, 2, 1, 1, 7, 5], grumpy = [0, 1, 0, 1, 0, 1, 0, 1], X = 3
# 输出：16
# 解释：书店老板在最后 3 分钟保持冷静。感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
#
# 提示：
# 1 <= X <= customers.length == grumpy.length <= 20000
# 0 <= customers[i] <= 1000
# 0 <= grumpy[i] <= 1

# class Solution { # 换用JAVA 暴力法才过了
#     public int maxSatisfied(int[] customers, int[] grumpy, int X) {
#         int res = 0;
#         for(int i =0;i<customers.length;i++){
#             if (grumpy[i] == 0)
#                 res += customers[i];
#         }
#         int r0 = res;
#         int r1;
#         for(int i=0; i<customers.length-X+1;i++){
#             r1 = r0;
#             for(int j =0;j<X;j++){
#                 if(grumpy[i+j] == 1){
#                     r1 += customers[i+j];
#                     if(r1>res)
#                         res = r1;
#                 }
#             }
#         }
#         return res;
#     }
# }

class Solution(object):  # 评论里的On写法
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        res = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                res += customers[i]
                customers[i] = 0
        r = customers[0]
        r0 = r
        for i in range(1, len(customers)):
            if i < X:
                r += customers[i]
            else:
                r = r - customers[i-X] + customers[i]
            r0 = max(r0, r)
        return res + r0

        # n = len(customers) 官方题解
        # total = sum(c for c, g in zip(customers, grumpy) if g == 0)
        # maxIncrease = increase = sum(c * g for c, g in zip(customers[:X], grumpy[:X]))
        # for i in range(X, n):
        #     increase += customers[i] * grumpy[i] - customers[i - X] * grumpy[i - X]
        #     maxIncrease = max(maxIncrease, increase)
        # return total + maxIncrease
