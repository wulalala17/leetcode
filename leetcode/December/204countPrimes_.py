
def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 2:
        return 0
    def isPrime(n):
        k = int(n ** 0.5) + 1
        for i in range(2, k):
            if n % i ==0:
                return False
        return True
    res = 0
    for i in range(2, n):
        if isPrime(i):
            res += 1
    return res

# class Solution(object):   # 别人的不超时写法
#     def countPrimes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n <= 2:
#             return 0
#         res = [1] * n
#         res[0], res[1] = 0, 0
#         for i in range(2, int(n ** 0.5) + 1):
#             if res[i] == 1:
#                 m = i**2 #起始点就是i平方
#                 while m < n:  # 循环遍历到列表最后一个元素
#                     res[m] = 0
#                     m += i  # 循环间隔为i
#         return sum(res)

print(countPrimes(10))