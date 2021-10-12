/*
29. 两数相除

给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2



示例 1:

输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

示例 2:

输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2



提示：

    被除数和除数均为 32 位有符号整数。
    除数不为 0。
    假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
*/
class Solution {
    long abs(int x){
        long a = (long)x;
        if(a < 0)
            return -a;
        return a;
    }
    public int divide(int dividend, int divisor) {//减法超时了，位运算好难
        if(dividend == 0)
            return 0;
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }
        boolean flag = false;
        if(dividend > 0 && divisor < 0 || dividend < 0 && divisor > 0){
            flag = true;
        }
        int res = 0;
        long d1 = abs(dividend);
        long d2 = abs(divisor);
        for (int i = 31; i >= 0;i--) {
            if ((d1>>i)>=d2) {//找出足够大的数2^n*divisor
                res+=1<<i;//将结果加上2^n
                d1-=d2<<i;//将被除数减去2^n*divisor
            }
        }
        return flag?-res:res;
    }
}
