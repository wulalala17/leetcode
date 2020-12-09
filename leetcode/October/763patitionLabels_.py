# 763.划分字母区间
# 字符串S由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。
# 示例
# 1：
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9, 7, 8]
# 解释：
# 划分结果为"ababcbaca", "defegde", "hijhklij"。每个字母最多出现在一个片段中。像"ababcbacadefegde", "hijhklij"的划分是错误的，因为划分的片段数较少。

# 提示：
# S的长度在[1, 500]之间。
# S只包含小写字母'a'到'z' 。
def partitionLabels(S):
    d = {}
    for i in range(26):  # 初始化
        d[chr(i + 97)] = [-1, -1]

    for i in range(len(S)):
        c = S[i]  # 当前字符
        if d[c][0] == -1:
            d[c][0] = i
            d[c][1] = i
        else:
            d[c][1] = i

    start, end = 0, 0
    res = []
    for i in range(len(S)):
        end = max(end, d[S[i]][1])
        if i == end:
            res.append(end-start+1)
            start = i + 1
    return res



import re
def pda(s):
    return re.match(r'', s)

a = 'ababcbacadefegdehijhklij'
partitionLabels(a)