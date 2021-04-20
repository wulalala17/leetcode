/*
28. 实现 strStr()

实现 strStr() 函数。
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

说明：
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。



示例 1：
输入：haystack = "hello", needle = "ll"
输出：2

示例 2：
输入：haystack = "aaaaa", needle = "bba"
输出：-1

示例 3：
输入：haystack = "", needle = ""
输出：0


提示：

    0 <= haystack.length, needle.length <= 5 * 104
    haystack 和 needle 仅由小写英文字符组成
*/
class Solution { // 暴力超时了，只能改成这样 库函数0ms
    public int strStr(String haystack, String needle) {
        //return haystack.indexOf(needle);
        if (needle == null || needle.length() == 0)
            return 0;
        int m = haystack.length(), n = needle.length();
        if(n > m)
            return -1;
        int i = 0, j = 0, idx = -1;
        List<Integer> l = new ArrayList<>();
        for(int k = 0;k < m;k++){
            if (haystack.charAt(k) == needle.charAt(0))
                l.add(k);
        }
        for(int k = 0;k < l.size(); k++){
            i = l.get(k);
            while(i < m && j < n && haystack.charAt(i) == needle.charAt(j)){
                if(idx == -1)
                    idx = i;
                i++;
                j++;
            }
            if(j == n)
                return idx;
            else{
                j = 0;
                idx = -1;
            }
        }
        return idx;
    }
}