import collections


class Solution(object):  # 最终版本 一开始没发现判断2的幂的函数里，0也是2的幂，直接没写出来，改了之后还是超时，必须用哈希表
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        res = 0
        # def judge(num):
        #     if num == 0:
        #         return False
        #     return True if num & (num - 1) == 0 else False
        d = []
        for i in range(0, 32):
            d.append(2 ** i)

        s = collections.Counter(deliciousness)
        for k in s:
            for dd in d:
                if dd - k in s:
                    if dd - k == k:
                        res += s[k] * (s[k] - 1)
                    else:
                        res += s[k] * s[dd - k]
        return (res // 2) % (10 ** 9 + 7)

def countPairs(deliciousness):
    """
    :type deliciousness: List[int]
    :rtype: int
    """
    res = 0
    def judge(num):
        if num == 0:
            return False
        return True if num & (num - 1) == 0 else False

    k = []

    shit = list(collections.Counter(deliciousness).items())
    print(shit)
    for i in range(0, len(shit)):
        for j in range(i+1, len(shit)):
            if judge(shit[i][0] + shit[j][0]):
                k.append(shit[i][0] + shit[j][0])
                res += shit[i][1] * shit[j][1]
    print(k)
    for i in range(0, len(shit)):
        if judge(shit[i][0] * 2):
            res += (shit[i][1] * (shit[i][1]-1)) // 2
    return res % (10**9 + 7)
    # k = []
    # for i in range(0, len(deliciousness)):
    #     for j in range(i, len(deliciousness)):
    #         if judge(deliciousness[i] + deliciousness[j]):
    #             k.append(deliciousness[i] + deliciousness[j])
    #             res += 1
    # print(k)
    # return res % (10 **9 + 7)

f2 = [1,1,1,1,2,2,3]
f3 = [1,1,1,3,3,3,7]
f4 = [0,0,0,1,1,1,2,2,2]
f = [2,14,11,5,1744,2352,0,1,1300,2796,0,4,376]
f5 =[2,14,11,5,1744,2352,0,1,1300,2796,0,4,376,1672,73,55,2006,42,10,6,0,2,2,0,0,1,0,1,0,2,271,241,1,63,1117,931,3,5,378,646,2,0,2,0,15,1]
print(countPairs(f5))



