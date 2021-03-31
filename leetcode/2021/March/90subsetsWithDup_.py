# 90. 子集 II
# 给你一个整数数组nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
# 解集不能 包含重复的子集。返回的解集中，子集可以按任意顺序排列。
#
# 示例1：
# 输入：nums = [1, 2, 2]
# 输出：[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
#
# 示例2：
# 输入：nums = [0]
# 输出：[[], [0]]

# 提示：
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10


def subsetsWithDup(nums):  # 暴力DFS 不知道怎么剪枝
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) == 0:
        return [[]]
    if len(nums) == 1:
        return [[], nums]
    res = [[]]

    def isinres(r, res):
        for re in res:
            if len(re) == len(r):
                if r == re:
                    return False
                if sorted(re) == sorted(r):
                    return False
        return True

    def dfs(x, index, r):
        if len(r) == x:
            if r not in res and isinres(r, res):
                res.append(r[:])
            return
        if index == len(nums):
            return
        for idx in range(index, len(nums)):
            r.append(nums[idx])
            dfs(x, idx + 1, r)
            r.pop()

    for i in range(1, len(nums)):
        r = []
        for j in range(len(nums)):
            r.append(nums[j])
            dfs(i, j + 1, r)
            r.pop()
    res.append(nums)
    return res

print(subsetsWithDup([4,4,4,1,4]))
print(subsetsWithDup([1,2,2]))



# class Solution {  // 官方题解
#     List<Integer> t = new ArrayList<Integer>();
#     List<List<Integer>> ans = new ArrayList<List<Integer>>();
#
#     public List<List<Integer>> subsetsWithDup(int[] nums) {
#         Arrays.sort(nums);
#         dfs(false, 0, nums);
#         return ans;
#     }
#
#     public void dfs(boolean choosePre, int cur, int[] nums) {
#         if (cur == nums.length) {
#             ans.add(new ArrayList<Integer>(t));
#             return;
#         }
#         dfs(false, cur + 1, nums);
#         if (!choosePre && cur > 0 && nums[cur - 1] == nums[cur]) {
#             return;
#         }
#         t.add(nums[cur]);
#         dfs(true, cur + 1, nums);
#         t.remove(t.size() - 1);
#     }
# }
#
# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/subsets-ii/solution/zi-ji-ii-by-leetcode-solution-7inq/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。