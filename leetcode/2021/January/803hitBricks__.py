# 803.打砖块
#
# 有一个mxn的二元网格，其中1表示砖块，0表示空白。砖块稳定（不会掉落）的前提是：一块砖直接连接到网格的顶部，或者至少有一块相邻（4个方向之一）砖块稳定不会掉落时
# 给你一个数组hits ，这是需要依次消除砖块的位置。每当消除hits[i] = (rowi, coli)
# 位置上的砖块时，对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这一消除操作而掉落。一旦砖块掉落，它会立即从网格中消失（即，它不会落在其他稳定的砖块上）。
# 返回一个数组result ，其中result[i]表示第i次消除操作对应掉落的砖块数目。
# 注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。
#
# 示例1：
# 输入：grid = [[1, 0, 0, 0], [1, 1, 1, 0]], hits = [[1, 0]]
# 输出：[2]
# 解释：
# 网格开始为：
# [[1, 0, 0, 0]，
# [1, 1, 1, 0]]
# 消除(1, 0)处加粗的砖块，得到网格：
# [[1, 0, 0, 0]
#  [0, 1, 1, 0]]
# 两个加粗的砖不再稳定，因为它们不再与顶部相连，也不再与另一个稳定的砖相邻，因此它们将掉落。得到网格：
# [[1, 0, 0, 0],
#  [0, 0, 0, 0]]
# 因此，结果为[2] 。
#
# 示例2：
# 输入：grid = [[1, 0, 0, 0], [1, 1, 0, 0]], hits = [[1, 1], [1, 0]]
# 输出：[0, 0]
# 解释：
# 网格开始为：
# [[1, 0, 0, 0],
#  [1, 1, 0, 0]]
# 消除(1, 1)处加粗的砖块，得到网格：
# [[1, 0, 0, 0],
#  [1, 0, 0, 0]]
# 剩下的砖都很稳定，所以不会掉落。网格保持不变：
# [[1, 0, 0, 0],
#  [1, 0, 0, 0]]
# 接下来消除(1, 0)处加粗的砖块，得到网格：
# [[1, 0, 0, 0],
#  [0, 0, 0, 0]]
# 剩下的砖块仍然是稳定的，所以不会有砖块掉落。因此，结果为[0, 0] 。
# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# grid[i][j]为0或1
# 1 <= hits.length <= 4 * 104
# hits[i].length == 2
# 0 <= xi <= m - 1
# 0 <= yi <= n - 1
# 所有(xi, yi)互不相同

class Solution(object):  # 太难了 完全想不出怎么写
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """

        # ==================== 并查集模板 =========================
        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootx, rooty = find(x), find(y)
            if rootx != rooty:
                if rank[rootx] < rank[rooty]:
                    parent[rootx] = rooty
                    count[rooty] += count[rootx]
                else:
                    parent[rooty] = rootx
                    count[rootx] += count[rooty]
                    if rank[rootx] == rank[rooty]: rank[rootx] += 1

        # =============== 第一步：将所有hits标记的砖块打碎 ==================
        nr, nc = len(grid), len(grid[0])  # 排列长度
        original_grid = copy.deepcopy(grid)  # 复制原图

        for i, j in hits: grid[i][j] = 0  # 打碎所有砖块

        # =============== 第二步：将砖块与相邻砖块连接起来 ==================
        parent = {nr * nc: nr * nc}  # 记录各个位置的父节点（初始一个虚拟屋顶）
        rank = [0] * (nr * nc + 1)  # 记录各个位置的rank（包含屋顶）
        count = [1] * (nr * nc) + [0]  # 记录各个位置连接的节点的数量（包含屋顶）

        for j in range(nc):
            if grid[0][j] == 1: union(j, nr * nc)  # 将最上面一排与屋顶连接

        for r in range(1, nr):  # 将剩余砖块相互连接
            for c in range(nc):
                if grid[r][c] == 1:
                    if grid[r - 1][c] == 1: union(r * nc + c, (r - 1) * nc + c)
                    if c > 0 and grid[r][c - 1] == 1: union(r * nc + c, r * nc + c - 1)

        # =============== 第三步：按照hits逆序往回补充砖块 ==================
        res = []
        for r, c in hits[::-1]:  # 逆序遍历hits
            if original_grid[r][c] == 0:  # 若原grid当中这个位置本身没有砖块，即空白
                res.append(0)  # 则没有砖块掉落
                continue
            origin = count[find(nr * nc)]  # 找到原先与屋顶连接的砖块的数量
            if r == 0: union(c, nr * nc)  # 若当前打击位置是第一排， 则将补回的砖块与屋顶连接
            for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:  # 依次查看四个方向
                if 0 <= x < nr and 0 <= y < nc and grid[x][y] == 1:  # 若存在砖块
                    union(r * nc + c, x * nc + y)  # 则将其与当前砖块连接
            current = count[find(nr * nc)]  # 连接完成之后，再找到现在与屋顶连接的砖块数量
            res.append(max(0, current - origin - 1))  # 计算差值（注意需要减去当前这块砖，因为不算做掉落）
            grid[r][c] = 1  # 补回砖块

        return res[::-1]  # 逆序返回结果

# 出处 https://leetcode-cn.com/problems/bricks-falling-when-hit/solution/python3bing-cha-ji-xian-ji-sui-zhuan-kua-nozq/

