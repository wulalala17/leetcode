# 995. K连续位的最小翻转次数
# 在仅包含0和1的数组A中，一次 K位翻转包括选择一个长度为K的（连续）子数组，同时将子数组中的每个0更改为1，而每个1更改为 0。
# 返回所需的K位翻转的最小次数，以便数组没有值为0的元素。如果不可能，返回 - 1。
# 示例1：
# 输入：A = [0, 1, 0], K = 1
# 输出：2
# 解释：先翻转 A[0]，然后翻转A[2]。
#
# 示例2：
# 输入：A = [1, 1, 0], K = 2
# 输出：-1
# 解释：无论我们怎样翻转大小为2的子数组，我们都不能使数组变为[1, 1, 1]。
#
# 示例3：
# 输入：A = [0, 0, 0, 1, 0, 1, 1, 0], K = 3
# 输出：3
# 解释：
# 翻转A[0], A[1], A[2]: A变成[1, 1, 1, 1, 0, 1, 1, 0]
# 翻转A[4], A[5], A[6]: A变成[1, 1, 1, 1, 1, 0, 0, 0]
# 翻转A[5], A[6], A[7]: A变成[1, 1, 1, 1, 1, 1, 1, 1]
#
# 提示：
# 1 <= A.length <= 30000
# 1 <= K <= A.length
import collections


class Solution(object):  # 知道暴力通过不了直接看的题解，人家的想法就是牛逼
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        que = collections.deque()
        res = 0
        for i in range(N):
            if que and i >= que[0] + K:
                que.popleft()
            if len(que) % 2 == A[i]:
                if i +  K > N: return -1
                que.append(i)
                res += 1
        return res

# 作者：fuxuemingzhu
# 链接：https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips/solution/hua-dong-chuang-kou-shi-ben-ti-zui-rong-z403l/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。