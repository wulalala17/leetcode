/*523. 连续的子数组和

给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：

    子数组大小 至少为 2 ，且
    子数组元素总和为 k 的倍数。

如果存在，返回 true ；否则，返回 false 。

如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。



示例 1：

输入：nums = [23,2,4,6,7], k = 6
输出：true
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。

示例 2：

输入：nums = [23,2,6,4,7], k = 6
输出：true
解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。
42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。

示例 3：

输入：nums = [23,2,6,4,7], k = 13
输出：false



提示：

    1 <= nums.length <= 105
    0 <= nums[i] <= 109
    0 <= sum(nums[i]) <= 231 - 1
    1 <= k <= 231 - 1
*/
class Solution {//看的官方题解，想到了同余定理算和，但没想到两次出现同样的余数说明区间和为倍数这种应用
    public boolean checkSubarraySum(int[] nums, int k) {
        /*int len = nums.length; //暴力法超时
        int[] prefix = new int[len];
        prefix[0] = nums[0];
        for(int i = 1; i < len; i++){
            prefix[i] = prefix[i - 1] + nums[i];
            if(prefix[i] % k == 0)
                return true;
        }
        for(int i = 1; i < len; i++){
            for(int j = i + 1; j < len; j++){
                if((prefix[j] - prefix[i] + nums[i]) % k == 0)
                    return true;
            }
        }
        return false;*/
        int len = nums.length;
        int sum = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);
        for(int i = 0; i < len; i++){
            sum = (sum + nums[i]) % k;
            if(map.containsKey(sum)){
                int preIdx = map.get(sum);
                if (i - preIdx >= 2)
                    return true;
                //map.put(sum, i);
            }
            else{
                map.put(sum, i);
            }
        }
        return false;
    }
}