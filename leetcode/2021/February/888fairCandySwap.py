# 888. 公平的糖果棒交换
# 爱丽丝和鲍勃有不同大小的糖果棒：A[i]是爱丽丝拥有的第i根糖果棒的大小，B[j]是鲍勃拥有的第j根糖果棒的大小。
# 因为他们是朋友，所以他们想交换一根糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）
# 返回一个整数数组ans，其中 ans[0]是爱丽丝必须交换的糖果棒的大小，ans[1]是 Bob 必须交换的糖果棒的大小。
# 如果有多个答案，你可以返回其中任何一个。保证答案存在。
# 示例1：
# 输入：A = [1, 1], B = [2, 2]
# 输出：[1, 2]
#
# 示例2：
# 输入：A = [1, 2], B = [2, 3]
# 输出：[1, 2]
#
# 示例3：
# 输入：A = [2], B = [1, 3]
# 输出：[2, 3]
#
# 示例4：
# 输入：A = [1, 2, 5], B = [2, 4]
# 输出：[5, 4]
#
# 提示：
# 1 <= A.length <= 10000
# 1 <= B.length <= 10000
# 1 <= A[i] <= 100000
# 1 <= B[i] <= 100000
# 保证爱丽丝与鲍勃的糖果总量不同。答案肯定存在。
class Solution(object):  # 差点超时
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumOfA = sum(A)
        sumOfB = sum(B)
        if sumOfA > sumOfB:
            x = sumOfA - sumOfB
            for a in A:
                if (2 * a - x) / 2 in B:
                    return [a, (2 * a - x) / 2]
        else:
            x = sumOfB - sumOfA
            for a in A:
                if (2 * a + x) / 2 in B:
                    return [a, (2 * a + x) / 2]
