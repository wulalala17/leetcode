# 973.最接近原点的K个点
# 我们有一个由平面上的点组成的列表points。需要从中找出K个距离原点(0, 0)最近的点。
# （这里，平面上两点之间的距离是欧几里德距离。）
# 你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。
# 示例
# 1：
# 输入：points = [[1, 3], [-2, 2]], K = 1
# 输出：[[-2, 2]]
# 解释：(1, 3)和原点之间的距离为sqrt(10)，(-2, 2)和原点之间的距离为sqrt(8)，由于sqrt(8) < sqrt(10)，(-2, 2)离原点更近。我们只需要距离原点最近的K = 1个点，所以答案就是[[-2, 2]]。
#
# 示例
# 2：
# 输入：points = [[3, 3], [5, -1], [-2, 4]], K = 2
# 输出：[[3, 3], [-2, 4]]（答案[[-2, 4], [3, 3]]也会被接受。）
def kClosest(points, K):
    """
    :type points: List[List[int]]
    :type K: int
    :rtype: List[List[int]]
    """
    d = {}
    for i in range(len(points)):
        l = points[i][0] ** 2 + points[i][1] ** 2
        d[i] = l
    # print(d)
    dd = sorted(d.items(), key=lambda item: item[1])
    res = [points[dd[i][0]] for i in range(K)]
    return res

points = [[1, 3], [-2, 2]]
K = 1
print(kClosest(points, K))

# 为什么别人写的这么简洁
# a = lambda x :x[0]**2 + x[1]**2
#         points.sort(key = a)
#         return points[:K]