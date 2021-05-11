/*
1734. 解码异或后的排列

给你一个整数数组 perm ，它是前 n 个正整数的排列，且 n 是个 奇数 。

它被加密成另一个长度为 n - 1 的整数数组 encoded ，满足 encoded[i] = perm[i] XOR perm[i + 1] 。比方说，如果 perm = [1,3,2] ，那么 encoded = [2,1] 。

给你 encoded 数组，请你返回原始数组 perm 。题目保证答案存在且唯一。



示例 1：

输入：encoded = [3,1]
输出：[1,2,3]
解释：如果 perm = [1,2,3] ，那么 encoded = [1 XOR 2,2 XOR 3] = [3,1]

示例 2：

输入：encoded = [6,5,4,6]
输出：[2,4,1,5,3]



提示：

    3 <= n < 105
    n 是奇数。
    encoded.length == n - 1
*/
class Solution {//暴力超时，看了评论才知道怎么求第一个数
    public int[] decode(int[] encoded) {
        // int n = encoded.length + 1;
        // int[] res = new int[n];
        // int cur = 0, f = 0;
        // Set<Integer> s1 = new HashSet<>();
        // Set<Integer> s2 = new HashSet<>();
        // for(int i = 1; i <=n; i++)
        //     s1.add(i);
        // for(int i = 1; i <= n; i++){
        //     res[0] = i;
        //     f = 0;
        //     s2.addAll(s1);
        //     for(int j = 0; j < encoded.length; j++){
        //         cur = res[j] ^ encoded[j];
        //         if(s2.contains(cur)){
        //             res[j + 1] = cur;
        //             s2.remove(cur);
        //         }
        //         else{
        //             f = 1;
        //             break;
        //         }
        //     }
        //     if(f == 0)
        //         break;
        // }
        // return res;

        int n = encoded.length + 1;
        int[] res = new int[n];
        int sum = 0;
        for(int i = 1; i <=n; i++)
            sum ^= i;
        for(int i = n - 2;i >= 0; i-=2)
            sum ^= encoded[i];
        res[0] = sum;
        for(int i = 0; i < n - 1; i++){
            res[i + 1] = res[i] ^ encoded[i];
        }
        return res;
    }
}