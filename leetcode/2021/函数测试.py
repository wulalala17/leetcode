import math


def judge(num):
    return True if num == 0 or num & (num - 1) == 0 else False


print(judge(0))
print(judge(1))
print(judge(2))
print(judge(3))
print(judge(4))
print(judge(5))
print(judge(6))
print(judge(7))
print(judge(8))
n = 5
p1 = list(range(n))
p2 = [i for i in range(n)]
print(p1)
print(p2)
a = [1, 2, 3, 3, 4, 110, 110, 110]
print(max(a, key=a.count))


def minCut(s):
    n = len(s)
    g = [[True] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]
    print(g)


# def minCut2(s):
#     n = len(s)
#     g = [[True] * n for _ in range(n)]
#
#     for i in range(0, n):
#         for j in range(i + 1, n):
#             g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]
#     print(g)
#
# minCut("abcddcba")
# minCut2("abcddcba")


def letterCombinations(digits):
    if not digits:
        return list()

    phoneMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrack(index: int):
        if index == len(digits):
            combinations.append("".join(combination))
        else:
            digit = digits[index]
            for letter in phoneMap[digit]:
                combination.append(letter)
                backtrack(index + 1)
                combination.pop()

    combination = list()
    combinations = list()
    backtrack(0)
    return combinations


print(letterCombinations("234"))

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 6]
c = [1, 2, 3, 4, 5]
print(a == c)
ss = ''
ss += '1'
s1 = 'abc'
ss += s1
s3 = '(' + ss + ')'
print(ss)
print('ab' in ss)
print(s3)

r1 = [4, 1, 4]
r2 = [4, 4, 1]
print(sorted(r1) == sorted(r2))
for i in range(1, 5):
    for j in range(1, 5):
        if j != 4:
            print(i * j, end=" ")
        else:
            print(i * j)
x1 = 2
x2 = 2
print(int(x1/x2))
math.ceil(3)
print(math.ceil(3))
print(math.ceil(3.1))
