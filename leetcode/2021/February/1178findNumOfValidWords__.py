# 1178. 猜字谜
# 外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。
# 字谜的迷面puzzle按字符串形式给出，如果一个单词word符合下面两个条件，那么它就可以算作谜底：
# 单词word中包含谜面puzzle的第一个字母。单词word中的每一个字母都可以在谜面puzzle中找到。例如，如果字谜的谜面是"abcdefg"，那么可以作为谜底的单词有
# "faced", "cabbage", 和"baggage"；而"beefed"（不含字母"a"）以及"based"（其中的"s"没有出现在谜面中）。
# 返回一个答案数组answer，数组中的每个元素answer[i]是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜底的单词数目。
#
# 示例：
# 输入：
# words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
# puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
# 输出：[1, 1, 3, 2, 4, 0]
# 解释：1个单词可以作为 "aboveyz" 的谜底: "aaaa"
# 1个单词可以作为 "abrodyz"的谜底: "aaaa"
# 3个单词可以作为 "abslute" 的谜底: "aaaa", "asas", "able"
# 2个单词可以作为 "absoryz" 的谜底: "aaaa", "asas"
# 4个单词可以作为 "actresz" 的谜底: "aaaa", "asas", "actt", "access"
# 没有单词可以作为"gaswxyz" 的谜底，因为列表中的单词都不含字母 'g'。

# 提示：
# 1 <= words.length <= 10 ^ 5
# 4 <= words[i].length <= 50
# 1 <= puzzles.length <= 10 ^ 4
# puzzles[i].length == 7
# words[i][j], puzzles[i][j]
# 都是小写英文字母。每个 puzzles[i] 所包含的字符都不重复。

# class Solution(object):  # 暴力是行不通的，看的官方题解
#     def findNumOfValidWords(self, words, puzzles):
#         """
#         :type words: List[str]
#         :type puzzles: List[str]
#         :rtype: List[int]
#         """
#         f = []
#         s1 = []
#         s2 = []
#         for p in puzzles:
#             f.append(p[0])
#             s2.append(set(p))
#         for w in words:
#             s1.append(set(w))
#         res = []
#         for i in range(len(s2)):
#             r = 0
#             for s in s1:
#                 if f[i] not in s:
#                     continue
#                 if s2[i] & s == s:
#                     r += 1
#             res.append(r)
#
#         # for p in puzzles:
#         #     r = 0
#         #     for w in words:
#         #         if p[0] not in w:
#         #             continue
#         #         if set(p) & set(w) == set(w):
#         #             r += 1
#         #     res.append(r)
#         return res


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        frequency = collections.Counter()

        for word in words:
            mask = 0
            for ch in word:
                mask |= (1 << (ord(ch) - ord("a")))
            if str(bin(mask)).count("1") <= 7:
                frequency[mask] += 1

        ans = list()
        for puzzle in puzzles:
            total = 0

            # 枚举子集方法一
            # for choose in range(1 << 6):
            #     mask = 0
            #     for i in range(6):
            #         if choose & (1 << i):
            #             mask |= (1 << (ord(puzzle[i + 1]) - ord("a")))
            #     mask |= (1 << (ord(puzzle[0]) - ord("a")))
            #     if mask in frequency:
            #         total += frequency[mask]

            # 枚举子集方法二
            mask = 0
            for i in range(1, 7):
                mask |= (1 << (ord(puzzle[i]) - ord("a")))

            subset = mask
            while subset:
                s = subset | (1 << (ord(puzzle[0]) - ord("a")))
                if s in frequency:
                    total += frequency[s]
                subset = (subset - 1) & mask

            # 在枚举子集的过程中，要么会漏掉全集 mask，要么会漏掉空集
            # 这里会漏掉空集，因此需要额外判断空集
            if (1 << (ord(puzzle[0]) - ord("a"))) in frequency:
                total += frequency[1 << (ord(puzzle[0]) - ord("a"))]

            ans.append(total)

        return ans