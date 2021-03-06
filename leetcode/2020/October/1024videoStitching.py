# 1024.视频拼接
# 你将会获得一系列视频片段，这些片段来自于一项持续时长为T秒的体育赛事。这些片段可能有所重叠，也可能长度不一。视频片段
# clips[i]都用区间进行表示：开始于clips[i][0]并于clips[i][1]结束。我们甚至可以对这些片段自由地再剪辑，例如片段[0, 7]可以剪切成[0, 1] + [1, 3] + [3, 7]三部分。
# 我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（[0, T]）。返回所需片段的最小数目，如果无法完成该任务，则返回 - 1 。
# 示例
# 1：
# 输入：clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], T = 10
# 输出：3
# 解释：
# 我们选中[0, 2], [8, 10], [1, 9]这三个片段。然后，按下面的方案重制比赛片段：将[1, 9]再剪辑为[1, 2] + [2, 8] + [8, 9] 。现在我们手上有[0, 2] + [2, 8] + [8, 10]，而这些涵盖了整场比赛[0, 10]。
# 示例
# 2：
# 输入：clips = [[0, 1], [1, 2]], T = 5
# 输出：-1
# 解释：我们无法只用[0, 1]和[1, 2]覆盖[0, 5]的整个过程。
# 示例
# 3：
# 输入：clips = [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4],
#             [4, 5], [5, 7], [6, 9]], T = 9
# 输出：3
# 解释：
# 我们选取片段[0, 4], [4, 7]
# 和[6, 9] 。
# 示例
# 4：输入：clips = [[0, 4], [2, 8]], T = 5
# 输出：2
# 解释：
# 注意，你可能录制超过比赛结束时间的视频。
def videoStitching(clips, T):
    d = {}
    for c in clips:
        if c[1] > d.get(c[0], -1):
            d[c[0]] = c[1]
    l = sorted(d.items(), key=lambda item: item[0])
    print(l)
    k = 0
    if l[0][0] != 0:
        return -1
    for li in l:
        if li[1] > k >= li[0]:
            k = li[1]
        if k >= T:
            break
    if k < T:
        return -1
    res = 1
    cur = l[0][1]
    pre = 0
    i = 1
    while i < len(l):
        ma = cur  # 临时记录当前最远
        mi = pre
        flag = 0
        while i < len(l) and l[i][0] <= ma:
            if l[i][1] > cur:
                flag = 1
                cur = l[i][1]
                pre = l[i][0]
            i += 1
        if flag == 1:
            res += 1
        if cur >= T:
            return res









cl = [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4],
             [4, 5], [5, 7], [6, 9]]
print(videoStitching(cl, 9))
