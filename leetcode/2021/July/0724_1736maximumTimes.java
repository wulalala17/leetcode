/*1736. 替换隐藏数字得到的最晚时间

给你一个字符串 time ，格式为 hh:mm（小时：分钟），其中某几位数字被隐藏（用 ? 表示）。

有效的时间为 00:00 到 23:59 之间的所有时间，包括 00:00 和 23:59 。

替换 time 中隐藏的数字，返回你可以得到的最晚有效时间。



示例 1：

输入：time = "2?:?0"
输出："23:50"
解释：以数字 '2' 开头的最晚一小时是 23 ，以 '0' 结尾的最晚一分钟是 50 。

示例 2：

输入：time = "0?:3?"
输出："09:39"

示例 3：

输入：time = "1?:22"
输出："19:22"



提示：

    time 的格式为 hh:mm
    题目数据保证你可以由输入的字符串生成有效的时间
*/
class Solution {
    public String maximumTime(String time) {
        StringBuffer res = new StringBuffer();
        char a = time.charAt(0);
        char b = time.charAt(1);
        if(a == '?'){
            if(b == '?'){
                res.append("23");
            }
            else{
                if(b - '0' > 3){
                    res.append("1");
                }
                else{
                    res.append("2");
                }
                res.append(String.valueOf(b));
            }
        }
        else{//a不为问号
            res.append(String.valueOf(a));
            if(b == '?'){
                if(a == '2'){
                    res.append("3");
                }
                else{
                    res.append("9");
                }
            }
            else{
                res.append(String.valueOf(b));
            }
        }
        res.append(":");

        char c = time.charAt(3);
        char d = time.charAt(4);
        if(c == '?'){
            res.append("5");
        }
        else{
            res.append(String.valueOf(c));
        }
        if(d == '?'){
            res.append("9");
        }
        else{
            res.append(String.valueOf(d));
        }
        return res.toString();

    }
}