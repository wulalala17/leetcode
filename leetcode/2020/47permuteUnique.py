# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
# 示例:
# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutations-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
def permuteUnique(candidates):
    t = len(candidates)
    res = []
    cur_res = []
    sorted_candidates = sorted(candidates)
    def exist(li, r):  # 判断li里是否有r
        for ll in li:
            if ll == r:
                return True
        return False

    def backTrace(l, cur_res, index):  # l
        n = len(l)
        if len(cur_res) == t:
            if not exist(res, cur_res):
                res.append(cur_res[:])
            return

        for i in range(index, len(l)):
            cur_res.append(l[i])
            backTrace(l, cur_res, i + 1)
            cur_res.pop()
    backTrace(sorted_candidates, [], 0)
    print(res)
    # return res

def per(can):
    if len(can) == 1:
        return [can]

    def exist(li, r):  # 判断li里是否有r
        for ll in li:
            if ll == r:
                return True
        return False

    if len(can) == 2:
        a = [can[0], can[1]]
        b = [can[1], can[0]]
        res = []
        res.append(a)
        if a != b:
            res.append(b)
        return res

    l = []
    res = []
    for i in range(len(can)):
        cur_res = []
        f = can[i]  # 暂存
        can.pop(i)  # 删除某个数
        cur_res = per(can)  # 删除一个数之后的结果
        for cc in cur_res:
            cc.insert(0, f)  # 把去掉的数加到第一个
            if not exist(res, cc):  # 保证不重复就添加
                res.append(cc)
        can.insert(i, f)  # 插入删除的数
    return res


print(per([1, 1, 2]))
# permuteUnique([1, 1, 2])

# 不明觉厉 https://leetcode-cn.com/problems/permutations-ii/solution/jian-ji-si-lu-11xing-python-by-xiao-yan-gou/
class Solution:
    def permuteUnique(self, nums):
        ret = []

        def search(left,history):
            nonlocal ret
            if not left: #如果没有可以搜的了，说明所有数字用完了
                ret.append(history)

            for i in set(left): #只考虑了当前位置不重复选择，那也就能保证history不重复，所以直接用一个集合来维护
                left.remove(i)
                left.append(i)
                search(left[:-1],history+[i])

        search(nums, [])
        return ret


# 牛逼的剪枝 https://leetcode-cn.com/problems/permutations-ii/solution/hot-100-47quan-pai-lie-ii-python3-hui-su-kao-lu-zh/
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         res = []
#         temp = []
#
#         def back(nums, temp):
#             if not nums:
#                 res.append(temp)
#                 return
#             else:
#                 for i in range(len(nums)):
#                     if i > 0 and nums[i] == nums[i - 1]:
#                         continue
#                     back(nums[:i] + nums[i + 1:], temp + [nums[i]])  # 这种拼接方法是天然的标记，判断前一字符是否在循环里。
#
#         back(nums, temp)
#         return res