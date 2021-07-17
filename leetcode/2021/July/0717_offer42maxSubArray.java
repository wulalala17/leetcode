/*
剑指 Offer 42. 连续子数组的最大和

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。



示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。



提示：

    1 <= arr.length <= 10^5
    -100 <= arr[i] <= 100

注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/
*/

class Solution {//DP的思想，做了很多遍，完全凭记忆写出来
    public int maxSubArray(int[] nums) {
        int cur = 0;
        int res = -100;
        for(int i = 0; i < nums.length; i++){
            if(cur < 0){
                cur = nums[i];
            }
            else{
                cur += nums[i];
            }
            res = Math.max(cur, res);
        }
        return res;
    }
}