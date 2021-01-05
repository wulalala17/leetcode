# 830.较大分组的位置
# 在一个由小写字母构成的字符串s中，包含由一些连续的相同字符所构成的分组。
# 例如，在字符串s = "abbxxxxzyy"中，就含有"a", "bb", "xxxx", "z"和"yy"这样的一些分组。
# 分组可以用区间[start, end]表示，其中start和end分别表示该分组的起始和终止位置的下标。上例中的"xxxx"分组用区间表示为[3, 6] 。
# 我们称所有包含大于或等于三个连续字符的分组为较大分组 。找到每一个较大分组的区间，按起始位置下标递增顺序排序后，返回结果。
# 示例1：
# 输入：s = "abbxxxxzzy"
# 输出：[[3, 6]]
# 解释："xxxx"是一个起始于3且终止于6的较大分组。
# 示例2：
# 输入：s = "abc"
# 输出：[]
# 解释："a", "b"和"c"均不是符合要求的较大分组。
# 示例3：
# 输入：s = "abcdddeeeeaabbbcd"
# 输出：[[3, 5], [6, 9], [12, 14]]
# 解释：较大分组为"ddd", "eeee"和 "bbb"
# 示例4：
# 输入：s = "aba"
# 输出：[]

# 提示：
# 1 <= s.length <= 1000
# s仅含小写英文字母

class Solution(object):
    def largeGroupPositions(self, s):  # 比较字符，只循环一遍
        """
        :type s: str
        :rtype: List[List[int]]
        """
        if len(s) < 3:
            return []
        res = []
        i = 0
        while i < len(s)-2:
            if s[i] == s[i+1] and s[i] == s[i+2]:
                j = i+3
                while j < len(s):
                    if s[i] != s[j]:
                        break
                    j += 1
                res.append([i,j-1])
                i = j
            else:
                i += 1
        return res