/*
1588. 所有奇数长度子数组的和

给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。

子数组 定义为原数组中的一个连续子序列。

请你返回 arr 中 所有奇数长度子数组的和 。



示例 1：

输入：arr = [1,4,2,5,3]
输出：58
解释：所有奇数长度子数组和它们的和为：
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

示例 2：

输入：arr = [1,2]
输出：3
解释：总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。

示例 3：

输入：arr = [10,11,12]
输出：66



提示：

    1 <= arr.length <= 100
    1 <= arr[i] <= 1000
*/
class Solution {//简单题On方法没想出来，还不如一年前的我用暴力
    public int sumOddLengthSubarrays(int[] arr) {
        int n = arr.length;
        int res = 0;
        for(int i = 0; i < n; i++){
            int left = i + 1, right = n - i;
            //对左侧而言，选择偶数长度的子数组情况为left/2
            //奇数为(left + 1)/2，右侧亦然
            int leftOdd = (left + 1) / 2, leftEven = left / 2;
            int rightOdd = (right + 1) / 2, rightEven = right / 2;

            //对每个元素出现在奇数个子数组的次数累加即可
            res += (leftOdd * rightOdd + leftEven * rightEven) * arr[i];
        }
        return res;

    }
}