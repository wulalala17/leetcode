# 402. 移掉K位数字
# 给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
# 注意:
#     num 的长度小于 10002 且 ≥ k。
#     num 不会包含任何前导零。
# 示例 1 :
# 输入: num = "1432219", k = 3
# 输出: "1219"
# 解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
# 示例 2 :
# 输入: num = "10200", k = 1
# 输出: "200"
# 解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
# 示例 3 :
# 输入: num = "10", k = 2
# 输出: "0"
# 解释: 从原数字移除所有的数字，剩余为空就是0。
def removeKdigits(num, k):# 思路错了
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    if len(num) <= k:
        return 0
    indexOfMin = 0
    mmax = 10
    # j = 0
    # te = []
    # while j < len(num) and j < k+2:
    #     if int(num[j]) not in te:
    #         te.append(int(num[j]))
    #         j += 1
    # te = te.sort(reverse=True)
    # for t in te:
    #     i = 0
    #     while i < j:
    #         if int(num[i]) == t:
    for i in range(k+1):
        if int(num[i]) < mmax:
            mmax = int(num[i])
            indexOfMin = i
    num = num[indexOfMin] + num[k+1:]
    i = 0
    while i < len(num):
        if num[i] == '0':
            i += 1
        else:
            num = num[i:]
            break
    if i == len(num):
        return "0"
    return num[:]

# def removeKdigits(num, k):
# numStack = [] 官方题解
#
# # 构建单调递增的数字串
# for digit in num:
#     while k and numStack and numStack[-1] > digit:
#         numStack.pop()
#         k -= 1
#
#     numStack.append(digit)
#
# # 如果 K > 0，删除末尾的 K 个字符
# finalStack = numStack[:-k] if k else numStack
#
# # 抹去前导零
# return "".join(finalStack).lstrip('0') or "0"
#
# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / remove - k - digits / solution / yi - diao - kwei - shu - zi - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


a = "10200"
b = "10"
c = "1432219"
d = "100"
e = "112"
print(removeKdigits(e, 1))
