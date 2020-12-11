# 649 Dota2参议院
# Dota2的世界里有两个阵营：Radiant(天辉)和Dire(夜魇) Dota2参议院由来自两派的参议员组成。现在参议院希望对一个Dota2
# 游戏里的改变作出决定。他们以一个基于轮为过程的投票进行。在每一轮中，每一位参议员都可以行使两项权利中的一项：
# 禁止一名参议员的权利：参议员可以让另一位参议员在这一轮和随后的几轮中丧失所有的权利。
# 宣布胜利：如果参议员发现有权利投票的参议员都是同一个阵营的，他可以宣布胜利并决定在游戏中的有关变化。
# 给定一个字符串代表每个参议员的阵营。字母 “R” 和 “D” 分别代表了Radiant（天辉）和Dire（夜魇）。然后，如果有n个参议员，给定字符串的大小将是n。
# 以轮为基础的过程从给定顺序的第一个参议员开始到最后一个参议员结束。这一过程将持续到投票结束。所有失去权利的参议员将在过程中被跳过。
# 假设每一位参议员都足够聪明，会为自己的政党做出最好的策略，你需要预测哪一方最终会宣布胜利并在Dota2游戏中决定改变。输出应该是Radiant或Dire。
# 示例1：
# 输入："RD"
# 输出："Radiant"
# 解释：第一个参议员来自Radiant阵营并且他可以使用第一项权利让第二个参议员失去权力，因此第二个参议员将被跳过因为他没有任何权利。然后在第二轮的时候，第一个参议员可以宣布胜利，因为他是唯一一个有投票权的人
# 示例2：
# 输入："RDD"
# 输出："Dire"
# 解释：第一轮中, 第一个来自Radiant阵营的参议员可以使用第一项权利禁止第二个参议员的权利第二个来自Dire阵营的参议员会被跳过因为他的权利被禁止第三个来自
# Dire阵营的参议员可以使用他的第一项权利禁止第一个参议员的权利因此在第二轮只剩下第三个参议员拥有投票的权利, 于是他可以宣布胜利
# 提示：给定字符串的长度在[1, 10, 000]之间.


def predictPartyVictory(senate):
    """
    :type senate: str
    :rtype: str
    """
    def over(num, sen):  # 判断是否终止，终止条件是有投票权利的都为同一方（为1的所有字母都相同）
        s = ''
        for i in range(len(num)):
            if num[i] == 1:
                if s == '':
                    s = sen[i]
                else:
                    if sen[i] != s:
                        return False
        return True

    num = [1 for _ in senate]
    delD, delR = 0, 0  # 待失去投票权利的R,D个数
    n = len(senate)
    while not over(num, senate):
        for i in range(n):
            if num[i] == 0:
                continue
            else:
                if senate[i] == 'R':
                    if delR > 0:
                        num[i] = 0
                        delR -= 1
                        continue
                    else:
                        delD += 1
                if senate[i] == 'D':
                    if delD > 0:
                        num[i] = 0
                        delD -= 1
                        continue
                    else:
                        delR += 1
    for i in range(n):
        if num[i] == 1:
            if senate[i] == 'R':
                return 'Radiant'
            else:
                return 'Dire'

    # def predictPartyVictory(self, senate: str) -> str: 别人写的简单易懂版本
    #     que = list(senate)
    #     while True:
    #         if que.count("R") == 0:
    #             return "Dire"
    #         elif que.count("D") == 0:
    #             return "Radiant"
    #         cur = que.pop(0)
    #         if cur == "R":
    #             que.remove("D")
    #         elif cur == "D":
    #             que.remove("R")
    #         que.append(cur)

    # class Solution:  # 官方题解
    #     def predictPartyVictory(self, senate: str) -> str:
    #         n = len(senate)
    #         radiant = collections.deque()
    #         dire = collections.deque()
    #
    #         for i, ch in enumerate(senate):
    #             if ch == "R":
    #                 radiant.append(i)
    #             else:
    #                 dire.append(i)
    #
    #         while radiant and dire:
    #             if radiant[0] < dire[0]:
    #                 radiant.append(radiant[0] + n)
    #             else:
    #                 dire.append(dire[0] + n)
    #             radiant.popleft()
    #             dire.popleft()
    #
    #         return "Radiant" if radiant else "Dire"
    #
    # 作者：LeetCode - Solution
    # 链接：https: // leetcode - cn.com / problems / dota2 - senate / solution / dota2 - can - yi - yuan - by - leetcode - solution - jb7l /
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。