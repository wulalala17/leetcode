# 205. 同构字符串
# 给定两个字符串 s 和 t，判断它们是否是同构的。
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
#
# 示例 1:
# 输入: s = "egg", t = "add"
# 输出: true
#
# 示例 2:
# 输入: s = "foo", t = "bar"
# 输出: false
#
# 示例 3:
# 输入: s = "paper", t = "title"
# 输出: true
#
# 说明:
# 你可以假设 s 和 t 具有相同的长度。


def isIsomorphic(s, t):  # 没想到好方法，只能暴力
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    n = len(s)
    d = {}
    for i in range(n):
        if t[i] not in d.values():
            if s[i] not in d:
                d[s[i]] = t[i]
            else:
                return False
        else:
            if s[i] not in d:
                return False
            else:
                if d[s[i]] != t[i]:
                    return False
    return True

print(isIsomorphic('aa', 'ab'))