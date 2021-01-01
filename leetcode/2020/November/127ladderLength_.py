def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    def twowords(wa, wb):
        res = 0
        if len(wa) != len(wb):
            return -1
        else:
            for i in range(len(wa)):
                if wa[i] != wb[i]:
                    res += 1
            return res

    stack = [beginWord]
    less = 0
    start = 0
    while endWord not in stack:
        less += 1
        le = len(stack)
        for i in range(start, le):
            for j in range(len(wordList)):
                if wordList[j] in stack:
                    continue
                if twowords(stack[i], wordList[j]) == 1 and wordList[j] not in stack:
                    stack.append(wordList[j])
        newle = len(stack)
        if newle == le and endWord not in stack:
            return 0
            break
        start = le
    return less + 1

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord, endWord, wordList))


# class Solution:  双向BFS 好难
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if endWord not in wordList:
#             return 0
#         wordict = set(wordList)
#         s1 = {beginWord}
#         s2 = {endWord}
#         n = len(beginWord)
#         step = 0
#         wordict.remove(endWord)
#         while s1 and s2:
#             step += 1
#             if len(s1) > len(s2): s1, s2 = s2, s1
#             s = set()
#             for word in s1:
#                 nextword = [word[:i] + chr(j) + word[i + 1:] for j in range(97, 123) for i in range(n)]
#                 for w in nextword:
#                     if w in s2:
#                         return step + 1
#                     if w not in wordict: continue
#                     wordict.remove(w)
#                     s.add(w)
#             s1 = s
#         return 0
#
# 作者：powcai
# 链接：https://leetcode-cn.com/problems/word-ladder/solution/bfscong-wu-dao-you-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。