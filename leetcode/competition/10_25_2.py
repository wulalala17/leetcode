
def checkArithmeticSubarrays(nums, l, r):
    def isdengcha(l):
        l = sorted(l)
        k = l[1] - l[0]
        for i in range(1, len(l)):
            if l[i] - l[i-1] != k:
                return False
        return True
    res = []
    for i in range(len(l)):
        res.append(isdengcha(nums[l[i]:r[i]+1]))
    return res

a=[4,6,5,9,3,7]
b=[0,0,2]
c=[2,3,5]
print(checkArithmeticSubarrays(a,b,c))