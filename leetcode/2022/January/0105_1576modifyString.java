/*
1576. 替换所有的问号

给你一个仅包含小写英文字母和 '?' 字符的字符串 s，请你将所有的 '?' 转换为若干小写字母，使最终的字符串不包含任何 连续重复 的字符。

注意：你 不能 修改非 '?' 字符。

题目测试用例保证 除 '?' 字符 之外，不存在连续重复的字符。

在完成所有转换（可能无需转换）后返回最终的字符串。如果有多个解决方案，请返回其中任何一个。可以证明，在给定的约束条件下，答案总是存在的。



示例 1：
输入：s = "?zs"
输出："azs"
解释：该示例共有 25 种解决方案，从 "azs" 到 "yzs" 都是符合题目要求的。只有 "z" 是无效的修改，因为字符串 "zzs" 中有连续重复的两个 'z' 。

示例 2：
输入：s = "ubv?w"
输出："ubvaw"
解释：该示例共有 24 种解决方案，只有替换成 "v" 和 "w" 不符合题目要求。因为 "ubvvw" 和 "ubvww" 都包含连续重复的字符。

示例 3：
输入：s = "j?qg??b"
输出："jaqgacb"

示例 4：
输入：s = "??yw?ipkj?"
输出："acywaipkja"


提示：

    1 <= s.length <= 100
    s 仅包含小写英文字母和 '?' 字符
*/
class Solution {
    char newChar(int i, int j){
        for(int k = 0; k < 26; k++){
            if(k != i && k != j){
                return (char)(k + 'a');
            }
        }
        return 'a';
    }
    public String modifyString(String s) {
        StringBuffer sb = new StringBuffer(s);
        int n = s.length();
        if(s.charAt(0) == '?'){
            if(n > 1){
                if(s.charAt(1) == '?')
                    sb.setCharAt(0, 'a');
                else
                    sb.setCharAt(0, newChar((int)s.charAt(1) - 97, -1));
            }else{
                sb.setCharAt(0, 'a');
            }
        }
        for(int i = 1; i < n - 1; i++){
            if(sb.charAt(i) == '?'){
                if(sb.charAt(i + 1) == '?'){
                    sb.setCharAt(i, newChar((int)sb.charAt(i - 1) - 97, -1));
                }else{
                    sb.setCharAt(i, newChar((int)sb.charAt(i - 1) - 97, (int)sb.charAt(i + 1) - 97));
                }
            }
        }
        if(sb.charAt(n - 1) == '?'){
            sb.setCharAt(n - 1, newChar((int)sb.charAt(n - 2) - 97, -1));
        }
        return sb.toString();
    }
}
