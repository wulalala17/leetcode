/*149. 直线上最多的点数

给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。



示例 1：

输入：points = [[1,1],[2,2],[3,3]]
输出：3

示例 2：

输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出：4



提示：

    1 <= points.length <= 300
    points[i].length == 2
    -104 <= xi, yi <= 104
    points 中的所有点 互不相同
*/
class Solution {//想不到gcd做法，想到了估计也写不出来
    public int maxPoints(int[][] points) {
        int n = points.length;
        if (n == 0) return 0;
        if (n == 1) return 1;
        int res = 0;
        for (int i = 0; i < n - 1; i++) {
            Map<String, Integer> slope = new HashMap<>();
            int repeat = 0;
            int tmp_max = 0;
            for (int j = i + 1; j < n; j++) {
                int dy = points[i][1] - points[j][1];
                int dx = points[i][0] - points[j][0];
                if (dy == 0 && dx == 0) {
                    repeat++;
                    continue;
                }
                int g = gcd(dy, dx);
                if (g != 0) {
                    dy /= g;
                    dx /= g;
                }
                String tmp = String.valueOf(dy) + "/" + String.valueOf(dx);
                slope.put(tmp, slope.getOrDefault(tmp, 0) + 1);
                tmp_max = Math.max(tmp_max, slope.get(tmp));
            }
            res = Math.max(res, repeat + tmp_max + 1);
        }
        return res;
    }

    private int gcd(int dy, int dx) {
        if (dx == 0) return dy;
        else return gcd(dx, dy % dx);
    }
}
