/*
525. 连续数组

给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。



示例 1:

输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。

示例 2:

输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。



提示：

    1 <= nums.length <= 105
    nums[i] 不是 0 就是 1
*/
class Solution {
    public int findMaxLength(int[] nums) {
        /*int n = nums.length;//又超时了,昨天的思路愣是不知道怎么转换
        int res = 0;
        int cur = 0;
        for(int i = 0; i < n; i++){
            if(nums[i] == 0)
                cur = 1;
            else
                cur = -1;
            for(int j = i+1; j < n; j++){
                if(nums[j] == 0)
                    cur++;
                else
                    cur--;
                if(cur == 0)
                    res = Math.max(j-i+1, res);
            }
        }
        return res;*/
        int n = nums.length;
        for(int i = 0; i < n; i++){
            if(nums[i] == 0)
                nums[i] = -1;
        }
        int res = 0, sum = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (map.containsKey(sum)) {
                res = Math.max(i - map.get(sum), res);
            } else {
                map.put(sum, i);
            }
        }
        return res;
    }
}