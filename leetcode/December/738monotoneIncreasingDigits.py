# 738. 单调递增的数字
# 给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。
# （当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）
# 示例 1:
# 输入: N = 10
# 输出: 9
# 示例 2:
# 输入: N = 1234
# 输出: 1234
# 示例 3:
# 输入: N = 332
# 输出: 299
# 说明: N 是在 [0, 10^9] 范围内的一个整数。

def monotoneIncreasingDigits(N):  # 从前往后遍历很麻烦
    """
    :type N: int
    :rtype: int
    """

    N = str(N)
    if len(N) < 2:
        return int(N)
    flag = 0  # 判断是否有某位数字大于后一位数字
    res = []
    for i in range(len(N) - 1):
        if flag == 1:
            res.append('9')
            continue
        if N[i] > N[i + 1]:
            res.append('9')
            index = i
            j = i - 1
            while j > -1:  # 往前找，找到第一个和当前不同的数字
                if N[j] == N[i]:
                    j -= 1
                    continue
                else:
                    break

            k = int(N[index]) - 1
            res[j + 1] = str(k)
            for s in range(j+2, index+1):
                res[s] = '9'
            flag = 1
        else:
            res += N[i]
    if flag == 0:
        res.append(N[-1])
    else:
        res.append('9')
    return "".join(res).lstrip('0')

# 10
# 963856657
# 332
print(monotoneIncreasingDigits(963856657))


#  别人的思路更简单 思路：从后往前遍历，如果前面的值大于后面的值就把当前位数减一然后把后面的值变成9，以此类推
# def monotoneIncreasingDigits(N):
#     res = []
#     for n in str(N):
#         res.append(n)
#     index = len(res)
#     for i in range(len(res)-1, 0, -1):
#         if int(res[i-1]) > int(res[i]):
#             k = int(res[i-1]) - 1
#             res[i-1] = str(k)
#             index = i
#     for i in range(index, len(res)):
#         res[i] = '9'
#     return "".join(res).lstrip('0')

