/*
664. 奇怪的打印机

有台奇怪的打印机有以下两个特殊要求：

    打印机每次只能打印由 同一个字符 组成的序列。
    每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。

给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。


示例 1：

输入：s = "aaabbb"
输出：2
解释：首先打印 "aaa" 然后打印 "bbb"。

示例 2：

输入：s = "aba"
输出：2
解释：首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。



提示：

    1 <= s.length <= 100
    s 由小写英文字母组成
*/
class Solution {//把状态方程想简单了，一看没过的样例就不知道怎么写了
    public int strangePrinter(String s) {
        /*int n = s.length();
        if(n == 1)
            return 1;
        int[] dp = new int[n+1];
        dp[0] = 1;
        HashMap<Character, Integer> map = new HashMap<>();
        map.put(s.charAt(0), 1);
        for(int i = 1; i < n; i++){
            char c = s.charAt(i);
            if(s.charAt(i) == s.charAt(i-1)){
                dp[i] = dp[i - 1];
            }
            else{
                if(map.containsKey(c)){
                    dp[i] = Math.min(dp[i - 1] + 1, map.get(c) + (dp[i-1] - map.get(c)) );
                }
                else{
                    dp[i] = dp[i - 1] + 1;
                }
            }
            map.put(c, dp[i]);
        }
        return dp[n - 1]; */
        int n = s.length();
        int[][] f = new int[n][n];
        for (int i = n - 1; i >= 0; i--) {
            f[i][i] = 1;
            for (int j = i + 1; j < n; j++) {
                if (s.charAt(i) == s.charAt(j)) {
                    f[i][j] = f[i][j - 1];
                } else {
                    int minn = Integer.MAX_VALUE;
                    for (int k = i; k < j; k++) {
                        minn = Math.min(minn, f[i][k] + f[k + 1][j]);
                    }
                    f[i][j] = minn;
                }
            }
        }
        return f[0][n - 1];
    }
}