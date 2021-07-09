# 面试题 17.10.主要元素
#
# 数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 - 1 。请设计时间复杂度为 O(N) 、空间复杂度为 O(1) 的解决方案。
#
# 示例 1：
# 输入：[1, 2, 5, 9, 5, 9, 5, 5, 5]
# 输出：5
#
# 示例 2：
# 输入：[3, 2]
# 输出：-1
#
# 示例 3：
# 输入：[2, 2, 1, 1, 1, 2, 2]
# 输出：2

class Solution(object):  # 看题解才知道摩尔投票算法，不然只会哈希表
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate, count = -1, 0
        for n in nums:
            if count == 0:
                candidate = n
            if candidate == n:
                count += 1
            else:
                count -= 1
        count = 0
        for n in nums:
            if n == candidate:
                count += 1
        if count * 2 > len(nums):
            return candidate
        else:
            return -1