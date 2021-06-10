/*
518. 零钱兑换 II

给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。



示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

示例 2:

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。

示例 3:

输入: amount = 10, coins = [10]
输出: 1



注意:

你可以假设：

    0 <= amount (总金额) <= 5000
    1 <= coin (硬币面额) <= 5000
    硬币种类不超过 500 种
    结果符合 32 位符号整数
*/
class Solution {//一维还是比二维简洁多了，我写的才超过18%
    public int change(int amount, int[] coins) {
        if(amount == 0)
            return 1;
        int[][] dp = new int[coins.length + 1][amount + 1];//前i个硬币凑成金额恰好为j的组合
        for(int i = 1; i < coins.length + 1; i++){
            for(int j = 1; j < amount + 1; j++){
                if(coins[i - 1] > j)
                    dp[i][j] = dp[i-1][j];
                else if(coins[i-1] == j)
                    dp[i][j] = dp[i-1][j] + 1;
                else
                    dp[i][j] = dp[i][j - coins[i-1]] + dp[i-1][j];
            }
        }
        return dp[coins.length][amount];
    }
}

/*class Solution {//评论区简洁版
    public int change(int amount, int[] coins) {
        int dp[] = new int[amount+1];
        // 设置起始状态
        dp[0] = 1;

        for (int coin : coins) {
            // 记录每添加一种面额的零钱，总金额j的变化
            for (int j = 1; j <= amount; j++) {
                if (j >= coin) {
                    // 在上一钟零钱状态的基础上增大
                    // 例如对于总额5，当只有面额为1的零钱时，只有一种可能 5x1
                    // 当加了面额为2的零钱时，除了原来的那一种可能外
                    // 还加上了组合了两块钱的情况，而总额为5是在总额为3的基础上加上两块钱来的
                    // 所以就加上此时总额为3的所有组合情况
                    dp[j] = dp[j] + dp[j - coin];
                }
            }
        }
        return dp[amount];
    }
}*/