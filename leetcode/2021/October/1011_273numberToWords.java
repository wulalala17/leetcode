/*
273. 整数转换英文表示

将非负整数 num 转换为其对应的英文表示。



示例 1：

输入：num = 123
输出："One Hundred Twenty Three"

示例 2：

输入：num = 12345
输出："Twelve Thousand Three Hundred Forty Five"

示例 3：

输入：num = 1234567
输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

示例 4：

输入：num = 1234567891
输出："One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"



提示：

    0 <= num <= 231 - 1
*/
class Solution {//嗯模拟
    String toEnglish(int n){
        String[] s = new String[]{"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
        String[] s1 = new String[]{"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
        String[] s2 = new String[]{"Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
        if(n < 10){// 1-9
            return s[n - 1];
        }
        if(n < 20){//10-19
            return s1[n - 10];
        }
        if(n < 100){//20-99
            if(n % 10 == 0)//正十数
                return s2[n / 10 - 2];
            else{
                return s2[n / 10 - 2] + " " + s[n % 10 - 1];
            }
        }
        else{//100-999
            if(n % 100 == 0)
                return s[n / 100 - 1] + " Hundred";
            else{
                return s[n / 100 - 1] + " Hundred " + toEnglish(n % 100);
            }
        }
    }
    public String numberToWords(int num) {
        if(num == 0)
            return "Zero";
        StringBuffer ans = new StringBuffer();
        int part1 = num % 1000;
        num = num / 1000;
        int part2 = num % 1000;
        num = num / 1000;
        int part3 = num % 1000;
        num = num / 1000;
        int part4 = num;
        if(part4 != 0){
            ans.append(toEnglish(part4) + " Billion ");
        }
        if(part3 != 0){
            ans.append(toEnglish(part3) + " Million ");
        }
        if(part2!=0){
            ans.append(toEnglish(part2) + " Thousand ");
        }
        if(part1!=0){
            ans.append(toEnglish(part1));
        }
        return ans.toString().trim();
    }
}