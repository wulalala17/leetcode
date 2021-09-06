/*
704. 二分查找

给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1



提示：

    你可以假设 nums 中的所有元素是不重复的。
    n 将在 [1, 10000]之间。
    nums 的每个元素都将在 [-9999, 9999]之间。
*/
class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length;
        if(target > nums[n - 1] || target < nums[0])
            return -1;
        int i = 0, j = n;
        while(i < j){
            int mid = (i + j) / 2;
            if(target > nums[mid]){
                i = mid + 1;
            }
            else if(target < nums[mid]){
                j = mid;
            }
            else{
                return mid;
            }
        }
        return nums[i] == target?i:-1;
    }
}