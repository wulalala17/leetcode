/*
438. 找到字符串中所有字母异位词

给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。



示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。



提示:

    1 <= s.length, p.length <= 3 * 104
    s 和 p 仅包含小写字母
*/
class Solution {//学了Arrays.equals这个方法
    public List<Integer> findAnagrams(String s, String p) {
        int lens = s.length(), lenp = p.length();
        List<Integer> res = new ArrayList<>();
        if(lens < lenp)
            return res;
        int[] fres = new int[26];
        int[] frep = new int[26];
        for(int i = 0; i < lenp; i++){
            frep[p.charAt(i) - 'a']++;
            fres[s.charAt(i) - 'a']++;
        }
        for(int i = lenp; i < lens; i++){
            if(Arrays.equals(frep, fres)){
                res.add(i - lenp);
            }
            fres[s.charAt(i - lenp) - 'a']--;
            fres[s.charAt(i) - 'a']++;
        }
        if(Arrays.equals(frep, fres)){
            res.add(lens - lenp);
        }
        return res;

    }
}