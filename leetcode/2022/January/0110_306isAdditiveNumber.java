/*
306. 累加数

累加数 是一个字符串，组成它的数字可以形成累加序列。

一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。

给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。

说明：累加序列里的数 不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。



示例 1：

输入："112358"
输出：true
解释：累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

示例 2：

输入："199100199"
输出：true
解释：累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199



提示：

    1 <= num.length <= 35
    num 仅由数字（0 - 9）组成



进阶：你计划如何处理由过大的整数输入导致的溢出?
*/
class Solution {
    boolean check(int i, int j, String num){
        int n = num.length();
        if(n - i - j < i || n - i - j < j){
            return false;
        }
        if(num.charAt(i) == '0' && j > 1 || num.charAt(0) == '0' && i > 1)
            return false;
        long first = Long.valueOf(num.substring(0, i));
        long second = Long.valueOf(num.substring(i, i + j));
        String cur = String.valueOf(first + second);
        int x = i + j;
        while(x < n){
            if(num.substring(x).indexOf(cur) != 0){
                return false;
            }
            x += cur.length();
            first = second;
            second = Long.valueOf(cur);
            cur = String.valueOf(first + second);
        }
        return x == num.length();
    }
    public boolean isAdditiveNumber(String num) {
        for(int i = 1; i < num.length() - 1; i++){
            for(int j = 1; j < num.length() - 1; j++){
                if(check(i, j, num)){
                    return true;
                }
            }
        }
        return false;
    }
}