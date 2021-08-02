/*
743. 网络延迟时间

有 n 个网络节点，标记为 1 到 n。

给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。



示例 1：

输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出：2

示例 2：

输入：times = [[1,2,1]], n = 2, k = 1
输出：1

示例 3：

输入：times = [[1,2,1]], n = 2, k = 2
输出：-1



提示：

    1 <= k <= n <= 100
    1 <= times.length <= 6000
    times[i].length == 3
    1 <= ui, vi <= n
    ui != vi
    0 <= wi <= 100
    所有 (ui, vi) 对都 互不相同（即，不含重复边）
*/
class Solution {
    int dijstra(int[][] matrix, int source) {
        //最短路径长度
        int[] shortest = new int[matrix.length];
        //判断该点的最短路径是否求出
        int[] visited = new int[matrix.length];

        //初始化源节点
        shortest[source] = 0;
        visited[source] = 1;

        for (int i = 1; i < matrix.length; i++) {
            int min = Integer.MAX_VALUE;
            int index = -1;

            for (int j = 1; j < matrix.length; j++) {
                //已经求出最短路径的节点不需要再加入计算并判断加入节点后是否存在更短路径
                if (visited[j] == 0 && matrix[source][j] < min) {
                    min = matrix[source][j];
                    index = j;
                }
            }
            if(index == -1)
                continue;
            //更新最短路径
            shortest[index] = min;
            visited[index] = 1;

            //更新从index跳到其它节点的较短路径
            for (int m = 1; m < matrix.length; m++) {
                if (visited[m] == 0 && matrix[source][index] + matrix[index][m] < matrix[source][m]) {
                    matrix[source][m] = matrix[source][index] + matrix[index][m];
                    //path[m] = path[index] + "->" + m;
                }
            }
        }
        int res = 0;
        for(int i = 1; i < matrix.length; i++){
            if (shortest[i] == 1000)
                return -1;
            res = Math.max(res, shortest[i]);
        }
        return res;
    }

    public int networkDelayTime(int[][] times, int n, int k) {
        int[][] edges = new int[n + 1][n + 1];
        int MaxValue = 1000;
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                edges[i][j] = MaxValue;
            }
        }
        for(int[] t:times){
            edges[t[0]][t[1]] = t[2];
        }
        int a = dijstra(edges, k);
        return a;
    }
}