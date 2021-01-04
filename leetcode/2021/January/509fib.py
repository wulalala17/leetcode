# 509.斐波那契数
# 斐波那契数，通常用F(n)表示，形成的序列称为斐波那契数列 。该数列由0和1开始，后面的每一项数字都是前面两项数字的和。也就是：
# F(0) = 0，F(1) = 1 F(n) = F(n - 1) + F(n - 2)，其中n > 1
# 给你n ，请计算F(n) 。
# 示例1：
# 输入：2
# 输出：1
# 解释：F(2) = F(1) + F(0) = 1 + 0 = 1
#
# 示例2：
# 输入：3
# 输出：2
# 解释：F(3) = F(2) + F(1) = 1 + 1 = 2
#
# 示例3：
# 输入：4
# 输出：3
# 解释：F(4) = F(3) + F(2) = 2 + 1 = 3


class Solution(object):  # 只想起了数组法，没想到替换法，替换法常数空间，效率更高
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        n1, n2 = 0, 1
        times = 1
        res = 0
        if n == 1:
            return 1
        if n == 0:
            return 0
        while times < n:
            res = n1 + n2
            n1 = n2
            n2 = res
            times += 1
        return res

        # res = [0, 1]
        # if n >= 2:
        #     for i in range(2, n+1):
        #         a = res[-1] + res[-2]
        #         res.append(a)
        # return res[n]