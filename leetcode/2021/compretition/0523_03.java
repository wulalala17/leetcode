/*
5765. 跳跃游戏 VII

给你一个下标从 0 开始的二进制字符串 s 和两个整数 minJump 和 maxJump 。一开始，你在下标 0 处，且该位置的值一定为 '0' 。当同时满足如下条件时，你可以从下标 i 移动到下标 j 处：

    i + minJump <= j <= min(i + maxJump, s.length - 1) 且
    s[j] == '0'.

如果你可以到达 s 的下标 s.length - 1 处，请你返回 true ，否则返回 false 。



示例 1：

输入：s = "011010", minJump = 2, maxJump = 3
输出：true
解释：
第一步，从下标 0 移动到下标 3 。
第二步，从下标 3 移动到下标 5 。

示例 2：

输入：s = "01101110", minJump = 2, maxJump = 3
输出：false



提示：

    2 <= s.length <= 105
    s[i] 要么是 '0' ，要么是 '1'
    s[0] == '0'
    1 <= minJump <= maxJump < s.length
*/
class Solution {
    public boolean canReach(String s, int minJump, int maxJump) {
        // Queue<Integer> q = new LinkedList<>();//超时的BFS
        // HashSet<Integer> set = new HashSet<>();
        // q.offer(0);
        // set.add(0);
        // int l = 0;
        // while(!q.isEmpty()){
        //     l = q.size();
        //     while(l > 0){
        //         int x = q.poll();
        //         for(int i = x + minJump; i <= x + maxJump && i < s.length(); i++){
        //             if (s.charAt(i) == '0' && !set.contains(i)){
        //                 q.offer(i);
        //                 set.add(i);
        //                 if(i == s.length()-1)
        //                     return true;
        //             }
        //         }
        //         l--;
        //     }
        // }
        // return false;

        /*int n = s.length(); // DP版本
        boolean[] dp = new boolean[n];
        dp[0] = true;
        for(int i = 1; i < n; i++){
            if(s.charAt(i) == '0'){
                for(int j = i - minJump; j >= 0 && j >= i - maxJump; j--){
                    if(dp[j] == true){
                        dp[i] = true;
                        break;
                    }
                }
            }
        }
        return dp[n - 1];*/

        int n = s.length();//DP+前缀和
        int[] pre = new int[n];
        int[] f = new int[n];
        for(int i = 0; i < minJump; i++)
            pre[i] = 1;
        for(int i = minJump; i < n; i++){
            int l = i - maxJump, r = i - minJump;
            if(s.charAt(i) == '0'){
                int total = pre[r] - (l > 0 ? pre[l-1]:0);
                f[i] = total > 0? 1 : 0;
            }
            pre[i] = pre[i - 1] + f[i];
        }
        return f[n-1] == 1;
    }
}