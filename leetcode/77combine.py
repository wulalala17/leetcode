def combine(n, k):
    # l = []
    # for x in range(1, n+1):
    #     l.append(x)
    l = [x for x in range(1, n+1)]  # 别人的写法，先生成数
    res = []  # 最终结果
    def backtrace(nums_b, cur_res, index):  # 回溯法  三个参数：剩下的数 当前数组 索引
        if len(cur_res) == k:
            res.append(cur_res[:])
            return

        for i in range(index, n):
            cur_res.append(l[i])
            backtrace(nums_b[index:], cur_res, i+1)
            cur_res.pop()


    if n==0 or k==0:
        return res
    backtrace(l, [], 0)
    return res

print(combine(4, 2))