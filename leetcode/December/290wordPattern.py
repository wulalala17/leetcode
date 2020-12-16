# 290. 单词规律
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
# 示例1:
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
# 示例 2:
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
# 示例 3:
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
# 示例 4:
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。

def wordPattern(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    str1 = []  # 字符串数组，按空格分组
    # str1 = s.split(" ")  正确的分组做法
    d = {}
    s1 = ""
    for i in range(len(s)):
        if i == (len(s) - 1):
            s1 += s[i]
            str1.append(s1)
            break
        if s[i] == ' ':
            str1.append(s1)
            s1 = ""
        else:
            s1 += s[i]
    if len(str1) != len(pattern):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in d:
            d[pattern[i]] = [i]
        else:
            d[pattern[i]].append(i)
    for key in d:
        n = len(d[key])
        if n == 1:
            continue
        else:
            for i in range(1, n):
                if str1[d[key][i]] != str1[d[key][i - 1]]:
                    return False
    c = 0
    se = set()
    for key in d:  # 判断abba里ab代表的字符串不同
        c += 1
        se.add(str1[d[key][0]])
    if len(se) != c:
        return False

    return True

pattern = "abba"
str = "dog cat cat dog"
print(wordPattern(pattern, str))


# class Solution:  # 官方题解，两个字典，更简便
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         word2ch = dict()
#         ch2word = dict()
#         words = s.split()
#         if len(pattern) != len(words):
#             return False
#
#         for ch, word in zip(pattern, words):
#             if (word in word2ch and word2ch[word] != ch) or (ch in ch2word and ch2word[ch] != word):
#                 return False
#             word2ch[word] = ch
#             ch2word[ch] = word
#
#         return True
#
#
# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / word - pattern / solution / dan - ci - gui - lu - by - leetcode - solution - 6
# vqv /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

