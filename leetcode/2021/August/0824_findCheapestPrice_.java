/*
787. K 站中转内最便宜的航班

有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [fromi, toi, pricei] ，表示该航班都从城市 fromi 开始，以价格 toi 抵达 pricei。

现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的 价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。



示例 1：

输入:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
输出: 200
解释:
城市航班图如下


从城市 0 到城市 2 在 1 站中转以内的最便宜价格是 200，如图中红色所示。

示例 2：

输入:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
输出: 500
解释:
城市航班图如下


从城市 0 到城市 2 在 0 站中转以内的最便宜价格是 500，如图中蓝色所示。



提示：

    1 <= n <= 100
    0 <= flights.length <= (n * (n - 1) / 2)
    flights[i].length == 3
    0 <= fromi, toi < n
    fromi != toi
    1 <= pricei <= 104
    航班没有重复，且不存在自环
    0 <= src, dst, k < n
    src != dst
*/
class Solution {//dj不会 DP好难想啊
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int[][] dp = new int[n][k+2];
        for(int i = 0; i < n; ++i)
            Arrays.fill(dp[i], Integer.MAX_VALUE);
        for(int i = 0; i <= k+1; ++i)
            dp[src][i] = 0;
        for(int i = 1; i <= k+1; ++i) {
            for(int[] flight : flights) {
                if(dp[flight[0]][i - 1] != Integer.MAX_VALUE)
                    dp[flight[1]][i] = Math.min(dp[flight[1]][i], dp[flight[0]][i-1] + flight[2]);
            }
        }
        return dp[dst][k+1] == Integer.MAX_VALUE ? -1 : dp[dst][k+1];
    }
}



/**
动态规划解法, dp[i][k]表示经过k个中转站后到达站i的最低费用
初始除了dp[src][0]~dp[src][k]之外所有的元素置为无穷大inf
则状态方程为: 对于所有目标地位i的航班(flight[1] = i)
只要dp[flight[0]][k-1] != inf就更新dp[i][k]
dp[i][k] = Math.min(dp[i][k], dp[flight[0]][k-1])
**/



