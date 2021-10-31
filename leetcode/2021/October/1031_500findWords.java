/*
500. 键盘行

给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

美式键盘 中：

    第一行由字符 "qwertyuiop" 组成。
    第二行由字符 "asdfghjkl" 组成。
    第三行由字符 "zxcvbnm" 组成。

American keyboard



示例 1：

输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]

示例 2：

输入：words = ["omk"]
输出：[]

示例 3：

输入：words = ["adsdf","sfd"]
输出：["adsdf","sfd"]



提示：

    1 <= words.length <= 20
    1 <= words[i].length <= 100
    words[i] 由英文字母（小写和大写字母）组成
*/
class Solution {//遍历
    String find(char a, String[] words){
        for(String word: words){
            if(word.indexOf(a) != -1)
                return word;
        }
        return "";
    }
    public String[] findWords(String[] words) {
        String[] keyboard = new String[]{"qwertyuiop", "asdfghjkl", "zxcvbnm"};
        String cur = "";
        int flag = 0;
        List<String> res = new ArrayList<>();
        for(int i = 0; i < words.length; i++){
            String s = words[i].toLowerCase();
            cur = find(s.charAt(0), keyboard);
            flag = 0;
            for(int j = 1; j < s.length(); j++){
                char c = s.charAt(j);
                if(cur.indexOf(c) == -1){
                    flag = 1;
                    break;
                }
            }
            if(flag == 0)
                res.add(words[i]);
        }
        String[] ans = res.toArray(new String[0]);
        return ans;


    }
}