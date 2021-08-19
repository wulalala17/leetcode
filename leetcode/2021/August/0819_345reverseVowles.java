/*
345. 反转字符串中的元音字母

编写一个函数，以字符串作为输入，反转该字符串中的元音字母。



示例 1：

输入："hello"
输出："holle"

示例 2：

输入："leetcode"
输出："leotcede"



提示：

    元音字母不包含字母 "y" 。
*/
class Solution {
    public String reverseVowels(String s) {
        StringBuffer res = new StringBuffer(s);
        Set<Character> set = new HashSet<>();
        set.add('a');
        set.add('e');
        set.add('i');
        set.add('o');
        set.add('u');
        set.add('A');
        set.add('E');
        set.add('I');
        set.add('O');
        set.add('U');
        int i = 0, j = s.length() - 1;
        int f1 = 0, f2 = 0;
        while(i < j){
            if(f1 == 1 && f2 == 1){
                res.setCharAt(i, s.charAt(j));
                res.setCharAt(j, s.charAt(i));
                f1 = 0;
                f2 = 0;
                i++;
                j--;
                continue;
            }
            if(f1 == 0){
                if(set.contains(s.charAt(i)))
                    f1 = 1;
                else
                    i++;
            }
            if(f2 == 0){
                if(set.contains(s.charAt(j)))
                    f2 = 1;
                else
                    j--;
            }
        }
        return res.toString();
    }
}