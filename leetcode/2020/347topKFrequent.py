def topKFrequent(l, k):
    d0 = {}
    res = []
    for i in l:
        d0[i] = 0
    for i in l:
        d0[i] += 1
    print('first d0:', d0)
    d1 = sorted(d0.items(), key=lambda item: item[1], reverse=True)  # 按照字典的value倒序排序
    for i in range(k):
        res.append(d1[i][0])
        print('前%d频繁出现的数字：'%(i), d1[i][0])
    print(d1)
    print(res)
    return res


topKFrequent([1, 2, 3, 3, 4], 2)


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         Hash = {}
#         for i in nums:
#             Hash[i] = Hash.get(i, 0) + 1
#         keyvalues = sorted(Hash.items(), key = lambda x: (x[1], x[0]), reverse=True)
#         return [keyvalues[j][0] for j in range(k)]

# 别人的方法，省了一次循环，字典的value值可以直接用get初始化，返回结果可以用列表生成式
# 作者：yi-wen-statistics
# 链接：https://leetcode-cn.com/problems/top-k-frequent-elements/solution/ha-xi-biao-pai-xu-by-yi-wen-statistics-3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
