/*
413. 等差数列划分

如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

    例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。

给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

子数组 是数组中的一个连续序列。



示例 1：
输入：nums = [1,2,3,4]
输出：3
解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。

示例 2：
输入：nums = [1]
输出：0

123456
3 1
4 1 + 2
5 1 + 2 + 3
6 1 + 2 + 3 +4
提示：

    1 <= nums.length <= 5000
    -1000 <= nums[i] <= 1000
*/
class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int n = nums.length;
        if(n < 3)
            return 0;
        List<Integer> start = new ArrayList<>();
        List<Integer> end = new ArrayList<>();
        int l = 0;
        int res = 0, cur = 0, f = 0;
        int d = nums[1] - nums[0];
        int s = 0;
        for(int i = 2; i < n; i++){
            if(nums[i] - nums[i - 1] == d){
                f = 1;
                continue;
            }
            else{
                if(f == 1){//已经构成等差数列
                    start.add(s);
                    end.add(i - 1);
                }
                d = nums[i] - nums[i - 1];
                f = 0;
                s = i - 1;
            }
        }
        if(f == 1){
            start.add(s);
            end.add(n - 1);
        }
        for(int i = 0; i < start.size(); i++){
            l = end.get(i) - start.get(i) + 1;
            res += (l - 1) * (l - 2) / 2;
        }
        return res;
    }
}