class Solution{//回到学校上不去力扣，很奇怪，只能手机刷题了
    public int[] runningSum(int[] nums){
        int[] res = new int[nums.length];
        res[0] = nums[0];
        for(int i = 1; i < nums.length; i++)
            res[i] = res[i-1] + nums[i];
        return res;
    }
}