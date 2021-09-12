/*
678. 有效的括号字符串

给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

    任何左括号 ( 必须有相应的右括号 )。
    任何右括号 ) 必须有相应的左括号 ( 。
    左括号 ( 必须在对应的右括号之前 )。
    * 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
    一个空字符串也被视为有效字符串。

示例 1:

输入: "()"
输出: True

示例 2:

输入: "(*)"
输出: True

示例 3:

输入: "(*))"
输出: True

注意:

    字符串大小将在 [1，100] 范围内。
*/
class Solution {//当我还在为贪心遍历两遍击败100%而沾沾自喜的时候人家用范围法遍历一遍就行了
    public boolean checkValidString(String s) {
        int l = 0, r = 0, star = 0;
        char c = '-';
        for(int i = 0; i < s.length(); i++){
            c = s.charAt(i);
            if(c == '('){
                l++;
            }
            else if(c == ')'){
                if(l > 0){
                    l--;
                }
                else{
                    if(star > 0)
                        star--;
                    else
                        return false;
                }
            }
            else{
                star++;
            }
        }
        star = 0;
        for(int i = s.length() - 1; i >= 0; i--){
            c = s.charAt(i);
            if(c == ')'){
                r++;
            }
            else if(c == '('){
                if(r > 0){
                    r--;
                }
                else{
                    if(star > 0)
                        star--;
                    else
                        return false;
                }
            }
            else{
                star++;
            }
        }
        return true;
    }
}

/*class Solution {//记录左括号未匹配的范围 tql
public:
    bool checkValidString(string s) {
        int lo = 0; int hi = 0;
        for(auto it : s) {
            if(it == '(') {
                lo++;
                hi++;
            } else if(it == ')') {
                lo = max(0, lo - 1);
                hi--;
                if(hi < 0) return false;
            } else {
                lo = max(lo - 1, 0);
                hi++;
            };
        }
        return lo <= 0;
    }
};*/