/*
229. 求众数 II

给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

示例 1：

输入：[3,2,3]
输出：[3]

示例 2：

输入：nums = [1]
输出：[1]

示例 3：

输入：[1,1,1,3,3,2,2,2]
输出：[1,2]



提示：

    1 <= nums.length <= 5 * 104
    -109 <= nums[i] <= 109



进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。
*/
class Solution {
    public List<Integer> majorityElement(int[] nums) {//摩尔投票法
        List<Integer> res = new ArrayList<>();
        int x = 0, y = 0, countx = 0, county = 0, count = 0;
        for(int n : nums){
            if((countx == 0 || n == x) && n != y){
                x = n;
                countx++;
            }
            else if(county == 0 || n == y){
                y = n;
                county++;
            }
            else{
                countx--;
                county--;
            }
        }
        for(int n: nums){
            if(x == n)
                count++;
        }
        if(count > nums.length / 3){
            res.add(x);
        }
        count = 0;
        for(int n: nums){
            if(y == n)
                count++;
        }
        if(count > nums.length / 3 && y != x){//加上y!=x 防止全是0的情况
            res.add(y);
        }
        return res;
    }
}