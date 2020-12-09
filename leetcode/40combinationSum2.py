# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明：
#
#     所有数字（包括目标数）都是正整数。
#     解集不能包含重复的组合。
#
# 示例 1:
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#
# 示例 2:
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
def combinationSum2(candidates, target):
    used = []
    res = []
    cur_res = []
    for x in candidates:
        used.append(0)
    sorted_candidates = sorted(candidates)

    def baceTrace(l, target, sum, startIndex, used):
        if sum > target:
            return
        if sum == target:
            res.append(cur_res[:])
            return
        for i in range(startIndex, len(l)):
            if i > 0 and l[i] == l[i-1] and used[i-1] == 0:
                continue
            sum += l[i]
            cur_res.append(l[i])
            used[i] = 1
            baceTrace(l, target, sum, i+1, used)
            used[i] = 0
            sum -= l[i]
            cur_res.pop()
    baceTrace(sorted_candidates, target, 0, 0, used)
    print(res)
    # return res

combinationSum2([10,1,2,7,6,1,5], 8)
