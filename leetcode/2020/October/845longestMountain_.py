# 845.数组中的最长山脉
# 我们把数组A中符合下列属性的任意连续子数组B称为 “山脉”：
# B.length >= 3存在0 < i < B.length - 1使得B[0] < B[1] < ...B[i - 1] < B[i] > B[i + 1] > ... > B[B.length - 1]
# （注意：B可以是A的任意子数组，包括整个数组A。）
# 给出一个整数数组
# A，返回最长 “山脉” 的长度。如果不含有 “山脉” 则返回0。

# 示例
# 1：
# 输入：[2, 1, 4, 7, 3, 2, 5]
# 输出：5
# 解释：最长的 “山脉” 是[1, 4, 7, 3, 2]，长度为5。
# 示例
# 2：
# 输入：[2, 2, 2]
# 输出：0
# 解释：不含 “山脉”。
def longestMountain(A):
    if len(A) < 3:
        return 0
    f = 0
    le = 1
    res = 0
    k = -1
    you = -1
    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            k = i
            break
    if k == -1:
        return 0
    for i in range(k, len(A)):
        if f == 0:
            if A[i] > A[i - 1]:
                le += 1
                you = 1
            elif A[i] == A[i - 1]:
                le = 0
                you = 0
            else:
                if you == 1:
                    le += 1
                    f = 1
                    res = max(res, le)
                    continue
        elif f == 1:
            if A[i] < A[i - 1]:
                le += 1
            elif A[i] == A[i - 1]:
                res = max(res, le)
                le = 1
                f = 0  # 重新开始上升
            else:
                res = max(res, le)
                le = 2
                f = 0  # 重新开始上升
            res = max(res, le)
    return res

a = [2,1,4,7,3,2,5]
b = [0,1,2,3,4,5,4,3,2,1,0]
c = [0, 1, 0]
d = [2,3,3,2,0,2]
print(longestMountain(d))

# class Solution:
#     def longestMountain(self, A: List[int]) -> int:
#         n = len(A)
#         ans = left = 0
#         while left + 2 < n:
#             right = left + 1
#             if A[left] < A[left + 1]:
#                 while right + 1 < n and A[right] < A[right + 1]:
#                     right += 1
#                 if right < n - 1 and A[right] > A[right + 1]:
#                     while right + 1 < n and A[right] > A[right + 1]:
#                         right += 1
#                     ans = max(ans, right - left + 1)
#                 else:
#                     right += 1
#             left = right
#         return ans




