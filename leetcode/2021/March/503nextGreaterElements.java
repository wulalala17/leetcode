/*503. 下一个更大元素 II

给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:

输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

注意: 输入数组的长度不会超过 10000。
通过次数51,284
提交次数85,010*/

class Solution { // 暴力击败6%
    public int[] nextGreaterElements(int[] nums) {
        int [] res = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            res[i] = -1;
            int j = i+1;
            while(j!=i){
                if (j==nums.length)
                    j = 0;
                if (j == i)
                    break;
                if (nums[j] > nums[i]){
                    res[i] = nums[j];
                    break;
                }
                j++;
            }
        }
        return res;
    }
}


/*class Solution {  // 正确做法
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] ret = new int[n];
        Arrays.fill(ret, -1);
        Deque<Integer> stack = new LinkedList<Integer>();
        for (int i = 0; i < n * 2 - 1; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i % n]) {
                ret[stack.pop()] = nums[i % n];
            }
            stack.push(i % n);
        }
        return ret;
    }
}

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/next-greater-element-ii/solution/xia-yi-ge-geng-da-yuan-su-ii-by-leetcode-bwam/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。*/