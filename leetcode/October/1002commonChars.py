def commonChars(A):
    k = [0 for _ in range(26)]
    for a in A[0]:
        k[ord(a)-97] += 1

    for i in range(1, len(A)):
        newk = [0 for _ in range(26)]  # 保存当前字符串每个字符出现次数
        for a in A[i]:
            newk[ord(a) - 97] += 1
        for j in range(26):  # 更新结果
            k[j] = min(k[j], newk[j])

    res = []
    for i in range(26):
        if k[i] > 0:
            while k[i]:
                res.append(chr(i+97))
                k[i] -= 1
    return res

#     def commonChars(self, A: List[str]) -> List[str]: 官方答案
#         minfreq = [float("inf")] * 26
#         for word in A:
#             freq = [0] * 26
#             for ch in word:
#                 freq[ord(ch) - ord("a")] += 1
#             for i in range(26):
#                 minfreq[i] = min(minfreq[i], freq[i])
#
#         ans = list()
#         for i in range(26):  # 一行生成结果
#             ans.extend([chr(i + ord("a"))] * minfreq[i])
#         return ans
#
#
# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / find - common - characters / solution / cha - zhao - chang - yong - zi - fu - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

 # def commonChars(self, A: List[str]) -> List[str]: 一行答案 不明觉厉
 #        return list(reduce(lambda x, y: x & y, map(collections.Counter, A)).elements())
print(ord('a'))