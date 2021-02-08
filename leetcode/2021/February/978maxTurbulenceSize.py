# 978. 最长湍流子数组
# 当A 的子数组A[i], A[i + 1], ..., A[j]满足下列条件时，我们称其为湍流子数组：
# 若 i <= k < j，当 k为奇数时， A[k] > A[k + 1]，且当 k为偶数时，A[k] < A[k + 1]；
# 或若i <= k < j，当 k 为偶数时，A[k] > A[k + 1] ，且当 k为奇数时， A[k] < A[k + 1]。
# 也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。返回A的最大湍流子数组的长度。
#
# 示例1：
# 输入：[9, 4, 2, 10, 7, 8, 8, 1, 9]
# 输出：5
# 解释：(A[1] > A[2] < A[3] > A[4] < A[5])
#
# 示例2：
# 输入：[4, 8, 12, 16]
# 输出：2
#
# 示例3：
# 输入：[100]
# 输出：1
#
# 提示：
# 1 <= A.length <= 40000
# 0 <= A[i] <= 10 ^ 9

def maxTurbulenceSize(arr):  # 不知道为什么这是错的，本地跑[9,4,2,10,7,8,8,1,9]就是5，力扣上变成4
    """
    :type arr: List[int]
    :rtype: int
    """
    if len(arr) == 1:
        return len(arr)
    if len(arr) == 2:
        if arr[0] != arr[1]:
            return 2
        return 1
    res = 1
    cur = 1
    f = 0
    if arr[1] > arr[0]:
        f = 1
        cur = 2
        res = 2
    elif arr[1] < arr[0]:
        f = 0
        cur = 2
        res = 2
    for i in range(2, len(arr)):
        if f == 0:  # 期待上升
            if arr[i] > arr[i-1]:
                cur += 1
                res = max(cur, res)
                f = 1
            elif arr[i] == arr[i-1]:
                cur = 1
                continue
            else:
                cur = 2
        else:  # 期待下降
            if arr[i] < arr[i-1]:
                cur += 1
                res = max(cur, res)
                f = 0
            elif arr[i] == arr[i-1]:
                cur = 1
                continue
            else:
                cur = 2
    return res

# class Solution {  JAVA版本就过了
#     public int maxTurbulenceSize(int[] arr) {
#         if (arr.length == 1)
#             return 1;
#         if (arr.length == 2){
#             if (arr[0] == arr[1])
#                 return 1;
#             else
#                 return 2;
#         }
#         int res = 1, cur = 1, f = 0;
#         for(int i = 1; i < arr.length;i++){
#             if (f == 0){
#                 if (arr[i] > arr[i-1]){
#                     cur += 1;
#                     if (cur > res)
#                         res = cur;
#                     f = 1;
#                 }
#                 else if (arr[i] == arr[i-1]){
#                     cur = 1;
#                     continue;
#                 }
#                 else{
#                     cur = 2;
#                 }
#             }
#             else{
#                 if (arr[i] < arr[i-1]){
#                     cur += 1;
#                     if (cur > res)
#                         res = cur;
#                     f = 0;
#                 }
#                 else if (arr[i] == arr[i-1]){
#                     cur = 1;
#                     continue;
#                 }
#                 else{
#                     cur = 2;
#                 }
#             }
#         }
#         return res;
#     }
# }
print(maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
