# 896. 单调数列
# 如果数组是单调递增或单调递减的，那么它是单调的。
# 如果对于所有i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i] > = A[j]，那么数组A是单调递减的。
# 当给定的数组A是单调数组时返回true，否则返回false。
# 示例1：
# 输入：[1, 2, 2, 3]
# 输出：true
#
# 示例 2：
# 输入：[6, 5, 4, 4]
# 输出：true
#
# 示例3：
# 输入：[1, 3, 2]
# 输出：false
#
# 示例4：
# 输入：[1, 2, 4, 5]
# 输出：true
#
# 示例5：
# 输入：[1, 1, 1]
# 输出：true
#
# 提示：
# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000

# class Solution { //看了题解才知道一次遍历的机智写法，本来用Py直接排序和原序列对比，相当慢
#     public boolean isMonotonic(int[] A) {
#         boolean inc = true, dec = true;
#         for(int i = 0;i<A.length-1;i++){
#             if (A[i] > A[i+1])
#                 inc = false;
#             if(A[i] < A[i+1])
#                 dec = false;
#         }
#         return inc || dec;
#
#     }
# }