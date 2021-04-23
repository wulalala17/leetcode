/*
368. 最大整除子集
给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：

    answer[i] % answer[j] == 0 ，或
    answer[j] % answer[i] == 0

如果存在多个有效解子集，返回其中任何一个均可。



示例 1：

输入：nums = [1,2,3]
输出：[1,2]
解释：[1,3] 也会被视为正确答案。

示例 2：

输入：nums = [1,2,4,8]
输出：[1,2,4,8]



提示：

    1 <= nums.length <= 1000
    1 <= nums[i] <= 2 * 109
    nums 中的所有整数 互不相同
*/

class Solution {//暴力行不通，没想到是DP

    public List<Integer> largestDivisibleSubset(int[] nums) {
        /*Arrays.sort(nums);
        List<List<Integer>> l = new ArrayList<List<Integer>>();
        int f = 0, f2 = 0;
        for(int n:nums){
            for(int i = 0; i < l.size(); i++){
                f2 = 1;
                List<Integer> x = l.get(i);
                f = 0;
                for(int j = 0; j < x.size(); j++){
                    if (n % x.get(j) != 0){
                        f = 1;
                        break;
                    }
                }
                if(f == 0){
                    x.add(n);
                }
            }
            if (f == 1 || f2 == 0){
                List<Integer> newx = new ArrayList<>();
                newx.add(n);
                l.add(newx);
            }
            f2 = 0;
        }
        int max = 0;
        int m, idx = 0;
        for(int i = 0; i < l.size(); i++){
            m = l.get(i).size();
            if (m > max){
                max = m;
                idx = i;
            }
        }
        return l.get(idx);*/
        int n = nums.length;
        int[] dp = new int[n];
        List<Integer> res = new ArrayList();
        if(n == 0)
            return res;
        Arrays.sort(nums);
        Arrays.fill(dp, 1);
        int max = 1, idx = 0;
        for(int i = 1; i < n; i++){
            for(int j = 0; j < i; j++){
                if (nums[i] % nums[j] == 0)
                    dp[i] = Math.max(dp[j]+1, dp[i]);
            }
            if (dp[i] > max){
                max = dp[i];
                idx = i;
            }
        }
        int x = nums[idx];
        for(int i = idx; i >=0; i--){
            if(x % nums[i] == 0 && dp[i] == max){
                x = nums[i];
                res.add(nums[i]);
                max--;
            }
        }
        return res;

    }
}