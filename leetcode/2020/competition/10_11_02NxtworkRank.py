def maximalNetworkRank(n, roads):
    s = 0
    d = {}
    for r in roads:
        d[r[0]] = d.get(r[0], 0) + 1
        d[r[1]] = d.get(r[1], 0) + 1
    d1 = sorted(d.items(), key=lambda item: item[1], reverse=True)  # 按照字典的value倒序排序
    s = d1[0][1] + d1[1][1]
    if d1[1][1] == d1[0][1]:
        for i in range(len(d1)):
            if d1[i][1] < d1[1][1]:
                break
        for j in range(0, i):
            for k in range(j + 1, i):
                aa = [d1[j][0], d1[k][0]]
                bb = [d1[k][0], d1[j][0]]
                if aa not in roads and bb not in roads:
                    return s
    else:
        for i in range(len(d1)):
            if d1[i][1] < d1[1][1]:
                break
        for k in range(1, i):
            aa = [d1[0][0], d1[k][0]]
            bb = [d1[k][0], d1[0][0]]
            if aa not in roads and bb not in roads:
                return s
    return s-1

"pvhmupgqeltozftlmfjjde"
"yjgpzbezspnnpszebzmhvp"
"aejbaalflrmkswrydwdkdwdyrwskmrlfqizjezd"
"uvebspqckawkhbrtlqwblfwzfptanhiglaabjea"

a = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
b = [[0,1],[0,3],[1,2],[1,3]]
c = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
print(maximalNetworkRank(8, c))

