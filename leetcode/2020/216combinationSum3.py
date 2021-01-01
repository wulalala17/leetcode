# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
#     所有数字都是正整数。
#     解集不能包含重复的组合。
#
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
#
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
def combinationSum3(k, n):
    def cut(k, n):
        i = 1
        j = 9
        s1 = 0
        s2 = 0
        while k > 0:
            s1 += i
            i += 1
            s2 += j
            j -= 1
            k -= 1
        if s1 > n or s2 < n:
            return True  # 无法达到
        else:
            return False

    def sum(l):  # 求列表各个元素的和
        s = 0
        for i in l:
            s += i
        return s

    if cut(k, n):
        return []

    l = [x for x in range(1, 10)]  # 总数组
    res = []
    def backTrace(l, cur_res, index, target): # l
        n = len(l)
        if len(cur_res) == k:
            if sum(cur_res) == target:
                res.append(cur_res[:])
            return

        for i in range(index, len(l)):
            cur_res.append(l[i])
            backTrace(l, cur_res, i+1, target)
            cur_res.pop()

    backTrace(l, [], 0, n)
    print(res)
    return res

combinationSum3(3, 9)
