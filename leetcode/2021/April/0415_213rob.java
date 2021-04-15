/*
213. 打家劫舍 II

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

示例 1：
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

示例 2：
输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 3：
输入：nums = [0]
输出：0



提示：
    1 <= nums.length <= 100
    0 <= nums[i] <= 1000
*/
class Solution { //DP 很久没有这种自己从不会，一步一步想清思路到会的感觉了，写了得有一个小时
    public int rob(int[] nums) {
        if(nums.length == 1)
            return nums[0];
        if(nums.length == 2)
            return Math.max(nums[0], nums[1]);
        /*int sum1 = 0, sum2 = 0;
        // 1 3 5 7 9 1 3
        int min = 1000;
        if (nums.length % 2 == 0){
            for(int i = 0; i < nums.length; i+=2){
                sum1 += nums[i];
                sum2 += nums[i+1];
            }
            return Math.max(sum1, sum2);
        }
        else{
            for(int i = 1; i < nums.length; i+=2){
                sum1 += nums[i];
                sum2 += nums[i+1];
                min = Math.min(min, nums[i+1]);
            }
            sum2 += nums[0];
            min = Math.min(nums[0], min);
            sum2 -= min;
            return Math.max(sum1, sum2);
        }*/
        int n = nums.length;
        int res = 0;
        int res1 = 0;
        int[][] dp = new int[n][2];
        dp[1][0] = 0;
        dp[1][1] = nums[1];
        for(int i = 2; i < n; i++){ //第一个数一定不选
            dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1]);
            dp[i][1] = dp[i-1][0] + nums[i];
        }
        res = Math.max(dp[n-1][0], dp[n-1][1]);
        dp[1][0] = nums[0];
        dp[1][1] = nums[0];
        for(int i = 2; i < n - 1; i++){ //第一个数一定选, 最后一个数一定不选
            dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1]);
            dp[i][1] = dp[i-1][0] + nums[i];
        }

        res1 = Math.max(dp[n-2][0], dp[n-2][1]);
        res = Math.max(res, res1);
        return res;
    }
}