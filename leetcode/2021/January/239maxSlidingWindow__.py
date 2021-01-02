# 239.滑动窗口最大值
# 给你一个整数数组nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的k个数字。滑动窗口每次只向右移动一位。返回滑动窗口中的最大值。
# 示例1：
# 输入：nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
# 输出：[3, 3, 5, 5, 6, 7]

# 示例2：
# 输入：nums = [1], k = 1
# 输出：[1]
#
# 示例3：
# 输入：nums = [1, -1], k = 1
# 输出：[1, -1]
#
# 示例4：
# 输入：nums = [9, 11], k = 2
# 输出：[11]
#
# 示例5：
# 输入：nums = [4, -2], k = 2
# 输出：[4]
# 提示：
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length
import collections


class Solution:  # 不会做，官方题解的做法
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans


# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / sliding - window - maximum / solution / hua - dong - chuang - kou - zui - da - zhi - by - leetco - ki6m /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。