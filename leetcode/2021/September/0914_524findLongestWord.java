/*
524. 通过删除字母匹配到字典里最长单词

给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。

如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。



示例 1：

输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
输出："apple"

示例 2：

输入：s = "abpcplea", dictionary = ["a","b","c"]
输出："a"



提示：

    1 <= s.length <= 1000
    1 <= dictionary.length <= 1000
    1 <= dictionary[i].length <= 1000
    s 和 dictionary[i] 仅由小写英文字母组成
*/
class Solution {//双指针加排序，重写排序好蠢，才知道有Comparator.naturalOrder()这东西
    public boolean isSubstring(String s1, String s2){
        int i = 0, j = 0;
        char c1, c2;
        int res = 0;
        while(i < s1.length() && j < s2.length()){
            c1 = s1.charAt(i);
            c2 = s2.charAt(j);
            if(c1 == c2){
                i++;
                j++;
                res++;
            }
            else{
                i++;
            }
        }
        return res == s2.length();
    }
    public String findLongestWord(String s, List<String> dictionary) {
        Collections.sort(dictionary, new Comparator<String>() {
			public int compare(String s1, String s2) {
				if (s1.length() != s2.length()) {
					return s1.length() < s2.length()?-1:1;
				}
				else
                    return s1.compareTo(s2);
			}
		});
        String res = "";
        int resLength = 0, curLength = 1;
        for(int i = dictionary.size() - 1; i >= 0; i--){
            String cur = dictionary.get(i);
            if(isSubstring(s, cur)){
                curLength = cur.length();
                if(resLength == 0){
                    resLength = curLength;
                    res = cur;
                }
                else{
                    if(curLength < resLength)
                        break;
                    res = cur;
                }
            }
        }
        return res;
    }
}