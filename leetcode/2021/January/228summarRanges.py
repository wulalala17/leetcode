# 228.汇总区间
# 给定一个无重复元素的有序整数数组nums 。
# 返回恰好覆盖数组中所有数字的最小有序 区间范围列表。也就是说，nums的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于nums的数字x 。
# 列表中的每个区间范围[a, b]应该按如下格式输出："a->b" ，如果a != b "a" ，如果a == b
#
# 示例1：
# 输入：nums = [0, 1, 2, 4, 5, 7]
# 输出：["0->2", "4->5", "7"]
# 解释：区间范围是：[0, 2] --> "0->2" [4, 5] --> "4->5" [7, 7] --> "7"
#
# 示例2：
# 输入：nums = [0, 2, 3, 4, 6, 8, 9]
# 输出：["0", "2->4", "6", "8->9"]
# 解释：区间范围是：[0, 0] --> "0" [2, 4] --> "2->4" [6, 6] --> "6" [8, 9] --> "8->9"
#
# 示例3：
# 输入：nums = []
# 输出：[]
#
# 示例4：
# 输入：nums = [-1]
# 输出：["-1"]
#
# 示例5：
# 输入：nums = [0]
# 输出：["0"]
#
# 提示：
# 0 <= nums.length <= 20
# -231 <= nums[i] <= 231 - 1
# nums中的所有值都 互不相同nums按升序排列

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        res = []
        start, end = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    res.append(str(end))
                else:
                    s = str(start) + "->" + str(end)
                    res.append(s)
                start = nums[i]
                end = nums[i]
        if start == end:
            res.append(str(end))
        else:
            s = str(start) + "->" + str(end)
            res.append(s)
        return res