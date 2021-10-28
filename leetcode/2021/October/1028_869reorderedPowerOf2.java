/*
869. 重新排序得到 2 的幂

给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。

示例 1：
输入：1
输出：true

示例 2：
输入：10
输出：false

示例 3：
输入：16
输出：true

示例 4：
输入：24
输出：false

示例 5：
输入：46
输出：true

提示：

    1 <= N <= 10^9
*/
class Solution {
    public boolean reorderedPowerOf2(int n) {
        if(n == 1)
            return true;
        Set<List<Integer>> set = new HashSet<>();
        for(int i = 0; i <= 31; i++){
            int cur = 2 << i;
            List<Integer> list = new ArrayList<>();
            while(cur > 0){
                list.add(cur % 10);
                cur /= 10;
            }
            Collections.sort(list);
            set.add(list);
        }
        List<Integer> l = new ArrayList<>();
        while(n > 0){
            l.add(n % 10);
            n /= 10;
        }
        Collections.sort(l);
        return set.contains(l);
    }
}