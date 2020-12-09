def combine(l, k):
    # l = []
    # for x in range(1, n+1):
    #     l.append(x)
    # l = [x for x in range(1, n+1)]  # 别人的写法，先生成数
    n = len(l)
    res = []  # 最终结果
    def backtrace(nums_b, cur_res, index):  # 回溯法  三个参数：剩下的数 当前数组 索引
        if len(cur_res) == k:
            res.append(cur_res[:])
            return

        for i in range(index, n):
            cur_res.append(l[i])
            backtrace(nums_b[index:], cur_res, i)
            cur_res.pop()

    if n == 0 or k == 0:
        return res
    backtrace(l, [], 0)
    return res

# print(combine([2, 3, 4, 5], 5))

def combinationSum(candidates, target):
    def sum(l):
        ss = 0
        for i in l:
            ss += i
        return ss
    res = []
    cur_res = []
    sorted_candidates = sorted(candidates)
    fu = int(target/sorted_candidates[0])
    for x in range(1, fu+1):
        cur_res = combine(sorted_candidates, x)
        # print(cur_res)
        for xx in cur_res:
            if sum(xx) == target:
                res.append(xx)
            # if sum(xx) > target:
            #     break
        # if sum(cur_res[-1]) > target:
        #     break
    print(res)
    # def backTrance(cur_res, n, target):
    #     x = 0
    #     for i in cur_res:
    #         x += i
    #     if x == target:
    #         res.append(cur_res[:])
    #         return
    #     if x > target:
    #         cur_res.pop()
    #         return
    #
    #     for j in sorted_candidates:
    #         cur_res.append(j)
    #         backTrance(cur_res, n , target)
    #         cur_res.pop()
# combinationSum([2,3,5], 8)
print(combine([1,1,2], 3))
