5627. 石子游戏 VII
石子游戏中，爱丽丝和鲍勃轮流进行自己的回合，爱丽丝先开始 。
有 n 块石子排成一排。每个玩家的回合中，可以从行中 移除 最左边的石头或最右边的石头，并获得与该行中剩余石头值之 和 相等的得分。当没有石头可移除时，得分较高者获胜。
鲍勃发现他总是输掉游戏（可怜的鲍勃，他总是输），所以他决定尽力 减小得分的差值 。爱丽丝的目标是最大限度地 扩大得分的差值 。
给你一个整数数组 stones ，其中 stones[i] 表示 从左边开始 的第 i 个石头的值，如果爱丽丝和鲍勃都 发挥出最佳水平 ，请返回他们 得分的差值 。

示例 1：
输入：stones = [5,3,1,4,2]
输出：6
解释：
- 爱丽丝移除 2 ，得分 5 + 3 + 1 + 4 = 13 。游戏情况：爱丽丝 = 13 ，鲍勃 = 0 ，石子 = [5,3,1,4] 。
- 鲍勃移除 5 ，得分 3 + 1 + 4 = 8 。游戏情况：爱丽丝 = 13 ，鲍勃 = 8 ，石子 = [3,1,4] 。
- 爱丽丝移除 3 ，得分 1 + 4 = 5 。游戏情况：爱丽丝 = 18 ，鲍勃 = 8 ，石子 = [1,4] 。
- 鲍勃移除 1 ，得分 4 。游戏情况：爱丽丝 = 18 ，鲍勃 = 12 ，石子 = [4] 。
- 爱丽丝移除 4 ，得分 0 。游戏情况：爱丽丝 = 18 ，鲍勃 = 12 ，石子 = [] 。
得分的差值 18 - 12 = 6 。

示例 2：
输入：stones = [7,90,5,1,100,10,10,2]
输出：122
提示：

    n == stones.length
    2 <= n <= 1000
    1 <= stones[i] <= 1000



class Solution {  //参考468题的dp才写出来，py一直超时，Java用二维数组存求和结果就过了，应该有更好的优化方法，还是自己太菜了
    public int stoneGameVII(int[] stones) {
        int n = stones.length;
        if(n==0)
            return 0;
        int[][] dp = new int[n][n];
        int[][] x = new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=i;j<n;j++){
                x[i][j] = sumOfStones(stones, i, j+1);
            }
        }
        for(int i=0;i<n-1;i++){
            dp[i][i+1] = Math.max(stones[i], stones[i+1]);
        }
        int k1, k2;
        for(int i=2;i<n;i++){
            for(int j=0;j<n-i;j++){
                k1 = x[j+1][j+i] - dp[j+1][j+i];
                k2 = x[j][j+i-1] - dp[j][j+i-1];
                dp[j][j+i] = Math.max(k1,k2);
            }
        }
        return dp[0][n-1];
    }
    public static int sumOfStones(int []a, int b, int c){
        int res = 0;
        for(int i=b;i<c;i++)
            res += a[i];
        return res;
    }
}