/*剑指 Offer 38. 字符串的排列

输入一个字符串，打印出该字符串中字符的所有排列。



你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。



示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]



限制：

1 <= s 的长度 <= 8
*/
class Solution {//回溯，面试题同学写过
    HashSet<String> set = new HashSet<>();
    void swap(char[] c, int i, int j){
        char t = c[i];
        c[i] = c[j];
        c[j] = t;
    }
    void dfs(char[] c, int start){
        if(start == c.length - 1)
            set.add(String.valueOf(c));
        else{
            for(int i = 0; i < c.length; i++){
                swap(c, i, start);
                dfs(c, start + 1);
                swap(c, start, i);
            }
        }
    }
    public String[] permutation(String s) {
        dfs(s.toCharArray(), 0);
        String[] ans = new String[set.size()];
        set.toArray(ans);
        return ans;
    }
}