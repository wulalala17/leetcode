import collections
def isPossible(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    def isValidList(l):
        n = len(l)
        if n < 3:
            return False
        for i in range(n-1):
            if l[i] - l[i+1] != -1:
                return False
        return True

    if isValidList(nums):
        return True
    count = collections.Counter(nums)
    count = sorted(count.items(), key=lambda x:x[1], reverse=True)
    n = len(nums)
    if count[0][1] > 2:
        return False
    if count[0][1] == 1:
        for i in range(n-1):
            if nums[i] - nums[i+1] != -1:
                if isValidList(nums[:i+1]) and isValidList(nums[i+1:]):
                    return True
                else:
                    return False


    nums2 = []
    for i in range(n):
        if count[i][1] == 2:
            nums.remove(count[i][0])
            nums2.append(count[i][0])
        else:
            break
    if not isValidList(nums):
        return False
    else:
        if len(nums2) >= 3:
            if isValidList(nums2):
                return True
            else:
                return False
        else:
            for i in range(len(nums)):
                if nums[i] == nums2[-1]:
                    nums2 = nums2 + nums[i+1:]
                    break
            if isValidList(nums[:i+1]) and isValidList(nums2):
                return True
            else:
                return False

a = [1,2,3,3,4,5]
b = [1,2,3,3,4,4,5,5]
c = [1,2,3,4,4,5]
d = [1,2,5,6,7]
e = [1,2,3,5,6,7]
f = [1,2,3,3,5,6,7]
g = [5,6,6,7,8,8,9,9,10,10]
print(isPossible(g))

# countMap = collections.Counter(nums)  官方题解 理解错题意了，原来是可以分成多个子序列，不是两个
# endMap = collections.Counter()
#
# for x in nums:
#     if (count := countMap[x]) > 0:
#         if (prevEndCount := endMap.get(x - 1, 0)) > 0:
#             countMap[x] -= 1
#             endMap[x - 1] = prevEndCount - 1
#             endMap[x] += 1
#         else:
#             if (count1 := countMap.get(x + 1, 0)) > 0 and (count2 := countMap.get(x + 2, 0)) > 0:
#                 countMap[x] -= 1
#                 countMap[x + 1] -= 1
#                 countMap[x + 2] -= 1
#                 endMap[x + 2] += 1
#             else:
#                 return False
#
# return True
#
# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / split - array - into - consecutive - subsequences / solution / fen - ge - shu - zu - wei - lian - xu - zi - xu - lie - by - l - lbs5 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。