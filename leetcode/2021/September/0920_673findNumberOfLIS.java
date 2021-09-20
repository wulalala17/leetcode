/*
673. 最长递增子序列的个数

给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。

示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。

注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
*/

class Solution {//改了半天，最后还是看了评论的代码，发现写得出奇的像
    public int findNumberOfLIS(int[] nums) {
        int n = nums.length;
        if(n == 0)
            return 0;
        int[] dp = new int[n];//以i结尾的最长自增序列长度
        int[] t = new int[n];//以i结尾的最长自增序列个数
        for(int i = 0; i < n; i++){
            dp[i] = 1;
            t[i] = 1;
        }
        int max = 1;
        int res = 1;
        for(int i = 1; i < n; i++){
            for(int j = i - 1; j >= 0; j--){
                if(nums[i] > nums[j]){
                    if(dp[j] + 1 > dp[i]){
                        dp[i] = dp[j] + 1;
                        t[i] = t[j];
                    }
                    else if(dp[j] + 1 == dp[i]){
                        t[i] += t[j];
                    }
                }
            }
            if(dp[i] > max){
                max = dp[i];
                res = t[i];
            }
            else if(dp[i] == max){
                res += t[i];
            }
        }
        return res;
    }
}