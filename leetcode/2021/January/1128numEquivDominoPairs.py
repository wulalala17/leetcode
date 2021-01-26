# 1128. 等价多米诺骨牌对的数量
# 给你一个由一些多米诺骨牌组成的列表dominoes。
# 如果其中某一张多米诺骨牌可以通过旋转0度或180度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。
# 形式上，dominoes[i] = [a, b]和dominoes[j] = [c, d]等价的前提是a == c且b == d，或是a == d且b == c。
# 在0 <= i < j < dominoes.length的前提下，找出满足dominoes[i]和dominoes[j]等价的骨牌对(i, j)的数量。
# 示例：
# 输入：dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
# 输出：1
#
# 提示：
# 1 <= dominoes.length <= 40000
# 1 <= dominoes[i][j] <= 9
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        dic = {}
        res = 0
        for d in dominoes:
            if (d[0], d[1]) not in dic and (d[1], d[0]) not in dic:
                dic[(d[0], d[1])] = 1
                continue
            if (d[0], d[1]) in dic:
                dic[(d[0], d[1])] += 1
                continue
            if (d[1], d[0]) in dic:
                dic[(d[1], d[0])] += 1
                continue

        for k in dic:
            if dic[k] > 1:
                res += dic[k] * (dic[k] - 1) // 2
        return res


