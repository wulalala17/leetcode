/*
554. 砖墙

你的面前有一堵矩形的、由 n 行砖块组成的砖墙。这些砖块高度相同（也就是一个单位高）但是宽度不同。每一行砖块的宽度之和应该相等。

你现在要画一条 自顶向下 的、穿过 最少 砖块的垂线。如果你画的线只是从砖块的边缘经过，就不算穿过这块砖。你不能沿着墙的两个垂直边缘之一画线，这样显然是没有穿过一块砖的。

给你一个二维数组 wall ，该数组包含这堵墙的相关信息。其中，wall[i] 是一个代表从左至右每块砖的宽度的数组。你需要找出怎样画才能使这条线 穿过的砖块数量最少 ，并且返回 穿过的砖块数量 。



示例 1：

输入：wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
输出：2

示例 2：

输入：wall = [[1],[1],[1]]
输出：3



提示：

    n == wall.length
    1 <= n <= 104
    1 <= wall[i].length <= 104
    1 <= sum(wall[i].length) <= 2 * 104
    对于每一行 i ，sum(wall[i]) 应当是相同的
    1 <= wall[i][j] <= 231 - 1

*/
class Solution { //暴力是不行的，哈希表才行
    int[] res;
    void setRes(int idx, int x){
        for(int i = idx; i < idx + x; i++){
            if(res[i] == -1)
                res[i] = 1;
            else
                res[i]++;
        }
    }
    public int leastBricks(List<List<Integer>> wall) {
        /*int sum = 0;
        int step = 0, idx = 0;
        List<Integer> w = wall.get(0);
        for(int i = 0; i < w.size(); i++){
            sum += w.get(i);
        }
        sum = 1 + (sum - 1) * 2;
        res = new int[sum];
        for(int i = 0; i < sum; i++){
            res[i] = -1;
        }
        HashMap<Integer, Integer> map = new HashMap();
        List<Integer> w = wall.get(0);
        for(int i = 0; i < wall.size(); i++){
            w = wall.get(i);
            idx = 0;
            for(int j = 0; j < w.size(); j++){
                step = w.get(j);
                setRes(idx, step);
                idx += (step + 1);
            }
        }
        int min = 10000;
        for(int i = 0; i < sum; i++){
            if(res[i] != -1 && res[i] < min)
                min = res[i];
        }
        return min;*/

        int step = 0, idx = 0, n = wall.size(), v = n;
        int min = 0;
        HashMap<Integer, Integer> map = new HashMap();
        List<Integer> w = wall.get(0);
        for(int i = 0; i < wall.size(); i++){
            w = wall.get(i);
            idx = 0;
            for(int j = 0; j < w.size() - 1; j++){
                step = w.get(j);
                idx += step;
                v = map.getOrDefault(idx, 0);
                map.put(idx, ++v);
            }
        }
        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            if(entry.getValue() > min){
                min = entry.getValue();
            }
        }
        return n - min;
    }
}