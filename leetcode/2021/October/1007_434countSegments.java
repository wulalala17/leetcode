/*
434. 字符串中的单词数

统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:

输入: "Hello, my name is John"
输出: 5
解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。
*/
class Solution {//没看懂题，错了好几次
    public int countSegments(String s) {
        if(s.equals("") || s.length() == 0 || s == null)
            return 0;
        int res = 0;
        int f = -1;
        for(int i = 0;i < s.length(); i++){
            if(s.charAt(i) == ' '){
                if(f == 1){//遇到空格
                    f = 0;
                    res++;
                }
                else{
                    f = 0;
                }
            }
            else{
                f = 1;
            }
        }
        if(f == 1)
            res++;
        return res;

    }
}