/*
689. 三个无重叠子数组的最大和

给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且 3 * k 项的和最大的子数组，并返回这三个子数组。

以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。



示例 1：

输入：nums = [1,2,1,2,6,7,5,1], k = 2
输出：[0,3,5]
解释：子数组 [1, 2], [2, 6], [7, 5] 对应的起始下标为 [0, 3, 5]。
也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。

示例 2：

输入：nums = [1,2,1,2,1,2,1,2,1], k = 2
输出：[0,2,4]



提示：

    1 <= nums.length <= 2 * 104
    1 <= nums[i] < 216
    1 <= k <= floor(nums.length / 3)
*/
class Solution {//看了题解才会的DP
    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        int n = nums.length;
        long[] preSum = new long[n - k + 1];//以i开头连续k位的和
        int[] maxLeft = new int[n - k + 1];//preSum数组从0到i的最大值所在下标
        int[] maxRight = new int[n - k + 1];//preSum数组从n - k到i的最大值所在下标
        long sum = 0;
        for(int i = 0; i < k; i++){
            sum += nums[i];
        }
        preSum[0] = sum;
        for(int i = 1; i < n - k + 1; i++){
            preSum[i] = preSum[i - 1] - nums[i - 1] + nums[i + k - 1];
        }
        long max = preSum[0];
        for(int i = 1; i < n - k + 1; i++){
            if(preSum[i] > max){
                max = preSum[i];
                maxLeft[i] = i;
            }
            else{
                maxLeft[i] = maxLeft[i - 1];
            }
        }
        max = preSum[n - k];
        maxRight[n - k] = n - k;
        for(int i = n - k - 1; i >= 0; i--){
            if(preSum[i] >= max){//这里要取等号，不然会出错
                max = preSum[i];
                maxRight[i] = i;
            }
            else{
                maxRight[i] = maxRight[i + 1];
            }
        }
        int[] res = new int[3];
        max = 0;
        for(int i = k; i <= n - 2 * k; i++){//i最大值只能是n - 2 * k, 因为i占了k位，右边还需要k位
            if(preSum[maxLeft[i - k]] + preSum[i] + preSum[maxRight[i + k]] > max){
                max = preSum[maxLeft[i - k]] + preSum[i] + preSum[maxRight[i + k]];
                res[0] = maxLeft[i - k];
                res[1] = i;
                res[2] = maxRight[i + k];
            }
        }
        return res;
    }
}