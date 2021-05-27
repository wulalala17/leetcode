/*
461. 汉明距离

两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。
*/
class Solution {//一开始i++写顺手了超时，用了转二进制做法真傻
    public int hammingDistance(int x, int y) {
        /*int x1 = 0, x2 = 0, res = 0;
        String s1 = Integer.toBinaryString(x);
        String s2 = Integer.toBinaryString(y);
        int len1 = s1.length(), len2 = s2.length();
        if(len1 < len2){
            int c = len2 - len1;
            while(c > 0){
                s1 = '0' + s1;
                c--;
            }
        }
        else if(len1 > len2){
            int c = len1 - len2;
            while(c > 0){
                s2 = '0' + s2;
                c--;
            }
        }
        for(int i = 0;i < s1.length(); i++){
            if(s1.charAt(i) != s2.charAt(i))
                res++;
        }
        return res;*/

        int x1 = 0, x2 = 0, res = 0;
        for(int i = 30; i >= 0; i--){
            x1 = (x >> i) & 1;
            x2 = (y >> i) & 1;
            res += (x1 == x2?0:1);
        }
        return res;

    }
}