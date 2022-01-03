/*
1185. 一周中的第几天

给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。

输入为三个整数：day、month 和 year，分别表示日、月、年。

您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。



示例 1：

输入：day = 31, month = 8, year = 2019
输出："Saturday"

示例 2：

输入：day = 18, month = 7, year = 1999
输出："Sunday"

示例 3：

输入：day = 15, month = 8, year = 1993
输出："Sunday"



提示：

    给出的日期一定是在 1971 到 2100 年之间的有效日期。
*/
class Solution {
    int countDayOfYear(int year){
        if(year % 100 != 0 && year % 4 == 0 || year % 400 == 0)
            return 366;
        return 365;
    }
    public String dayOfTheWeek(int day, int month, int year) {
        String[] weekDay = new String[]{"Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"};
        int[] m = new int[]{31,28,31,30,31,30,31,31,30,31,30,31};
        int res = 0;
        for(int i = 1971; i < year; i++){
            res += countDayOfYear(i);
        }
        for(int i = 0; i < month - 1; i++){
            res += m[i];
        }
        res += day;
        if(countDayOfYear(year) == 366 && month > 2)
            res += 1;
        return weekDay[res % 7];
    }
}