/*
520. 检测大写字母

我们定义，在以下情况时，单词的大写用法是正确的：

    全部字母都是大写，比如 "USA" 。
    单词中所有字母都不是大写，比如 "leetcode" 。
    如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。

给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。



示例 1：

输入：word = "USA"
输出：true

示例 2：

输入：word = "FlaG"
输出：false



提示：

    1 <= word.length <= 100
    word 由小写和大写英文字母组成
*/
class Solution {
    public boolean detectCapitalUse(String word) {
        int l = word.length();
        if(l == 1)
            return true;
        if(word.charAt(0) >= 'a' && word.charAt(1) <= 'z'){//第一个字母小写，必须全小写
            for(int i = 1; i < l; i++){
                char c = word.charAt(i);
                if(c >= 'A' && c <= 'Z')
                    return false;
            }
            return true;
        }
        else{//第一个字母大写，后面的字母必须跟第二个字母一样
            int code = 0;
            if(word.charAt(1) >= 'A' && word.charAt(1) <= 'Z'){//大写
                code = 1;
            }
            for(int i = 2; i < l; i++){
                char c = word.charAt(i);
                if(code == 0 && c >= 'A' && c <= 'Z')
                    return false;
                if(code == 1 && c >= 'a' && c <= 'z')
                    return false;
            }
            return true;
        }
    }
}