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

