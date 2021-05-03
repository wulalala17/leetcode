/*
7. 整数反转

给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。


示例 1：
输入：x = 123
输出：321

示例 2：
输入：x = -123
输出：-321

示例 3：
输入：x = 120
输出：21

示例 4：
输入：x = 0
输出：0

提示：

    -231 <= x <= 231 - 1
*/
class Solution {//用int 判断溢出写了半天
    public int reverse(int x) {
        if (x == -Math.pow(2, 31))
            return 0;
        int f = 0, res = 0, newres = 0;
        if (x < 0){
            x = -x;
            f = 1;
        }
        while(x > 0){
            if(res > Math.pow(10, 8)){
                if(res / 100000000 > 2) //溢出
                    return 0;
                newres = res * 10 + x % 10;
                if(newres < res){//溢出
                    return 0;
                }
                else{
                    res = newres;
                    x = x / 10;
                }
            }
            else{
                res = res * 10 + x % 10;
                x = x / 10;
            }

        }
        if(f == 1)
            res = -res;
        return res;
    }
}

/*class Solution {//大佬做法，用除以10是否等于原来的数来判断有没有溢出
    public int reverse(int x) {
        int res = 0;
        while (x != 0) {
            int tmp = res * 10 + x % 10;
            if (tmp / 10 != res) { // 溢出!!!
                return 0;
            }
            res = tmp;
            x /= 10;
        }
        return res;
    }
}*/
