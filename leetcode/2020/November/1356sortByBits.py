# 1356.根据数字二进制下1的数目排序
# 给你一个整数数组arr 。请你将数组中的元素按照其二进制表示中数字1的数目升序排序。如果存在多个数字二进制中1的数目相同，则必须将它们按照数值大小升序排列。请你返回排序后的数组。
# 示例
# 1：
# 输入：arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# 输出：[0, 1, 2, 4, 8, 3, 5, 6, 7]
# 解释：[0]是唯一一个有0个1的数。[1, 2, 4, 8]都有1个1 。[3, 5, 6]有2个1 。[7]有3个1 。按照1的个数排序得到的结果数组为[0, 1, 2, 4, 8, 3, 5, 6, 7]
# 示例2：
# 输入：arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
# 输出：[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
# 解释：数组中所有整数二进制下都只有1个1 ，所以你需要按照数值大小将它们排序。
# 示例3：
# 输入：arr = [10000, 10000]
# 输出：[10000, 10000]
# 示例4：
# 输入：arr = [2, 3, 5, 7, 11, 13, 17, 19]
# 输出：[2, 3, 5, 17, 7, 11, 13, 19]

def sortByBits(arr):
    def numbersOfOne(n):
        res = 0
        while n:
            if n % 2 != 0:
                res += 1
            n = n // 2
        print(res)
        return res

    newshuzu = []
    sorted_arr = sorted(arr)
    for a in sorted_arr:
        newshuzu.append((a, numbersOfOne(a)))
    new = sorted(newshuzu, key=lambda n: n[1])
    r = []
    for n in new:
        r.append(n[0])
    return r
    # return sorted(arr,key=lambda x:(bin(x).count('1'),x)) 一行写法

# def count1(x):  位运算 统计1的个数
#     cnt = 0
#     while x:
#         x &= x - 1
#         cnt += 1
#     return cnt



arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
b = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
c = [10000, 10000]
print(sortByBits(c))
