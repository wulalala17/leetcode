/*
面试题 17.14. 最小K个数

设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

示例：

输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]

提示：

    0 <= len(arr) <= 100000
    0 <= k <= min(100000, len(arr))
*/
class Solution {//应该用快排的
    public int[] smallestK(int[] arr, int k) {
        Arrays.sort(arr);
        int[] res = new int[k];
        for(int i = 0; i < k; i++)
            res[i] = arr[i];
		return res;
    }
}