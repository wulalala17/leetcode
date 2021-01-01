# 860.柠檬水找零
#
# 在柠檬水摊上，每一杯柠檬水的售价为5美元。顾客排队购买你的产品，（按账单bills支付的顺序）一次购买一杯。每位顾客只买一杯柠檬水，然后向你付5美元、10美元或20美元。
# 你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付5美元。
# 注意，一开始你手头没有任何零钱。如果你能给每位顾客正确找零，返回true ，否则返回false 。
# 示例1：
# 输入：[5, 5, 5, 10, 20]
# 输出：true
# 解释：前3位顾客那里，我们按顺序收取3张5美元的钞票。第4位顾客那里，我们收取一张10美元的钞票，并返还5美元。
# 第5位顾客那里，我们找还一张10美元的钞票和一张5美元的钞票。由于所有客户都得到了正确的找零，所以我们输出true。
# 示例2：
# 输入：[5, 5, 10]
# 输出：true
# 示例3：
# 输入：[10, 10]
# 输出：false
# 示例4：
# 输入：[5, 5, 10, 10, 20]
# 输出：false
# 解释：前2位顾客那里，我们按顺序收取2张5美元的钞票。对于接下来的2位顾客，我们收取一张10美元的钞票，然后返还5美元。对于最后一位顾客，我们无法退回15美元，
# 因为我们现在只有两张10美元的钞票。由于不是每位顾客都得到了正确的找零，所以答案是false。
# 提示：0 <= bills.length <= 10000  bills[i]不是5就是10或是20

# class Solution { Java 版本
#     public boolean lemonadeChange(int[] bills) {
#         int numOfFive = 0, numOfTen = 0;
#         for(int i = 0; i < bills.length; i++){
#             if(numOfFive < 0 || numOfTen < 0)
#                 return false;
#             if (bills[i] == 5){
#                 numOfFive += 1;
#             }
#             else if(bills[i] == 10){
#                 //numOfTwenty += 1;
#                 numOfTen += 1;
#                 numOfFive -= 1;
#             }
#             else{
#                 if (numOfTen > 0){
#                     numOfTen -= 1;
#                     numOfFive -= 1;
#                 }
#                 else{
#                     numOfFive -= 3;
#                 }
#             }
#         }
#         if (numOfFive < 0 || numOfTen < 0)
#             return false;
#         return true;
#     }
# }

def lemonadeChange(self, bills):  # 别人写的版本，把20的情况分成两个
    """
    :type bills: List[int]
    :rtype: bool
    """
    five, ten = 0, 0
    for b in bills:
        if b == 5:
            five += 1
        elif b == 10:
            ten += 1
            five -= 1
        elif ten > 0:
            ten -= 1
            five -= 1
        else:
            five -= 3

        if five < 0:
            return False
    return True