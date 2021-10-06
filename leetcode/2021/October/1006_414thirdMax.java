/*
414. 第三大的数

给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。



示例 1：

输入：[3, 2, 1]
输出：1
解释：第三大的数是 1 。

示例 2：

输入：[1, 2]
输出：2
解释：第三大的数不存在, 所以返回最大的数 2 。

示例 3：

输入：[2, 2, 3, 1]
输出：1
解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。



提示：

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1



进阶：你能设计一个时间复杂度 O(n) 的解决方案吗？
*/
class Solution {
    public int thirdMax(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int res = nums[n - 1];
        int cur = 1, pre = res;
        for(int i = n - 2; i >= 0; i--){
            if(nums[i] != pre){
                pre = nums[i];
                cur++;
            }
            if(cur == 3)
                return nums[i];
        }
        return res;
    }
}
/*
class Solution {
    // Long.MIN_VALUE=-9223372036854775808(-2的63次方)
    private long MIN_VALUE = Long.MIN_VALUE;
    public int thirdMax(int[] nums) {
        // 初始化第一,第二以及第三大元素
        long firstElement = MIN_VALUE,secondElement = MIN_VALUE,thirdElement = MIN_VALUE;
        // 遍历数组,获取第一,第二以及第三大元素
        for(int num : nums) {
            if(num > firstElement) {
                thirdElement = secondElement;
                secondElement = firstElement;
                firstElement = num;
            }else if(secondElement < num && num < firstElement) {
                thirdElement = secondElement;
                secondElement = num;
            }else if (thirdElement < num && num < secondElement) {
                thirdElement = num;
            }
        }
        // 若无第三大元素则返回数组中的最大值
        return thirdElement==MIN_VALUE ? (int)firstElement : (int)thirdElement;
    }
}
*/