# 1232.缀点成线
# 在一个XY坐标系中有一些点，我们用数组coordinates来分别记录它们的坐标，其中coordinates[i] = [x, y]表示横坐标为x、纵坐标为y的点。
# 请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回true，否则请返回false。
# 示例1：
# 输入：coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
# 输出：true
#
# 示例2：
# 输入：coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
# 输出：false
#
# 提示：
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10 ^ 4 <= coordinates[i][0], coordinates[i][1] <= 10 ^ 4
# coordinates中不含重复的点

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) < 2:
            return False
        x = (coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1])
        for i in range(2, len(coordinates)):
            y = (coordinates[i][0] - coordinates[0][0], coordinates[i][1] - coordinates[0][1])
            if y[0] * x[1] != y[1] * x[0]:
                return False
        return True