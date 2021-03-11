/*227. 基本计算器 II
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
整数除法仅保留整数部分。

示例 1：
输入：s = "3+2*2"
输出：7

示例 2：
输入：s = " 3/2 "
输出：1

示例 3：
输入：s = " 3+5 / 2 "
输出：5

提示：

    1 <= s.length <= 3 * 105
    s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
    s 表示一个 有效表达式
    表达式中的所有整数都是非负整数，且在范围 [0, 231 - 1] 内
    题目数据保证答案是一个 32-bit 整数
*/

class Solution {  // 一顿操作猛如虎，一看击败13% 高手还是用昨天的思路，不用转成后缀表达式
    public int calculate(String s) {
        List<String> list = new ArrayList<String>();
        Stack<Character> operatorStack = new Stack<>();
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        map.put('(', 0);
        map.put('+', 1);
        map.put('-', 1);
        map.put('*', 2);
        map.put('/', 2);
        map.put(')', 3);
        char[] charArray = s.toCharArray();
        for(int i = 0;i<charArray.length;i++){
            char c = charArray[i];
            if (c==' ')
                continue;
            if(c>=48 && c<=57){//是数字
                int cur = c - '0';
                while(i+1<charArray.length&&Character.isDigit(charArray[i+1]))
                    cur = cur * 10 + charArray[++i] - '0';
                list.add(String.valueOf(cur));
            }
            // else if (c=='('){
            //     operatorStack.push(c);
            // }
            // else if (c==')'){
            //     while(!operatorStack.empty()){
            //         char x = operatorStack.pop();
            //         if (x!='('){
            //             res.append(x);
            //         }
            //         else{
            //             break;
            //         }
            //     }
            // }
            else{
                while(!operatorStack.empty()){
                    char x = operatorStack.peek();
                    if (map.get(x) >= map.get(c)){
                        list.add(String.valueOf(operatorStack.pop()));
                    }
                    else{
                        break;
                    }
                }
                operatorStack.push(c);
            }
        }
        while(!operatorStack.empty()){
            list.add(String.valueOf(operatorStack.pop()));
        }
        System.out.println(list);
        int ans = 0;
        Stack<Integer> numStack = new Stack<>();
        for (int i = 0; i < list.size(); i++) {
            String s1 = list.get(i);
            if (Character.isDigit(s1.charAt(0))){
                numStack.push(Integer.parseInt(s1));
            } else {
                if (s1.charAt(0)=='+'){
                    int r = numStack.pop() + numStack.pop();
                    numStack.push(r);
                }
                else if (s1.charAt(0)=='-'){
                    int r = -(numStack.pop() - numStack.pop());
                    numStack.push(r);
                }
                else if (s1.charAt(0)=='*'){
                    int r = numStack.pop() * numStack.pop();
                    numStack.push(r);
                }
                else{
                    int a = numStack.pop();
                    int b = numStack.pop();
                    int r = b / a;
                    numStack.push(r);
                }
            }
        }
        ans = numStack.pop();
        return ans;
    }
}

class Solution {//官方题解
    public int calculate(String s) {
        Deque<Integer> stack = new LinkedList<Integer>();
        char preSign = '+';
        int num = 0;
        int n = s.length();
        for (int i = 0; i < n; ++i) {
            if (Character.isDigit(s.charAt(i))) {
                num = num * 10 + s.charAt(i) - '0';
            }
            if (!Character.isDigit(s.charAt(i)) && s.charAt(i) != ' ' || i == n - 1) {
                switch (preSign) {
                    case '+':
                        stack.push(num);
                        break;
                    case '-':
                        stack.push(-num);
                        break;
                    case '*':
                        stack.push(stack.pop() * num);
                        break;
                    default:
                        stack.push(stack.pop() / num);
                }
                preSign = s.charAt(i);
                num = 0;
            }
        }
        int ans = 0;
        while (!stack.isEmpty()) {
            ans += stack.pop();
        }
        return ans;
    }
}

/*作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/basic-calculator-ii/solution/ji-ben-ji-suan-qi-ii-by-leetcode-solutio-cm28/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。*/