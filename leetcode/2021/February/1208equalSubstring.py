# 1208. 尽可能使字符串相等
# 给你两个长度相同的字符串，s和t。
# 将s中的第i个字符变到t中的第i个字符需要 | s[i] - t[i] | 的开销（开销可能为0），也就是两个字符的ASCII码值的差的绝对值。
# 用于变更字符串的最大预算是maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。
# 如果你可以将s的子字符串转化为它在t中对应的子字符串，则返回可以转化的最大长度。
# 如果s中没有子字符串可以转化成t中对应的子字符串，则返回0。
#
# 示例1：
# 输入：s = "abcd", t = "bcdf", cost = 3
# 输出：3
# 解释：s中的"abc"可以变为"bcd"。开销为 3，所以最大长度为3。
#
# 示例2：
# 输入：s = "abcd", t = "cdef", cost = 3
# 输出：1
# 解释：s中的任一字符要想变成t中对应的字符，其开销都是2。因此，最大长度为1。
#
# 示例3：
# 输入：s = "abcd", t = "acde", cost = 0
# 输出：1
# 解释：你无法作出任何改动，所以最大长度为1。
#
# 提示：
# 1 <= s.length, t.length <= 10 ^ 5
# 0 <= maxCost <= 10 ^ 6
# s和t都只含小写英文字母。

def equalSubstring(s, t, maxCost):  # 暴力超时
    """
    :type s: str
    :type t: str
    :type maxCost: int
    :rtype: int
    """
    cost = []
    n = len(s)
    res = 0
    for i in range(n):
        c = abs(ord(s[i]) - ord(t[i]))
        cost.append(c)
    i, j = 0, 0
    while i < n:
        j = i
        cur = maxCost
        while j < n and cur >= 0:
            if cur < cost[j]:
                break
            if cur >= cost[j]:
                cur -= cost[j]
                res = max(res, j - i + 1)
            j += 1
        if j == n:
            break
        i += 1
    return res

def equalSubstring1(s, t, maxCost):  # 双指针才过了
    """
    :type s: str
    :type t: str
    :type maxCost: int
    :rtype: int
    """
    cost = []
    n = len(s)
    res = 0
    for i in range(n):
        c = abs(ord(s[i]) - ord(t[i]))
        cost.append(c)
    i = 0
    j = i
    while i < n:
        if j == i:
            if maxCost < cost[j]:
                i += 1
                j += 1
                continue
            else:
                maxCost -= cost[i]
                res = max(res, j - i + 1)
                j += 1
                continue
        else:
            if j == n:
                break
            if maxCost < cost[j]:
                maxCost += cost[i]
                i += 1
                continue
            else:
                maxCost -= cost[j]
                res = max(res, j - i + 1)
                j += 1
                continue
    return res
a = "krrgw"
b = "zjxss"
c= 'abcd'
d = 'cdef'

print(equalSubstring1(c,d,3))



