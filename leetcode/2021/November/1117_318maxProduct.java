/*
318. 最大单词长度乘积

给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。



示例 1:

输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16
解释: 这两个单词为 "abcw", "xtfn"。

示例 2:

输入: ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4
解释: 这两个单词为 "ab", "cd"。

示例 3:

输入: ["a","aa","aaa","aaaa"]
输出: 0
解释: 不存在这样的两个单词。



提示：

    2 <= words.length <= 1000
    1 <= words[i].length <= 1000
    words[i] 仅包含小写字母
*/
class Solution {//暴力
    boolean check(String s1, String s2){
        for(int i = 0; i < s1.length(); i++){
            if(s2.indexOf(s1.charAt(i)) != -1)
                return false;
        }
        return true;
    }
    public int maxProduct(String[] words) {
        //Arrays.sort(words);
        int res = 0;
        for(int i = 0; i < words.length; i++){
            for(int j = i + 1; j < words.length; j++){
                if(check(words[i], words[j])){
                    res = Math.max(words[i].length() * words[j].length(), res);
                }
            }
        }
        return res;
    }
}