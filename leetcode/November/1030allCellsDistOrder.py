def allCellsDistOrder(R, C, r0, c0):
    """
    :type R: int
    :type C: int
    :type r0: int
    :type c0: int
    :rtype: List[List[int]]
    """
    res = []
    for i in range(R):
        for j in range(C):
            leng = abs(i - r0) + abs(j - c0)
            res.append([i, j, leng])
    res = sorted(res, key=lambda x: x[2])
    res1 = [[res[i][0], res[i][1]] for i in range(len(res))]
    return res1



print(allCellsDistOrder(2, 2, 0, 1))