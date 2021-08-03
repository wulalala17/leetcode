/*
581. 最短无序连续子数组

给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。



示例 1：

输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

示例 2：

输入：nums = [1,2,3,4]
输出：0

示例 3：

输入：nums = [1]
输出：0



提示：

    1 <= nums.length <= 104
    -105 <= nums[i] <= 105

进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？
*/

class Solution {//排序对比
    public int findUnsortedSubarray(int[] nums) {
        int n = nums.length;
        int[] source = new int[n];
        for(int i = 0; i < n; i++){
            source[i] = nums[i];
        }
        Arrays.sort(nums);
        int start = 0, end = n - 1;
        while(start < n && nums[start] == source[start])
            start++;
        if(start == n)
            return 0;
        while(end >= 0 && nums[end] == source[end])
            end--;
        return end - start + 1;
    }
}