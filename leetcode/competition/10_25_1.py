class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        d = {}
        d[keysPressed[0]] = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            c = keysPressed[i]
            d[c] = max(d.get(c, 0), releaseTimes[i] - releaseTimes[i-1])
        d1 = sorted(d.items(), key=lambda item: item[1], reverse=True)  # 按照字典的value倒序排序
        k = 0
        for i in range(1, len(d1)):
            if d1[i][1] < d1[i-1][1]:
                k = i
                break
        res = d1[0][0]
        for i in range(k):
            if d1[i][0] > res:
                res = d1[i][0]
        return res