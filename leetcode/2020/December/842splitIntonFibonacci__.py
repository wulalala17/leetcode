# 842.
# 将数组拆分成斐波那契序列给定一个数字字符串S，比如S = "123456579"，我们可以将它分成斐波那契式的序列[123, 456, 579]。
# 形式上，斐波那契式序列是一个非负整数列表F，且满足：0 <= F[i] <= 2 ^ 31 - 1，（也就是说，每个整数都符合32位有符号整数类型）；F.length >= 3；
# 对于所有的0 <= i < F.length - 2，都有F[i] + F[i + 1] = F[i + 2]成立。另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字
# 0本身。返回从S拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回[]。
# 示例1：
# 输入："123456579"
# 输出：[123, 456, 579]
# 示例2:
# 输入: "11235813"
# 输出: [1, 1, 2, 3, 5, 8, 13]
# 示例3：
# 输入: "112358130"
# 输出: []
# 解释: 这项任务无法完成。
# 示例4：
# 输入："0123"
# 输出：[]
# 解释：每个块的数字不能以零开头，因此"01"，"2"，"3"不是有效答案。
# 示例5：
# 输入: "1101111"
# 输出: [110, 1, 111]
# 解释: 输出[11, 0, 11, 11]也同样被接受。
# 提示：1 <= S.length <= 200字符串S中只含有数字。


# 想不出来 大概知道是回溯。不知道怎么处于字符串和数字的转换
# class Solution(object):
#     def splitIntoFibonacci(self, S):
#         """
#         :type S: str
#         :rtype: List[int]
#         """
#
#         def feibo(s, fir, sec):
#
#         limit = (len(S) - 1) // 2
#         for i in range(limit, 0, -1):
#             pre = int(S[0:i])
#             for j in range(limit, 0, -1):
#                 cur = int(S[i:i + j])
#                 if feibo(S, pre, cur):

# def splitIntoFibonacci(self, S: str) -> List[int]:
#     ans = list()
#
#     def backtrack(index: int):
#         if index == len(S):
#             return len(ans) >= 3
#
#         curr = 0
#         for i in range(index, len(S)):
#             if i > index and S[index] == "0":
#                 break
#             curr = curr * 10 + ord(S[i]) - ord("0")
#             if curr > 2 ** 31 - 1:
#                 break
#
#             if len(ans) < 2 or curr == ans[-2] + ans[-1]:
#                 ans.append(curr)
#                 if backtrack(i + 1):
#                     return True
#                 ans.pop()
#             elif len(ans) > 2 and curr > ans[-2] + ans[-1]:
#                 break
#
#         return False
#
#     backtrack(0)
#     return ans
#
#
# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / split - array - into - fibonacci - sequence / solution / jiang - shu - zu - chai - fen - cheng - fei - bo - na - qi - ts6c /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# class Solution:  这个回溯更好理解
#     def splitIntoFibonacci(self, S: str) -> List[int]:
#         def backtrack(cur, temp_state):
#             if len(temp_state) >= 3 and cur == n:  # 退出条件
#                 self.res = temp_state
#                 return
#             if cur == n:  # 剪枝
#                 return
#             for i in range(cur, n):
#                 if S[cur] == "0" and i > cur:  # 当数字以0开头时,应该跳过
#                     return
#                 if int(S[cur: i+1]) > 2 ** 31 - 1 or int(S[cur: i+1]) < 0:  # 剪枝
#                     continue
#                 if len(temp_state) < 2:
#                     backtrack(i+1, temp_state + [int(S[cur: i+1])])
#                 else:
#                     if int(S[cur: i+1]) == temp_state[-1] + temp_state[-2]:
#                         backtrack(i+1, temp_state + [int(S[cur: i+1])])
#
#         n = len(S)
#         self.res = []
#         backtrack(0, [])
#         return self.res
#
# 作者：azad-u
# 链接：https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence/solution/hui-su-jie-jue-tao-mo-ban-ji-ke-by-azad-u/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。