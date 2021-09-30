# 223. 矩形面积
#
# 给你 二维 平面上两个 由直线构成的 矩形，请你计算并返回两个矩形覆盖的总面积。
#
# 每个矩形由其 左下 顶点和 右上 顶点坐标表示：
#
#     第一个矩形由其左下顶点 (ax1, ay1) 和右上顶点 (ax2, ay2) 定义。
#     第二个矩形由其左下顶点 (bx1, by1) 和右上顶点 (bx2, by2) 定义。
#
#
#
# 示例 1：
# Rectangle Area
#
# 输入：ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
# 输出：45
#
# 示例 2：
#
# 输入：ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
# 输出：16
#
#
#
# 提示：
#
#     -104 <= ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 <= 104
class Solution(object):  # java越写越复杂，还是看了评论才知道 淦
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        x1=max(ax1,bx1)
        y1=max(ay1,by1)
        x2=min(ax2,bx2)
        y2=min(ay2,by2);
        if x1>=x2 or y1>=y2:
            return ((ax2-ax1)*(ay2-ay1)+(bx2-bx1)*(by2-by1))
        else:
            return ((ax2-ax1)*(ay2-ay1)+(bx2-bx1)*(by2-by1)-(x2-x1)*(y2-y1))