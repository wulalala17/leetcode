/*
400. 第 N 位数字

给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n 位数字。



示例 1：

输入：n = 3
输出：3

示例 2：

输入：n = 11
输出：0
解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。



提示：

    1 <= n <= 231 - 1
*/
class Solution {
    public int findNthDigit(int n) {
        if(n < 10)
            return n;
        int d = 1, count = 9;
        while(n > (long)d * count){
            n -= d * count;
            d++;
            count *= 10;
        }
        int x = --n;
        int start = (int)Math.pow(10, d - 1);
        int nowNumber = start + n / d;
        int idx = n % d;
        int res = (nowNumber / (int)(Math.pow(10, d - idx - 1))) % 10;
        return res;
    }
}