def fxxk(n, k):
    def zuheshu(n, m):
        n_jc = 1
        m_jc = 1
        nm_jc = 1
        for i in range(1, n+1):
            n_jc = n_jc*i
        for j in range(1, m+1):
            m_jc = m_jc*j
        for k in range(1, n-m+1):
            nm_jc = nm_jc*k
        return n_jc/(m_jc*nm_jc)


    if k == 0 or k == n*n:
        return 1
    s = 0
    res = []
    for i in range(n+1):
        for j in range(n+1):
            if i*n+(n-i)*j == k:
                res.append((i, j))
    if len(res) == 0:
        return 0
    for r in res:
        s += zuheshu(n, r[0])*zuheshu(n, r[1])
    return s

print(fxxk(6, 36))