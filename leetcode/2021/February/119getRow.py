# 119. 杨辉三角 II
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
# 输入: 3
# 输出: [1,3,3,1]
# 进阶：
# 你可以优化你的算法到 O(k) 空间复杂度吗？

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        res = []
        res.append([1])
        for i in range(rowIndex):
            r0 = []
            for j in range(len(res[-1])-1):
                r0.append(res[-1][j] + res[-1][j+1])
            r = [1] + r0 + [1]
            res.append(r)
        return res[rowIndex]

# /** 牛逼做法
#  * 获取杨辉三角的指定行
#  * 直接使用组合公式C(n,i) = n!/(i!*(n-i)!)
#  * 则第(i+1)项是第i项的倍数=(n-i)/(i+1);
#  */
# public List<Integer> getRow(int rowIndex) {
#         List<Integer> res = new ArrayList<>(rowIndex + 1);
#         long cur = 1;
#         for (int i = 0; i <= rowIndex; i++) {
#             res.add((int) cur);
#             cur = cur * (rowIndex-i)/(i+1);
#         }
#         return res;
# }