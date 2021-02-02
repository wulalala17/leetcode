# 424. 替换后的最长重复字符
# 给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换k次。在执行上述操作后，找到包含重复字母的最长子串的长度。
# 注意：字符串长度和k不会超过104。
# 示例1：
# 输入：s = "ABAB", k = 2
# 输出：4
# 解释：用两个'A'替换为两个 'B', 反之亦然。
#
# 示例2：
# 输入：s = "AABABBA", k = 1
# 输出：4
# 解释：将中间的一个'A'替换为'B', 字符串变为 "AABBBBA"。子串 "BBBB"有最长重复字母, 答案为4。

class Solution(object):  # 第一反应是DP，发现不对，后面不知道咋写了。抄的官方题解
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        num = [0] * 26
        n = len(s)
        maxn = left = right = 0

        while right < n:
            num[ord(s[right]) - ord("A")] += 1
            maxn = max(maxn, num[ord(s[right]) - ord("A")])
            if right - left + 1 - maxn > k:
                num[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1

        return right - left