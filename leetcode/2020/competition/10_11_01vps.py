def maxDepth(s):
    k = 0
    m = -1
    for i in s:
        if i == '(':
            k += 1
            if k > m:
                m = k
        if i == ')':
            k -= 1
    return m

