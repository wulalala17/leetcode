/*
220. 存在重复元素 III

给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。
如果存在则返回 true，不存在返回 false。

示例 1：
输入：nums = [1,2,3,1], k = 3, t = 0
输出：true

示例 2：
输入：nums = [1,0,1,1], k = 1, t = 2
输出：true

示例 3：
输入：nums = [1,5,9,1,5,9], k = 2, t = 3
输出：false

提示：

    0 <= nums.length <= 2 * 104
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 104
    0 <= t <= 231 - 1
*/
class Solution { //带下标的排序，变相暴力
    public class Number implements Comparable<Number>{
        Integer data;
        int index;

        Number(int d, int i){
            this.data = d;
            this.index = i;
        }

        @Override
        public int compareTo(Number o) {
            return this.data.compareTo(o.data);
        }
    }

    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        int n = nums.length;
        Number sorted[] = new Number[n];
        for (int i = 0; i < n; i++) {
            sorted[i] = new Number(nums[i], i);
        }
        Arrays.sort(sorted);
        int j = 0;
        for(int i = 0; i < n; i++){
            long x = (long)sorted[i].data + t;
            int idx = sorted[i].index;
            j = i + 1;
            while(j < n && (long)sorted[j].data <= x){
                if(Math.abs(sorted[j].index - idx) <= k)
                    return true;
                else{
                    j++;
                }
            }
        }
        return false;
    }
}