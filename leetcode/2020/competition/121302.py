
def minPartitions(n):
    """
    :type n: str
    :rtype: int
    """

    def maxTen(n):  # 返回小于n的最大十-二进制数
         k = 0
         res = ''
         while k < len(n):
             res += '1'
             k += 1
         return int(res)


    res = 0
    for i in n:
        if int(i) > res:
            res = int(i)
    return res
print(1231)
