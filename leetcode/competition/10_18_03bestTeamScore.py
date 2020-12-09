def bestTeamScore(scores, ages):
    f = 0
    res = 0
    for i in range(len(scores)-1):
        if scores[i+1] < scores[i]:
            f = 1
    for i in range(len(ages)-1):
        if ages[i+1] < ages[i]:
            f = 1
    if f == 0:
        for s in scores:
            res += s
        return res
