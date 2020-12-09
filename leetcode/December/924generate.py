# 生成杨辉三角
class Solution:
    def generate(numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1], [1,1]]
        while len(res) < numRows:
            cur = res[-1]
            new = []
            for i in range(len(cur) - 1):
                new.append(cur[i]+cur[i+1])
            new.append(1)
            new.insert(0, 1)
            res.append(new)
        return res
# def generate(self, numRows): 别人的写法
#     """
#     :type numRows: int
#     :rtype: List[List[int]]
#     """
#     result = []
#     for i in range(numRows):
#         now = [1] * (i + 1)
#         if i >= 2:
#             for n in range(1, i):
#                 now[n] = pre[n - 1] + pre[n]
#         result += [now]
#         pre = now
#     return result

# class Solution: 官方题解
#     def generate(self, numRows: int) -> List[List[int]]:
#         ret = list()
#         for i in range(numRows):
#             row = list()
#             for j in range(0, i + 1):
#                 if j == 0 or j == i:
#                     row.append(1)
#                 else:
#                     row.append(ret[i - 1][j] + ret[i - 1][j - 1])
#             ret.append(row)
#         return ret
#
# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/pascals-triangle/solution/yang-hui-san-jiao-by-leetcode-solution-lew9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。