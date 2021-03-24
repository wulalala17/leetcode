/*456. 132模式

给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。
设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。
注意：n 的值小于15000。

示例1:
输入: [1, 2, 3, 4]
输出: False
解释: 序列中不存在132模式的子序列。

示例 2:
输入: [3, 1, 4, 2]
输出: True
解释: 序列中有 1 个132模式的子序列： [1, 4, 2].

示例 3:
输入: [-1, 3, 2, 0]
输出: True
解释: 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和 [-1, 2, 0].
*/

class Solution {
    public boolean find132pattern(int[] nums) { //自己写的暴力5%，别人的单调栈33%
        // int[] a = new int[nums.length];
        // for (int i = 0; i < nums.length; i++){
        //     a[i] = nums[i];
        // }
        // for (int i = 1; i < nums.length-1; i++){ //往前找比nums[i]小的数字
        //     for (int j = 0; j < i; j++){
        //         if(nums[j] < a[i])
        //             a[i] = nums[j];
        //     }
        // }
        // for (int i = 1; i < nums.length-1; i++){ //往后找比nums[i]大的数字
        //     for (int j = i+1; j < nums.length; j++){
        //         if(a[i] != nums[i]  && nums[j] > a[i] && nums[j] < nums[i])
        //             return true;
        //     }
        // }
        // return false;
        Stack<Integer> stack = new Stack<>();
        Integer last = Integer.MIN_VALUE;
        for(int i = nums.length - 1;i>=0;i--){
            if (nums[i] < last)
                return true;
            while(!stack.empty() && nums[i] > stack.peek())
                last = stack.pop();
            stack.push(nums[i]);
        }
        return false;

    }
}
