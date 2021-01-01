
def maxProfit(inventory, orders):
    """
    :type inventory: List[int]
    :type orders: int
    :rtype: int
    """
    if not inventory:
        return
    elif len(inventory) == 1:
        ll = inventory[0]
        r = 0
        kk = 0
        while kk < orders:
            kk += 1
            r += ll
            ll -= 1
        return r

    inv = sorted(inventory, reverse=True)
    i = 0
    k = inv[0]
    res = 0
    j = 1
    flag = 1
    while(i < orders):
        if k > inv[j]:
            res += k * j
            k -= 1
            i += j
        else:
            if j < len(inv) - 1:
                j += 1

    res -= (i-orders) * (k+1)
    return res // (10 ** 9 + 7)

inventory = [2,5]
orders = 4
print(maxProfit(inventory, orders))