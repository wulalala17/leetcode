# 5710. 积压订单中的订单总数
# 给你一个二维整数数组 orders ，其中每个 orders[i] = [pricei, amounti, orderTypei] 表示有 amounti 笔类型为 orderTypei 、价格为 pricei
# 的订单。  订单类型 orderTypei 可以分为两种：  0表示这是一批采购订单buy 1表示这是一批销售订单 sell
# 注意，orders[i]表示一批共计amounti笔的独立订单，这些订单的价格和类型相同。对于所有有效的i ，由orders[i]表示的所有订单提交时间均早于orders[i + 1]表示的所有订单。
# 存在由未执行订单组成的积压订单 。积压订单最初是空的。提交订单时，会发生以下情况：
# 如果该订单是一笔采购订单buy ，则可以查看积压订单中价格最低 的销售订单sell 。如果该销售订单 sell的价格低于或等于当前采购订单 buy
# 的价格，则匹配并执行这两笔订单，并将销售订单sell从积压订单中删除。否则，采购订单buy 将会添加到积压订单中。反之亦然，如果该订单是一笔销售订单sell ，则可以查看积压订单中价格
# 最高的采购订单buy 。如果该采购订单 buy的价格高于或等于当前销售订单sell的价格，则匹配并执行这两笔订单，并将采购订单buy从积压订单中删除。否则，销售订单sell
# 将会添加到积压订单中。输入所有订单后，返回积压订单中的订单总数 。由于数字可能很大，所以需要返回对109 + 7取余的结果。
#
#
#
# 示例
# 1：
# 输入：orders = [[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]
# 输出：6
# 解释：输入订单后会发生下述情况：
# - 提交5笔采购订单，价格为10 。没有销售订单，所以这5笔订单添加到积压订单中。
# - 提交2笔销售订单，价格为15 。没有采购订单的价格大于或等于15 ，所以这2笔订单添加到积压订单中。
# - 提交1笔销售订单，价格为25 。没有采购订单的价格大于或等于25 ，所以这1笔订单添加到积压订单中。
# - 提交4笔采购订单，价格为30 。前2笔采购订单与价格最低（价格为15）的2笔销售订单匹配，从积压订单中删除这2笔销售订单。第3
# 笔采购订单与价格最低的1笔销售订单匹配，销售订单价格为25 ，从积压订单中删除这1笔销售订单。积压订单中不存在更多销售订单，所以第4笔采购订单需要添加到积压订单中。
# 最终，积压订单中有5笔价格为10的采购订单，和 1笔价格为30的采购订单。所以积压订单中的订单总数为6 。

def getNumberOfBacklogOrders(orders):  # 改了半天还是超时了
    """
    :type orders: List[List[int]]
    :rtype: int
    """

    def mi(sell):  # 犯了个错误，没用res直接返回i,这样都能通过好几个样例，醉了
        zuixiaozhi = 10 ** 9
        res = -1
        for i in range(len(sell)):
            if sell[i][0] <= zuixiaozhi:
                zuixiaozhi = sell[i][0]
                res = i
        return res

    def ma(buy):
        zdz = 0
        res = -1
        for i in range(len(buy)):
            if buy[i][0] >= zdz:
                zdz = buy[i][0]
                res = i
        return res

    buy = []
    sell = []
    for o in orders:
        f = 0
        if o[2] == 0:
            while sell:
                i = mi(sell)
                if sell[i][0] <= o[0]:  # 价格比采购的小
                    if sell[i][1] < o[1]:  # 数量比当前数量少
                        o[1] -= sell[i][1]
                        sell.pop(i)
                    else:
                        sell[i][1] -= o[1]
                        if sell[i][1] == 0:
                            sell.pop(i)
                        o[1] = 0
                        break
                else:
                    if o[1] > 0:
                        f = 1
                        buy.append(o)
                        break
            if f == 0:
                if o[1] > 0:
                    buy.append(o)
        else:
            while buy:
                i = ma(buy)
                if buy[i][0] >= o[0]:
                    if buy[i][1] < o[1]:
                        o[1] -= buy[i][1]
                        buy.pop(i)
                    else:
                        buy[i][1] -= o[1]
                        if buy[i][1] == 0:
                            buy.pop(i)
                        o[1] = 0
                        break
                else:
                    if o[1] > 0:
                        f = 1
                        sell.append(o)
                        break
            if f == 0:
                if o[1] > 0:
                    sell.append(o)
    re = 0
    for b in buy:
        re += b[1]
    for s in sell:
        re += s[1]
    return re % (10 ** 9 + 7)

ore = [ [10,5,0], [15,2,1], [25,1,1], [30,4,0]]
o2 = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
o3 = [[26,7,0],[16,1,1],[14,20,0],[23,15,1],[24,26,0],[19,4,1],[1,1,0]]
o4 = [[1,29,1],[22,7,1],[24,1,0],[25,15,1],[18,8,1],[8,22,0],[25,15,1],[30,1,1],[27,30,0]]
print(getNumberOfBacklogOrders(o3))



