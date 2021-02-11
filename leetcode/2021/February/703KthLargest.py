# 703. 数据流中的第K大元素
# 设计一个找到数据流中第k大元素的类（class ）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。
# 请实现KthLargest类：
# KthLargest(intk, int[]nums) 使用整数k和整数流nums初始化对象。
# int add(int val) 将val插入数据流nums后，返回当前数据流中第k大的元素。
# 示例：
# 输入：
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# 输出：
# [null, 4, 5, 5, 8, 8]
# 解释：
# KthLargest
# kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3); // return 4
# kthLargest.add(5); // return 5
# kthLargest.add(10); // return 5
# kthLargest.add(9); // return 8
# kthLargest.add(4); // return 8
#
# 提示：
# 1 <= k <= 104
# 0 <= nums.length <= 104
# -104 <= nums[i] <= 104
# -104 <= val <= 104
# 最多调用 add方法104次题目数据保证，在查找第k大元素时，数组中至少有k个元素

class KthLargest(object):  # 讨厌设计题

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = sorted(nums, reverse=True)
        while len(self.nums) > k:
            self.nums.pop()

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.nums.sort(reverse=True)
        if len(self.nums) > self.k:
            self.nums.pop()
        return self.nums[-1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)