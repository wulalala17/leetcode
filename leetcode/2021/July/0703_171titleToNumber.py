# 171. Excel表列序号
#
# 给定一个Excel表格中的列名称，返回其相应的列序号。
#
# 例如，
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
#
# 示例 1:
#
# 输入: "A"
# 输出: 1
#
# 示例 2:
#
# 输入: "AB"
# 输出: 28
#
# 示例 3:
#
# 输入: "ZY"
# 输出: 701

class Solution(object):  # 上个月刚写的题，26进制
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        l = len(columnTitle)
        if l == 1:
            return ord(columnTitle[0]) - 64
        res = 0
        for i in range(l - 1):
            res = res + (ord(columnTitle[i]) - 64) * 26 ** (l - 1 - i)
        res += ord(columnTitle[-1]) - 64
        return res



