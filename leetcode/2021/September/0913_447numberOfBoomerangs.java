/*
447. 回旋镖的数量

给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组 ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

返回平面上所有回旋镖的数量。


示例 1：

输入：points = [[0,0],[1,0],[2,0]]
输出：2
解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]

示例 2：

输入：points = [[1,1],[2,2],[3,3]]
输出：2

示例 3：

输入：points = [[1,1]]
输出：0



提示：

    n == points.length
    1 <= n <= 500
    points[i].length == 2
    -104 <= xi, yi <= 104
    所有点都 互不相同
*/
class Solution {
    public int numberOfBoomerangs(int[][] points) {
        int n = points.length;
        if(n <= 2)
            return 0;
        int[][] dis = new int[n][n];
        int a,b;
        for(int i = 0; i < n; i++){
            for(int j = i + 1; j < n; j++){
                a = Math.abs(points[i][0] - points[j][0]);
                b = Math.abs(points[i][1] - points[j][1]);
                dis[i][j] = a * a + b * b;
                dis[j][i] = dis[i][j];
            }
        }
        int res = 0, cur = 0;
        for(int i = 0; i < n; i++){
            Map<Integer, Integer> map = new HashMap<>();
            for(int j = 0; j < n; j++){
                map.put(dis[i][j], map.getOrDefault(dis[i][j], 0) + 1);
            }
            for(Integer k: map.keySet()){
                if(map.get(k) > 1){
                    cur = map.get(k);
                    res += cur * (cur - 1);
                }
            }
        }
        return res;
    }
}