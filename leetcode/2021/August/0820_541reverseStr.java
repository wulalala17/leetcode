/*
541. 反转字符串 II

给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。

    如果剩余字符少于 k 个，则将剩余字符全部反转。
    如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。



示例 1：

输入：s = "abcdefg", k = 2
输出："bacdfeg"

示例 2：

输入：s = "abcd", k = 2
输出："bacd"



提示：

    1 <= s.length <= 104
    s 仅由小写英文组成
    1 <= k <= 104
*/
class Solution {//参数里直接新建对象，总觉得写得很难看
    public String reverseStr(String s, int k) {
        int n = s.length(), cur = 0;
        StringBuffer res = new StringBuffer();
        while(cur < n){
            if(n - cur >= 2 * k){
                res.append(new StringBuffer(s.substring(cur, cur + k)).reverse());
                res.append(s.substring(cur + k, cur + 2 * k));
                cur += 2 * k;
                continue;
            }
            else if(n - cur >= k){
                res.append(new StringBuffer(s.substring(cur, cur + k)).reverse());
                res.append(s.substring(cur + k, n));
                break;
            }
            else{
                res.append(new StringBuffer(s.substring(cur, n)).reverse());
                break;
            }
        }
        return res.toString();
    }
}