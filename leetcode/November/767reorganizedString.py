# 767. 重构字符串
# 给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
# 若可行，输出任意可行的结果。若不可行，返回空字符串。
# 示例 1:
# 输入: S = "aab"
# 输出: "aba"
# 示例 2:
# 输入: S = "aaab"
# 输出: ""
# 注意:
#     S 只包含小写字母并且长度在[1, 500]区间内。
# 通过次数20,807
# 提交次数45,143
from collections import Counter

def reorganizeString(S):
    """
    :type S: str
    :rtype: str
    """
    def isUnique(s):  # 判断是否符合题目要求
        if len(s) == 1:
            return True
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                return False
        return True
    def insert(s, c, times):  # 按间隔顺序插入字符
        for i in range(0, len(s), 2):
            if times == 0:
                break
            if s[i] == '_':
                s[i] = c
                times -= 1
            else:
                continue
        for i in range(1, len(s), 2):
            if times == 0:
                break
            if s[i] == '_':
                s[i] = c
                times -= 1
            else:
                continue
        return s


    c = Counter(S)
    c1 = sorted(c.items(), key=lambda x: x[1], reverse=True)
    news = ['_' for _ in range(len(S))]
    for i in range(len(c1)):
        k = c1[i][1]
        news = insert(news, c1[i][0], k)
    res = ''
    for nn in news:
        res += nn[0]
    if isUnique(res):
        return res
    else:
        return ''

print(reorganizeString('aaab'))


