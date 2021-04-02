面试题 17.21. 直方图的水量

给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。 感谢 Marcos 贡献此图。

示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

class Solution(object):  # 看了评论才写出来，明明做过了，却忘记了
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right = [0 for _ in range(len(height))]
        left = [0 for _ in range(len(height))]
        ma = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] > ma:
                ma = height[i]
            right[i] = ma
        ma = 0
        for i in range(len(height)):
            if height[i] > ma:
                ma = height[i]
            left[i] = ma
        res = 0
        for i in range(len(height)):
            if min(left[i], right[i]) - height[i] > 0:
                res += (min(left[i], right[i]) - height[i])
        return res

class Solution { //官方题解双指针
    public int trap(int[] height) {
        int ans = 0;
        int left = 0, right = height.length - 1;
        int leftMax = 0, rightMax = 0;
        while (left < right) {
            leftMax = Math.max(leftMax, height[left]);
            rightMax = Math.max(rightMax, height[right]);
            if (height[left] < height[right]) {
                ans += leftMax - height[left];
                ++left;
            } else {
                ans += rightMax - height[right];
                --right;
            }
        }
        return ans;
    }
}

/*作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/volume-of-histogram-lcci/solution/zhi-fang-tu-de-shui-liang-by-leetcode-so-7rla/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。*/