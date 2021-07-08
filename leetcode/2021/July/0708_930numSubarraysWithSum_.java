/*
930. 和相同的二元子数组

给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。

子数组 是数组的一段连续部分。



示例 1：

输入：nums = [1,0,1,0,1], goal = 2
输出：4
解释：
如下面黑体所示，有 4 个满足题目要求的子数组：
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

示例 2：

输入：nums = [0,0,0,0,0], goal = 0
输出：15



提示：

    1 <= nums.length <= 3 * 104
    nums[i] 不是 0 就是 1
    0 <= goal <= nums.length
*/
class Solution {//前缀和这么明显还能忘了怎么写
    public int numSubarraysWithSum(int[] nums, int goal) {
        int res = 0, sum = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        for(int i = 0; i < nums.length; i++){
            sum += nums[i];
            if(map.containsKey(sum - goal)){
                res += map.get(sum - goal);
            }
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return res;
    }
}