# 57.插入区间
# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
# 示例
# 1：
# 输入：intervals = [[1, 3], [6, 9]], newInterval = [2, 5]
# 输出：[[1, 5], [6, 9]]
# 示例
# 2：
# 输入：intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval = [4, 8]
# 输出：[[1, 2], [3, 10], [12, 16]]
# 解释：这是因为新的区间[4, 8]与[3, 5], [6, 7], [8, 10]重叠。

def insert(intervals, newInterval):
    if len(intervals) == 0:
        return [newInterval[:]]

    i = 0
    left, right = newInterval[0], newInterval[1]
    start, flag = 0, 0
    if intervals[-1][1] < left:
        intervals.append(newInterval)
    if intervals[0][0] > right:
        return [newInterval]+intervals
    while i < len(intervals):
        if intervals[i][0] > left:
            intervals[i][0] = left
            if intervals[i][1] >= right:
                return intervals[:]
            else:
                intervals[i][1] = right
                start = i + 1
                break
        if intervals[i][0] < left and intervals[i][1] < left:
            i += 1
            continue
        if intervals[i][0] <= left <= intervals[i][1]:
            if intervals[i][1] >= right:
                return intervals
            else:
                intervals[i][1] = right
                flag = i
                start = i + 1
                break
    del_l, del_r = -1, -2
    delshuzu = []
    while start < len(intervals):
        if intervals[start][0] < right and intervals[start][1] < right:
            # if del_l == -1:
            #     del_l = start
            delshuzu.append(start)
            start += 1
            continue
        if intervals[start][0] < right <= intervals[start][1]:
            intervals[flag][1] = intervals[start][1]
            # if del_l == -1:
            #     del_l = start
            delshuzu.append(start)
            break

        if intervals[start][0] == right:
            intervals[flag][1] = intervals[start][1]
            # if start == len(intervals) - 1:
            #     del_r = -1
            # else:
            #     del_r = start + 1
            delshuzu.append(start)
            break

        if intervals[start][0] > right:
            # del_r = start
            # delshuzu.append(start-1)
            break
    # if del_l != -1:
    #     if del_r == -2:
    #         del intervals[del_l:]
    #     else:
    #         del intervals[del_l:del_r]
    for d in delshuzu[::-1]:
        del intervals[d]
    return intervals[:]

a = [[1, 3], [6, 9]]
b = [2, 5]
c = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
d = [4, 8]
e = [[1, 2], [10, 11]]
f = [0, 9]
g = [[1, 5]]
h = [0, 0]
cn = [[1, 5], [6, 8]]
nm = [5, 6]
print(insert(a, b))
print(insert(c, d))
print(insert(e, f))
print(insert(g, h))
print(insert(cn, nm))

# left, right = newInterval
# placed = False
# ans = list()
# for li, ri in intervals:
#     if li > right:
#         # 在插入区间的右侧且无交集
#         if not placed:
#             ans.append([left, right])
#             placed = True
#         ans.append([li, ri])
#     elif ri < left:
#         # 在插入区间的左侧且无交集
#         ans.append([li, ri])
#     else:
#         # 与插入区间有交集，计算它们的并集
#         left = min(left, li)
#         right = max(right, ri)
#
# if not placed:
#     ans.append([left, right])
# return ans
#
# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / insert - interval / solution / cha - ru - qu - jian - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 原地修改，节省空间
# 先找到第一个与待插入重叠的区间， 向后扩大区间直到没有重叠区域
# 最后删除所有曾重叠的子区间，插入最终新增的区间
#
# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         # 初始状况判断
#         if not newInterval:
#             return intervals
#         if not intervals:
#             return [newInterval]
#         # 已经是起点有序的了
#         i = 0
#         intervalsLen = len(intervals)
#         while i < intervalsLen and intervals[i][1] < newInterval[0]:
#             i += 1
#         # 保存删除之前的位置，最后在这个位置上插入
#         tempI = i
#         while i < intervalsLen and intervals[i][0] <= newInterval[1]:
#             newInterval[0] = min(newInterval[0], intervals[i][0])
#             newInterval[1] = max(newInterval[1], intervals[i][1])
#             i += 1
#         else:
#             del intervals[tempI:i]
#             intervals.insert(tempI, newInterval)
#         return intervals
#
# 作者：cui-jin-hao-_official
# 链接：https://leetcode-cn.com/problems/insert-interval/solution/python-shuang-100-by-cui-jin-hao-_official/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
