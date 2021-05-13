/*
1269. 停在原地的方案数

有一个长度为 arrLen 的数组，开始有一个指针在索引 0 处。

每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。

给你两个整数 steps 和 arrLen ，请你计算并返回：在恰好执行 steps 次操作以后，指针仍然指向索引 0 处的方案数。

由于答案可能会很大，请返回方案数 模 10^9 + 7 后的结果。



示例 1：

输入：steps = 3, arrLen = 2
输出：4
解释：3 步后，总共有 4 种不同的方法可以停在索引 0 处。
向右，向左，不动
不动，向右，向左
向右，不动，向左
不动，不动，不动

示例  2：

输入：steps = 2, arrLen = 4
输出：2
解释：2 步后，总共有 2 种不同的方法可以停在索引 0 处。
向右，向左
不动，不动

示例 3：

输入：steps = 4, arrLen = 2
输出：8



提示：

    1 <= steps <= 500
    1 <= arrLen <= 10^6
*/
class Solution {//优化数组程度成steps/2没想到，还是超时了
    public int numWays(int steps, int arrLen) {
        if(arrLen == 1)
            return 1;
        // int[][] dp = new int[steps + 1][arrLen + 1];
        // dp[1][0] = 1;
        // dp[1][1] = 1;
        // for(int i = 2;i <= steps; i++){
        //     for(int j = 0; j < arrLen; j++){
        //         if(j == 0)
        //             dp[i][j] = dp[i-1][j] + dp[i-1][j+1];
        //         else if(j < arrLen)
        //             dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1];
        //         else
        //             dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
        //     }
        // }
        // return dp[steps][0];
        int len = Math.min(arrLen, steps / 2 + 1);
        long[] dp = new long[len];
        long[] t = new long[len];
        int m = 1000000000 + 7;
        dp[0] = 1;
        dp[1] = 1;
        int f = 0;
        for(int i = 2; i <= steps; i++){
            if(f == 0){
                t[0] = dp[0] % m + dp[1] % m;
                t[0] %= m;
                for(int j = 1; j < len - 1; j++){
                    t[j] = dp[j - 1] % m + dp[j] % m + dp[j + 1] % m;
                    t[j] %= m;
                }
                t[len - 1] = dp[len - 2] % m + dp[len - 1] % m;
                t[len - 1] %= m;
                f = 1;
            }
            else{
                dp[0] = t[0] % m + t[1] % m;
                dp[0] %= m;
                for(int j = 1; j < len - 1; j++){
                    dp[j] = t[j - 1] % m + t[j] % m + t[j + 1] % m;
                    dp[j] %= m;
                }
                dp[len - 1] = t[len - 2] % m + t[len - 1] % m;
                dp[len - 1] %= m;
                f = 0;
            }
        }
        if(f == 0)
            return (int)dp[0];
        else
            return (int)t[0];
    }
}