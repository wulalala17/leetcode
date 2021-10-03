/*
166. 分数到小数

给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。

如果小数部分为循环小数，则将循环的部分括在括号内。

如果存在多个答案，只需返回 任意一个 。

对于所有给定的输入，保证 答案字符串的长度小于 104 。



示例 1：

输入：numerator = 1, denominator = 2
输出："0.5"

示例 2：

输入：numerator = 2, denominator = 1
输出："2"

示例 3：

输入：numerator = 2, denominator = 3
输出："0.(6)"

示例 4：

输入：numerator = 4, denominator = 333
输出："0.(012)"

示例 5：

输入：numerator = 1, denominator = 5
输出："0.2"



提示：

    -231 <= numerator, denominator <= 231 - 1
    denominator != 0
*/
class Solution {//评论里的做法，好强，想不到这么做。模拟除法，用整数直接除来算每一位
    public String fractionToDecimal(int numerator, int denominator) {
        StringBuffer res = new StringBuffer();
        if(numerator < 0 && denominator > 0 || numerator > 0 && denominator < 0)
            res.append('-');
        long a = numerator, b = denominator;
        a = Math.abs(a);
        b = Math.abs(b);
        res.append(String.valueOf(a / b));
        if(a % b == 0)
            return res.toString();
        res.append('.');
        Map<Long, Integer> map = new HashMap<>();
        a = a % b * 10;
        while(a > 0 && !map.containsKey(a)){
            map.put(a, res.length());
            res.append(String.valueOf(a / b));
            a = a % b * 10;
        }
        if(a == 0)
            return res.toString();
        res.insert(map.get(a).intValue(), '(');
        res.append(')');
        return res.toString();
    }
}