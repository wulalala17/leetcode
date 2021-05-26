/*1190. 反转每对括号间的子串

给出一个字符串 s（仅含有小写英文字母和括号）。

请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。

注意，您的结果中 不应 包含任何括号。



示例 1：

输入：s = "(abcd)"
输出："dcba"

示例 2：

输入：s = "(u(love)i)"
输出："iloveu"

示例 3：

输入：s = "(ed(et(oc))el)"
输出："leetcode"

示例 4：

输入：s = "a(bcdefghijkl(mno)p)q"
输出："apmnolkjihgfedcbq"



提示：

    0 <= s.length <= 2000
    s 中只有小写英文字母和括号
    我们确保所有括号都是成对出现的
*/
class Solution {//一看就会，一写就废，直接模拟，不用想太多
    void swap(char[] c, int start, int end){
        while(start < end){
            char t = c[start];
            c[start] = c[end];
            c[end] = t;
            start++;
            end--;
        }

    }
    public String reverseParentheses(String s) {
        Stack<Integer> stack = new Stack<>();
        char[] res = s.toCharArray();
        int start = 0, end = 0;
        for(int i = 0; i < res.length; i++){
            if(res[i] == '('){
                stack.push(i);
                continue;
            }
            if(res[i] == ')'){
                swap(res, stack.pop() + 1, i - 1);
            }
        }
        // int n = l.size();
        // for(int i = 0; i < n; i++){
        //     start = l.get(n - i - 1);
        //     end = r.get(i);
        //     swap(res, start + 1, end - 1);
        // }
        StringBuffer sb = new StringBuffer();
        for(int i = 0; i < res.length; i++){
            if (res[i] != ')' && res[i] != '(')
                sb.append(res[i]);
        }
        return sb.toString();
    }
}