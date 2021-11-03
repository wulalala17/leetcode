/*
407. 接雨水 II

给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。



示例 1:

输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
输出: 4
解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。

示例 2:

输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
输出: 10



提示:

    m == heightMap.length
    n == heightMap[i].length
    1 <= m, n <= 200
    0 <= heightMap[i][j] <= 2 * 104
*/
class Solution {//自己写的不知道错哪里了
    public int trapRainWater(int[][] heightMap) {
        int n = heightMap.length, m = heightMap[0].length;
        int[][] left = new int[n][m];
        int[][] right = new int[n][m];
        int[][] up = new int[n][m];
        int[][] down = new int[n][m];
        int max = 0, min = 0, res = 0;
        for(int i = 0; i < n; i++){
            max = heightMap[i][0];
            left[i][0] = max;
            for(int j = 1; j < m; j++){
                if(heightMap[i][j] >= max){
                    max = heightMap[i][j];
                }
                left[i][j] = max;
            }
        }
        for(int i = 0; i < n; i++){
            max = heightMap[i][m - 1];
            right[i][m - 1] = max;
            for(int j = m - 2; j >= 0; j--){
                if(heightMap[i][j] >= max){
                    max = heightMap[i][j];
                }
                right[i][j] = max;
            }
        }
        for(int i = 0; i < m; i++){
            max = heightMap[0][i];
            up[0][i] = max;
            for(int j = 1; j < n; j++){
                if(heightMap[j][i] >= max){
                    max = heightMap[j][i];
                }
                up[j][i] = max;
            }
        }
        for(int i = 0; i < m; i++){
            max = heightMap[n - 1][i];
            down[n - 1][i] = max;
            for(int j = n - 2; j >= 0; j--){
                if(heightMap[j][i] >= max){
                    max = heightMap[j][i];
                }
                down[j][i] = max;
            }
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                int m1 = Math.min(up[i][j], down[i][j]);
                int m2 = Math.min(left[i][j], right[i][j]);
                res += Math.min(m1, m2) - heightMap[i][j];
            }
        }
        return res;
    }
}

/*
class Solution {
    public int trapRainWater(int[][] heightMap) {
        if (heightMap.length <= 2 || heightMap[0].length <= 2) {
            return 0;
        }
        int m = heightMap.length;
        int n = heightMap[0].length;
        boolean[][] visit = new boolean[m][n];
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 || i == m - 1 || j == 0 || j == n - 1) {
                    pq.offer(new int[]{i * n + j, heightMap[i][j]});
                    visit[i][j] = true;
                }
            }
        }
        int res = 0;
        int[] dirs = {-1, 0, 1, 0, -1};
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            for (int k = 0; k < 4; ++k) {
                int nx = curr[0] / n + dirs[k];
                int ny = curr[0] % n + dirs[k + 1];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visit[nx][ny]) {
                    if (curr[1] > heightMap[nx][ny]) {
                        res += curr[1] - heightMap[nx][ny];
                    }
                    pq.offer(new int[]{nx * n + ny, Math.max(heightMap[nx][ny], curr[1])});
                    visit[nx][ny] = true;
                }
            }
        }
        return res;
    }
}

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/trapping-rain-water-ii/solution/jie-yu-shui-ii-by-leetcode-solution-vlj3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/