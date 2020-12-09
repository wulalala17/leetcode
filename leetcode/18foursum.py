# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
#
# 示例：
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]




def fourSum(nums, target):
    def sumoflist(l):
        sum = 0
        for i in l:
            sum += i
        return sum

    res = []
    used = [0 for _ in nums]
    def backtrace(l, cur, index, target, used, s):
        nonlocal res
        if s > target and target>0:
            return
        if len(cur) == 4:
            if s == target:
                res.append(cur[:])
            return

        for i in range(index, len(l)):
            if i >= 1 and l[i] == l[i-1] and used[i-1] == 0:
                continue
            s += l[i]
            cur.append(l[i])
            used[i] = 1
            backtrace(l, cur, i+1, target, used, s)
            s -= l[i]
            used[i] = 0
            cur.pop()

    l0 = sorted(nums)
    backtrace(l0, [], 0, target, used, 0)
    return res


a = [1, 0, -1, 0, -2, 2]
b = [-1, 0, 1, 2, -1, -4]
t = 0
t2 = -1
print(fourSum(b, t2))


#         res = []
#         dic = Counter(nums) #对每个数出现的次数进行统计
#         arr = sorted(dic.keys())  #排序键值
#         for i, a in enumerate(arr):
#             dic[a] -= 1 #a用掉了一次，而且a的位置之后不会再遍历到了，不需要加回
#             for j, b in enumerate(arr[i:]):  #从arr[i]开始找b的值
#                 if dic[b] < 1: #b可能等于a，判断一下，如果dic[b]不够1个，跳过这次循环
#                     continue
#                 dic[b] -= 1
#                 for c in arr[i+j:]:  #从arr[i+j]开始找c的值，注意上一层循环枚举j以后，需要再加最外层的i
#                     if dic[c] < 1: #同上层循环b的判断
#                         continue
#                     d = target - (a + b + c)
#                     if d < c:   #因为是非递减顺序，如果d小于c，就直接跳出，这样就可以避免重复
#                         break
#                     if (d == c and dic[d] > 1) or (d > c and dic[d] > 0):
#                         res.append([a, b, c, d])
#                 dic[b] += 1 #b现在所处的位置，之后a还会遍历到，因此需要加回1
#         return res
#
# 作者：AIResearcherJHM
# 链接：https://leetcode-cn.com/problems/4sum/solution/can-zhao-san-shu-he-si-lu-jian-dan-pai-xu-ha-xi-by/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


