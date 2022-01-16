/*
1220. 统计元音字母序列的数目

给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：

    字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
    每个元音 'a' 后面都只能跟着 'e'
    每个元音 'e' 后面只能跟着 'a' 或者是 'i'
    每个元音 'i' 后面 不能 再跟着另一个 'i'
    每个元音 'o' 后面只能跟着 'i' 或者是 'u'
    每个元音 'u' 后面只能跟着 'a'

由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。



示例 1：

输入：n = 1
输出：5
解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。

示例 2：

输入：n = 2
输出：10
解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。

示例 3：

输入：n = 5
输出：68



提示：

    1 <= n <= 2 * 10^4
*/
class Solution {
    public int countVowelPermutation(int n) {
        long m = 1000000007;
        long[] a = new long[n + 1];
        long[] e = new long[n + 1];
        long[] i = new long[n + 1];
        long[] o = new long[n + 1];
        long[] u = new long[n + 1];
        a[1] = 1;
        e[1] = 1;
        i[1] = 1;
        o[1] = 1;
        u[1] = 1;
        for(int j = 2; j <= n; j++){
            a[j] = (e[j - 1] % m + i[j - 1] % m + u[j - 1] % m) % m;
            e[j] = (a[j - 1] % m + i[j - 1] % m) % m;
            i[j] = (e[j - 1] % m + o[j - 1] % m) % m;
            o[j] = i[j - 1] % m;
            u[j] = (i[j - 1] % m + o[j - 1] % m) % m;
        }
        long res = (a[n] + e[n]) % m;
        res = (res + i[n]) % m;
        res = (res + o[n]) % m;
        res = (res + u[n]) % m;
        return (int)res;



    }
}
//a -> e
//e -> ai
//i -> aeou
//o -> iu
//u -> a