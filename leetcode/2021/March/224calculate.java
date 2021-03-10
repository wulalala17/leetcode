/*224. 基本计算器
实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。

示例 1：
输入：s = "1 + 1"
输出：2

示例 2：
输入：s = " 2-1 + 2 "
输出：3

示例 3：
输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23

提示：

    1 <= s.length <= 3 * 105
    s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
    s 表示一个有效的表达式
*/

class Solution {  //写半天写了个中缀转后缀再计算的，太蠢了，还只能计算个位数，就过了6个例子
    public int calculate(String s) {
        StringBuffer res = new StringBuffer();
        Stack<Character> operatorStack = new Stack<>();
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        map.put('(', 0);
        map.put('+', 1);
        map.put('-', 1);
        map.put(')', 2);
        char[] charArray = s.toCharArray();
        for(char c: charArray){
            if (c==' ')
                continue;
            if(c>=48 && c<=57){
                res.append(c);
            }
            else if (c=='('){
                operatorStack.push(c);
            }
            else if (c==')'){
                while(!operatorStack.empty()){
                    char x = operatorStack.pop();
                    if (x!='('){
                        res.append(x);
                    }
                    else{
                        break;
                    }
                }
            }
            else{
                while(!operatorStack.empty()){
                    char x = operatorStack.peek();
                    if (map.get(x) >= map.get(c)){
                        res.append(operatorStack.pop());
                    }
                    else{
                        break;
                    }
                }
                operatorStack.push(c);
            }
        }
        while(!operatorStack.empty()){
            res.append(operatorStack.pop());
        }
        //System.out.println(res);
        int ans = 0;
        Stack<Integer> numStack = new Stack<>();
        for (int i = 0; i < res.length(); i++) {
            char ch = res.charAt(i);
            if (ch>=48 && ch<=57){
                numStack.push(Integer.parseInt(String.valueOf(ch)));
            } else {
                if (res.charAt(i)=='+'){
                    int r = numStack.pop() + numStack.pop();
                    numStack.push(r);
                }
                else{
                    int r = -(numStack.pop() - numStack.pop());
                    numStack.push(r);
                }
            }
        }
        ans = numStack.pop();
        return ans;
    }
}

class Solution {  // 别人的简洁方法
    public int calculate(String s) {
        Stack<Integer> stack = new Stack<Integer>();
        // sign 代表正负
        int sign = 1, res = 0;
        int length = s.length();
        for (int i = 0; i < length; i++) {
            char ch = s.charAt(i);
            if (Character.isDigit(ch)) {
                int cur = ch - '0';
                while (i + 1 < length && Character.isDigit(s.charAt(i + 1)))
                    cur = cur * 10 + s.charAt(++i) - '0';
                res = res + sign * cur;
            } else if (ch == '+') {
                sign = 1;
            } else if (ch == '-') {
                sign = -1;
            } else if (ch == '(') {
                stack.push(res);
                res = 0;
                stack.push(sign);
                sign = 1;
            } else if (ch == ')') {
                res = stack.pop() * res + stack.pop();
            }
        }
        return res;
    }
}