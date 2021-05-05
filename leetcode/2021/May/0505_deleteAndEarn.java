/*
740. 删除并获得点数

给你一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。



示例 1：

输入：nums = [3,4,2]
输出：6
解释：
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。

示例 2：

输入：nums = [2,2,3,3,3,4]
输出：9
解释：
删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。



提示：

    1 <= nums.length <= 2 * 104
    1 <= nums[i] <= 104
*/
class Solution {//麻烦的DP
    public int deleteAndEarn(int[] nums) {
        Arrays.sort(nums);
        HashMap<Integer, Integer> map = new HashMap();
        for(int n:nums){
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        List<Integer> l = new ArrayList();
        int x = nums[0];
        for(int i = 1; i < nums.length; i++){
            if(nums[i] != x){
                l.add(nums[i]);
                x = nums[i];
            }
        }
        int dp0 = 0; //不选当前数
        int dp1 = nums[0] * map.get(nums[0]); //选当前数
        int newdp0;
        x = nums[0]; //前一个数
        for(int n: l){
            if(n != x + 1){
                dp0 = Math.max(dp0, dp1);
                dp1 = dp0 + n * map.get(n);
                x = n;
            }
            else{
                newdp0 = Math.max(dp0, dp1);
                dp1 = dp0 + n * map.get(n);
                dp0 = newdp0;
                x = n;
            }
        }
        return Math.max(dp0, dp1);

    }
}