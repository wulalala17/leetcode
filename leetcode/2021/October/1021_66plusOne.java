/*
66. 加一

给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。



示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例 2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：

输入：digits = [0]
输出：[1]



提示：

    1 <= digits.length <= 100
    0 <= digits[i] <= 9
*/
class Solution {
    public int[] plusOne(int[] digits) {
        int pre = 1;//进位
        int n = digits.length;
        for(int i = n - 1; i >= 0; i--){
            if(digits[i] + pre >= 10){
                pre = 1;
                digits[i] = (digits[i] + pre) % 10;
            }
            else{
                digits[i] += 1;
                return digits;
            }
        }
        if(pre > 0){
            int[] res = new int[n + 1];
            res[0] = 1;
            for(int i = 1; i <= n; i++){
                res[i] = digits[i - 1];
            }
            return res;
        }
        return digits;
    }
}