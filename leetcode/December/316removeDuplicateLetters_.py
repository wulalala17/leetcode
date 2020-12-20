# 316.去除重复字母
# 给你一个字符串s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
# 注意：该题与1081https: // leetcode - cn.com / problems / smallest - subsequence - of - distinct - characters相同
# 示例1：
# 输入：s = "bcabc"
# 输出："abc"
# 示例2：
# 输入：s = "cbacdcbc"
# 输出："acdb"
# 提示：
# 1 <= s.length <= 104  s由小写英文字母组成

def removeDuplicateLetters(s):  # 没想出来，参考评论区
    """
    :type s: str
    :rtype: str
    """
    res = ''
    stack = []
    for i in range(len(s)):
        if s[i] in stack:
            continue
        while stack and ord(stack[-1]) > ord(s[i]) and stack[-1] in s[i+1:]:
            stack.pop(-1)
        stack.append(s[i])
    for s in stack:
        res += s
    return res

    # for char in s:
    #     if not char in d:
    #         d[char] = 1
    #     else:
    #         d[char] += 1
    # for i in range(len(s)):
    #     if s[i] in res:
    #         continue
    #     elif d[s[i]] > 1:
    #         temp.append(s[i])
    #         d[s[i]] -= 1
    #     else:
    #         while temp:
    #             p = temp.pop(0)
    #             d[p] -= 1
    #             if ord(p) < ord(s[i]):
    #                 res.append(p)
    #         res.append(s[i])
    # k = ''
    # for r in res:
    #     k += r
    # return k

print(removeDuplicateLetters("cdadabcc"))