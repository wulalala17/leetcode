def checkPalindromeFormation(a, b):
    def huiwen(s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    if huiwen(a) or huiwen(b):
        return True

    i = 0
    j = len(b) - 1
    while True:
        if a[i] == b[j]:
            s = a[:i+1] + b[i+1:]
            print('第一个%d'%i, s)
            if huiwen(a[:i+1] + b[i+1:]):
                return True
            # if i == j-1 or i==j or i == j-2:
            #     return True
            i += 1
            j -= 1
        else:
            break

    i = 0
    j = len(a) - 1
    while True:
        if b[i] == a[j]:
            s = a[:i + 1] + b[i + 1:]
            print('第二个', s)
            if huiwen(b[:i+1] + a[i+1:]):
                return True
            # if i == j-1 or i==j or i == j-2:
            #     return True
            i += 1
            j -= 1
        else:
            break
    return False

a = "aejbaalflrmkswrydwdkdwdyrwskmrlfqizjezd"
b = "uvebspqckawkhbrtlqwblfwzfptanhiglaabjea"
print(checkPalindromeFormation(a,b))