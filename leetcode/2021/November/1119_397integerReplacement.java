/*
397. 整数替换

给定一个正整数 n ，你可以做如下操作：

    如果 n 是偶数，则用 n / 2替换 n 。
    如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。

n 变为 1 所需的最小替换次数是多少？



示例 1：

输入：n = 8
输出：3
解释：8 -> 4 -> 2 -> 1

示例 2：

输入：n = 7
输出：4
解释：7 -> 8 -> 4 -> 2 -> 1
或 7 -> 6 -> 3 -> 2 -> 1

示例 3：

输入：n = 4
输出：2



提示：

    1 <= n <= 231 - 1
*/
class Solution {//只想到最慢的BFS 位运算和贪心都没想到
    public int integerReplacement(int n) {
        /*int[] dp = new int[n + 1];
        dp[1] = 0;
        dp[2] = 1;
        dp[3] = 2;
        for(int i = 4; i <= n; i++){
            if(i % 2 == 0){
                dp[i] = Math.min(dp[i / 2], dp[i - 1]) + 1;
            }
            else{
                dp[i] = dp[i - 1] + 1;
            }
        }
        return dp[n];*/

        Set<Long> set = new HashSet<>();
        set.add((long)n);
        int res = 0;
        long t = 1;
        while(!set.contains(t)){
            Set<Long> set1 = new HashSet<>();
            for(long x:set){
                if(x % 2 == 0){
                    set1.add(x / 2);
                }
                else{
                    set1.add(x + 1);
                    set1.add(x - 1);
                }
            }
            res++;
            set = set1;
        }
        return res;
    }
}