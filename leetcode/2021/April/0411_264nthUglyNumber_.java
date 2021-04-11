/*
264. 丑数 II

给你一个整数 n ，请你找出并返回第 n 个 丑数 。
丑数 就是只包含质因数 2、3 和/或 5 的正整数。



示例 1：
输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。

示例 2：
输入：n = 1
输出：1
解释：1 通常被视为丑数。

提示：

    1 <= n <= 1690
*/
class Solution { // 三指针，没做出来
    public int nthUglyNumber(int n) {
        int a, b, c, next;
        int[] ugly = new int[n];
        int[] idx = new int[3];
        for(int i = 0; i < n; i++){
            ugly[i] = 1;
        }
        for(int i = 1; i < n; i++){
            a = ugly[idx[0]] * 2;
            b = ugly[idx[1]] * 3;
            c = ugly[idx[2]] * 5;
            next = Math.min(Math.min(a, b), c);
            if(next == a)
                idx[0]++;
            if(next == b)
                idx[1]++;
            if(next == c)
                idx[2]++;
            ugly[i] = next;
        }
        return ugly[n-1];
    }

    // public static boolean isUglyNumber(int n){
    //     if (n < 1)
    //         return false;
    //     while(n > 1){
    //         while(n % 2 == 0)
    //             n /= 2;
    //         while(n % 3 == 0)
    //             n /= 3;
    //         while(n % 5 == 0)
    //             n /= 5;
    //         break;
    //     }
    //     return n == 1;
    // }
}