/*1711. 大餐计数

大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。

你可以搭配 任意 两道餐品做一顿大餐。

给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第 i 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大餐 的数量。结果需要对 109 + 7 取余。

注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。



示例 1：

输入：deliciousness = [1,3,5,7,9]
输出：4
解释：大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。
它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。

示例 2：

输入：deliciousness = [1,1,1,3,3,3,7]
输出：15
解释：大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。



提示：

    1 <= deliciousness.length <= 105
    0 <= deliciousness[i] <= 220
*/
class Solution {
    public int countPairs(int[] deliciousness) {
        int m = 1000000007;
        int[] sums = new int[22];
        sums[0] = 1;
        for(int i=1; i<=21; i++){
            sums[i] = 2 << (i - 1);
        }
        Map<Integer, Integer> map = new HashMap<>();
        int max = 0;
        for(int i = 0; i < deliciousness.length; i++){
            max = Math.max(deliciousness[i], max);
            map.put(deliciousness[i], map.getOrDefault(deliciousness[i], 0) + 1);
        }
        long res = 0;
        Iterator<Map.Entry<Integer, Integer>> it = map.entrySet().iterator();
        while(it.hasNext()){
            Map.Entry entry= it.next();
            Integer key= (Integer)entry.getKey();
            Long value = Long.valueOf((Integer)entry.getValue());//这里必须用Long，精度问题解决了半小时才搞好
            for(int i = 0; i < 22; i++){
                int x = sums[i];
                if(x - key == key){
                    res += ( (value % m) * ((value - 1) % m) / 2) % m;
                }
                else if(map.containsKey(x - key)){
                    int v = map.get(x - key);
                    res += ((v % m) * (value % m)) % m;
                }
            }
            it.remove();
        }

        return (int)res;
    }
}