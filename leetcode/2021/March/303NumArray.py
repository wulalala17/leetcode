# 303. 区域和检索 - 数组不可变
# 给定一个整数数组nums，求出数组从索引i到j（i ≤ j）范围内元素的总和，包含i、j两点。
# 实现NumArray类：
# NumArray(int[] nums) 使用数组 nums 初始化对象 int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含
# i、j 两点（也就是 sum(nums[i], nums[i + 1], ..., nums[j])）
#
# 示例：
# 输入：
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# 输出：
# [null, 1, -1, -3]
# 解释：
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return 1((-2) + 0 + 3)
# numArray.sumRange(2, 5); // return -1(3 + (-5) + 2 + (-1))
# numArray.sumRange(0, 5); // return -3((-2) + 0 + 3 + (-5) + 2 + (-1))
#
# 提示：
# 0 <= nums.length <= 104
# -105 <= nums[i] <= 105
# 0 <= i <= j < nums.length
# 最多调用 104 次 sumRange 方法

class NumArray(object):  # 暴力竟然过了

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = nums


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        res = 0
        for k in range(i, j+1):
            res += self.n[k]
        return res




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# class NumArray {  //评论里的写法
#     private int[] sums;
#
#     public NumArray(int[] nums) {
#         sums = new int[nums.length+1];
#         if (nums.length == 0) {
#             return;
#         }
#     sums[0] = nums[0];
#     for (int i = 1;i <= nums.length;i++)
#         sums[i] += sums[i - 1] + nums[i - 1];
# }
#
#     public int sumRange(int i, int j) {
#         return sums[j + 1] - sums[i];
#     }
# }