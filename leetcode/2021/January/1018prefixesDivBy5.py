# 1018.可被5整除的二进制前缀
# 给定由若干0和1组成的数组A。我们定义N_i：从A[0]到A[i]的第i个子数组被解释为一个二进制数（从最高有效位到最低有效位）。
# 返回布尔值列表answer，只有当N_i可以被5整除时，答案answer[i]为true，否则为false。
# 示例 1：
# 输入：[0, 1, 1]
# 输出：[true, false, false]
# 解释：输入数字为0, 01, 011；也就是十进制中的0, 1, 3 。只有第一个数可以被5整除，因此answer[0] 为真。
#
# 示例2：
# 输入：[1, 1, 1]
# 输出：[false, false, false]
#
# 示例3：
# 输入：[0, 1, 1, 1, 1, 1]
# 输出：[true, false, false, false, true, false]
#
# 示例4：
# 输入：[1, 1, 1, 0, 1]
# 输出：[false, false, false, false, false]

# 提示：
# 1 <= A.length <= 30000  A[i]为0或1

class Solution(object):  # 暴力做法 也就python才不会溢出了
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        r = ''
        res = []
        for a in A:
            r = r + str(a)
            b = int(r, 2) % 5
            if b == 0:
                res.append(True)
            else:
                res.append(False)
        return res

# class Solution:  # 真正的解法
#     def prefixesDivBy5(self, A: List[int]) -> List[bool]:
#         res=[]
#         temp=0
#         for i in A:
#             temp=((temp<<1)+i)%5
#             res.append(temp==0)
#         return res
