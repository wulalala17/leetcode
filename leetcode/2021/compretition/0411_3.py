class Solution(object):
    def minSideJumps(self, obstacles):  # 能写出t3但比赛中没写出来
        """
        :type obstacles: List[int]
        :rtype: int
        """
        # 思路：dp[i]表示到i要跳跃的次数，cur[i]表示在哪条跑道
        # 如果obstacles[i] != cur[i - 1]，说明不用换跑道，dp[i] = dp[i - 1], cur[i] = cur[i - 1]
        # 否则肯定要进行一次侧跳，dp[i] = dp[i - 1] + 1, 这时候要决定cur[i]跳到哪条跑道上，应该跳到下一个障碍物距离当前更远的跑道
        num1 = 0  # 统计障碍物个数
        num2 = 0
        num3 = 0
        n = len(obstacles)
        if n == 1:
            return 0
        idx1 = [n for i in range(n)]  # i右边障碍物的下标(包括i)
        idx2 = [n for i in range(n)]
        idx3 = [n for i in range(n)]
        for i in range(n - 2, -1, -1):
            if obstacles[i] == 0:  # 当前没障碍物,跟i+1保持一致
                idx1[i] = idx1[i + 1]
                idx2[i] = idx2[i + 1]
                idx3[i] = idx3[i + 1]
                continue
            else:  # 有障碍物则更新对应的跑道
                if obstacles[i] == 1:
                    idx1[i] = i
                    idx2[i] = idx2[i + 1]
                    idx3[i] = idx3[i + 1]
                elif obstacles[i] == 2:
                    idx1[i] = idx1[i + 1]
                    idx2[i] = i
                    idx3[i] = idx3[i + 1]
                else:
                    idx1[i] = idx1[i + 1]
                    idx2[i] = idx2[i + 1]
                    idx3[i] = i

        for o in obstacles:
            if o == 1:
                num1 += 1
                continue
            if o == 2:
                num2 += 1
                continue
            if o == 3:
                num3 += 1
        if num2 == 0:
            return 0

        dp = [0 for _ in range(n)]
        cur = [0 for _ in range(n)]
        dp[0] = 0
        cur[0] = 2  # 一开始在第二条跑道上
        for i in range(1, n):
            if obstacles[i] != cur[i - 1]:  # 不用侧跳
                dp[i] = dp[i - 1]
                cur[i] = cur[i - 1]
            else:
                dp[i] = dp[i - 1] + 1
                x = cur[i - 1]  # 当前跑道
                if obstacles[i - 1] != 0:  # 当前跑道也有障碍，只能侧跳到没障碍的跑道
                    cur[i] = 6 - obstacles[i - 1] - x
                    continue
                else:
                    ma = max(idx1[i], idx2[i], idx3[i])  # 两条无障碍的跑道，选择距离当前更远的那个
                    if ma == n:  # 如果是n说明后面都没障碍，直接返回
                        return dp[i]
                    else:
                        if ma == idx1[i]:
                            cur[i] = 1
                        elif ma == idx2[i]:
                            cur[i] = 2
                        else:
                            cur[i] = 3
        return dp[n - 1]






