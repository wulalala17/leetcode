/*
319. 灯泡开关

初始时有 n 个灯泡处于关闭状态。第一轮，你将会打开所有灯泡。接下来的第二轮，你将会每两个灯泡关闭一个。

第三轮，你每三个灯泡就切换一个灯泡的开关（即，打开变关闭，关闭变打开）。第 i 轮，你每 i 个灯泡就切换一个灯泡的开关。直到第 n 轮，你只需要切换最后一个灯泡的开关。

找出并返回 n 轮后有多少个亮着的灯泡。



示例 1：

输入：n = 3
输出：1
解释：
初始时, 灯泡状态 [关闭, 关闭, 关闭].
第一轮后, 灯泡状态 [开启, 开启, 开启].
第二轮后, 灯泡状态 [开启, 关闭, 开启].
第三轮后, 灯泡状态 [开启, 关闭, 关闭].

你应该返回 1，因为只有一个灯泡还亮着。

示例 2：

输入：n = 0
输出：0

示例 3：

输入：n = 1
输出：1



提示：

    0 <= n <= 109
*/
class Solution {//从算因子数目超时，想到找规律，On解决，结果看评论才发现还能进一步优化
    int factor(int n){
        if(n == 1)
            return 1;
        int res = 1, cur = 0;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            cur = 0;
            if (n % i == 0) {
                cur++;
                while (n % i == 0) {
                    n /= i;
                    cur++;
                }
                res *= cur;
            }
        }
        if (n != 1)
            res *= 2;
        return res;
    }
    public int bulbSwitch(int n) {
        /*int f = 0, res = 0;
        for(int i = 1; i <= n; i++){
            f = factor(i);
            if(f % 2 != 0)
                res++;
        }
        return res;*/
        if(n == 0)
            return 0;
        for(int i = 1; i < n; i++){
            if(n <= i * i + 2 * i)
                return i;
        }
        return 1;
    }
}