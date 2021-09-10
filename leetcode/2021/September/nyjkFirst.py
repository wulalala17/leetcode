def stat_hist(datas, num):

    minValue = min(datas)
    maxValue = max(datas)
    length = (maxValue - minValue) / num
    res = [0 for _ in range(num)]
    for d in datas:
        n = int(d // length)
        if n >= num - 1:
            res[num - 1] += 1
        else:
            res[n] += 1
    return res

if __name__ == '__main__':
    num = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    n = 3
    r = stat_hist(num, n)
    print(r)