# 692.前K个高频单词
#
# 给一非空的单词列表，返回前k个出现次数最多的单词。
#
# 返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。
#
# 示例1：
#
# 输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# 输出: ["i", "love"]
# 解析: "i"和"love"为出现次数最多的两个单词，均为2次。注意，按字母顺序"i"在"love"之前。
#
# 示例2：
#
# 输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# 输出: ["the", "is", "sunny", "day"]
# 解析: "the", "is", "sunny"和"day"是出现次数最多的四个单词，出现次数依次为4, 3, 2和1次。
#
#
#
# 注意：
# 假定k总为有效值， 1 ≤ k ≤ 集合元素数。输入的单词均由小写字母组成。
#
#
#
# 扩展练习：
# 尝试以O(nlogk) 时间复杂度和O(n)空间复杂度解决。
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = {}
        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        l = list(sorted(d.items(), key=lambda x: (-x[1], x[0])))  # 频率降序，单词字典序升序
        res = []
        for i in range(k):
            res.append(l[i][0])
        return res
