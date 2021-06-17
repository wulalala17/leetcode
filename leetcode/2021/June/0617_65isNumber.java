/*
65. 有效数字

有效数字（按顺序）可以分成以下几个部分：

    一个 小数 或者 整数
    （可选）一个 'e' 或 'E' ，后面跟着一个 整数

小数（按顺序）可以分成以下几个部分：

    （可选）一个符号字符（'+' 或 '-'）
    下述格式之一：
        至少一位数字，后面跟着一个点 '.'
        至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
        一个点 '.' ，后面跟着至少一位数字

整数（按顺序）可以分成以下几个部分：

    （可选）一个符号字符（'+' 或 '-'）
    至少一位数字

部分有效数字列举如下：

    ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]

部分无效数字列举如下：

    ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。



示例 1：

输入：s = "0"
输出：true

示例 2：

输入：s = "e"
输出：false

示例 3：

输入：s = "."
输出：false

示例 4：

输入：s = ".1"
输出：true



提示：

    1 <= s.length <= 20
    s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.' 。
*/


class Solution {//写得太丑了 面向测试用例编程
    boolean isInteger(String s){
        if(s.length() == 0)
            return false;
        if(s.length() == 1){
            if(s.charAt(0) >= '0' && s.charAt(0) <= '9')
                return true;
            else
                return false;
        }
        char c0 = s.charAt(0);
        if((c0 >= 'a' && c0 <= 'z') || (c0 >= 'A' && c0 <= 'Z') || c0 == '.')
            return false;
        for(int i = 1; i < s.length(); i++){
            if(s.charAt(i) >= '0' && s.charAt(i) <= '9')
                continue;
            else
                return false;
        }
        return true;
    }
    public boolean isNumber(String s) {
        int pointNumber = 0, number = 0;
        char c0 = s.charAt(0);
        if(s.length() == 1){
            if(s.charAt(0) >= '0' && s.charAt(0) <= '9')
                return true;
            else
                return false;
        }
        if((c0 >= 'a' && c0 <= 'z') || (c0 >= 'A' && c0 <= 'Z'))
            return false;
        if(c0 == '.')
            pointNumber++;
        if(c0 >= '0' && c0 <= '9')
            number++;
        for(int i = 1; i < s.length(); i++){
            char c = s.charAt(i);
            if(c == '.'){
                pointNumber++;
                if(pointNumber > 1)
                    return false;
            }
            else if(c == 'e' || c == 'E'){
                if(i == s.length() - 1 || number == 0)
                    return false;
                return isInteger(s.substring(i+1));
            }
            else if(c >= '0' && c <= '9'){
                number++;
                continue;
            }
            else{
                return false;
            }
        }
        if(number == 0)
            return false;
        return true;
    }
}