# 861.
# 翻转矩阵后的得分
#
# 有一个二维矩阵A其中每个元素的值为0或1 。移动是指选择任一行或列，并转换该行或列中的每一个值：将所有0都更改为1，将所有1都更改为0。
# 在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。返回尽可能高的分数。
# 示例：
# 输入：[[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
# 输出：39
# 解释：转换为[[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]]0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
# 提示：
# 1 <= A.length <= 20
# 1 <= A[0].length <= 20 A[i][j]是0或1


class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def change(martrix, row = -1, column = -1):
            if row != -1:
                for i in range(len(martrix[row])):
                    if martrix[row][i] == 0:
                        martrix[row][i] = 1
                    else:
                        martrix[row][i] = 0
            if column != -1:
                for i in range(len(martrix)):
                    if martrix[i][column] == 0:
                        martrix[i][column] = 1
                    else:
                        martrix[i][column] = 0
            return martrix
        for i in range(len(A)):
            if A[i][0] == 0:  # 第i行第0列为0，就改变这行
                A = change(A, i, -1)
        numOfZero, numOfOne = 0, 0
        for i in range(1, len(A[0])):
            numOfZero, numOfOne = 0, 0
            for j in range(0, len(A)):
                if A[j][i] == 0:
                    numOfZero += 1
                else:
                    numOfOne += 1
            if numOfZero > numOfOne:  # 第i列0的个数比1多，就改变这列
                A = change(A, -1, i)
        res = 0
        cur = ''
        for i in range(len(A)):
            cur = ''
            for j in range(len(A[0])):
                cur += str(A[i][j])
            res += int(cur, 2)
        return res

    # '''
    # 思路：
    # 可以这样看，n*m的每个格子都具有一个权重，其中每一行权重都自左向右递减，
    # 为使总和最大则尽可能使权重大的格子填“1”。最左边一列权重最大，所以总可以通过
    # 行翻转使左边第一列全都置“1”，后面就不能再使用行翻转了，以免破环当前的结构，
    # 所以考虑列翻转。对于除最左边第一列外的每一列，总可以通过列翻转使得该列“1”
    # 的个数不小于“0”的个数。最后所有填“1”的格子的权重和即为答案。
    # '''
    #
    # class Solution:
    #     def matrixScore(self, A: List[List[int]]) -> int:
    #         n, m = len(A), len(A[0])
    #         for i in range(n):
    #             if A[i][0] == 0:
    #                 for j in range(m):
    #                     A[i][j] = 1 ^ A[i][j]
    #         sum = 0
    #         for i in zip(*A):
    #             m -= 1
    #             sum += 2 ** m * max(i.count(1), i.count(0))
    #         return sum