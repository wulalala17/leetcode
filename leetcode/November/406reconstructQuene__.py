# 406. 根据身高重建队列
#
# 假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。
#
# 注意：
# 总人数少于1100人。
#
# 示例
#
# 输入:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# 输出:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
def reconstructQueue(people):  # 看了别人才知道怎么写
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    n = len(people)
    if n == 0:
        return
    def by_h(t):
        return t[0]
    def by_k(t):
        return t[1]
    # p0 = sorted(people, key=by_k, reverse=True)  # K降序
    # print("p0:",p0)
    # p1 = sorted(p0, key=by_h)  # h升序
    # print("p1：",p1)
    people.sort(key=lambda x: (x[0], -x[1]))
    print('p1:',people)
    res = [[-1, -1] for _ in range(n)]
    fl = [0 for _ in range(n)]
    for p in people:
        i = 0
        j = 0
        while i <= p[1]:
            if fl[j] == 1:
                j += 1
                continue
            if fl[j] == 0 and i != p[1]:
                j += 1
                i += 1
                continue
            if i == p[1] and fl[j] == 0:
                fl[j] = 1
                res[j][0] = p[0]
                res[j][1] = p[1]
                break
    return res
p = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(reconstructQueue(p))

# class Solution:  官方思路 先对h降序，再对k升序
#     def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
#         people.sort(key=lambda x: (-x[0], x[1]))
#         n = len(people)
#         ans = list()
#         for person in people:
#             ans[person[1]:person[1]] = [person]
#         return ans
#
# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/gen-ju-shen-gao-zhong-jian-dui-lie-by-leetcode-sol/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# people.sort(key=lambda x: (-x[0], x[1]))
#         res = []
#         for i in people:
#             res.insert(i[1], i)
#         return res
#
# 作者：wu-di-zzx
# 链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/python-cha-ru-5xing-dai-ma-gao-ding-by-wu-di-zzx/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

