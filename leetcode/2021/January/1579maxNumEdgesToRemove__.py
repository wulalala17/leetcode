# 1579. 保证图可完全遍历
# Alice和Bob共有一个无向图，其中包含n 个节点和3种类型的边：
# 类型1：只能由Alice遍历。
# 类型2：只能由Bob遍历。
# 类型3：Alice和Bob都可以遍历。
# 给你一个数组edges ，其中edges[i] = [typei, ui, vi]表示节点ui和vi之间存在类型为typei的双向边。
# 请你在保证图仍能够被Alice和Bob完全遍历的前提下，找出可以删除的最大边数。如果从任何节点开始，Alice和Bob都可以到达所有其他节点，则认为图是可以完全遍历的。
# 返回可以删除的最大边数，如果Alice和Bob无法完全遍历图，则返回 - 1 。
# 示例1：
# 输入：n = 4, edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
# 输出：2
# 解释：如果删除[1, 1, 2]和[1, 1, 3]这两条边，Alice和Bob
# 仍然可以完全遍历这个图。再删除任何其他的边都无法保证图可以完全遍历。所以可以删除的最大边数是2 。
#
# 示例 2：
# 输入：n = 4, edges = [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]
# 输出：0
# 解释：注意，删除任何一条边都会使Alice和Bob无法完全遍历这个图。
#
# 示例3：
# 输入：n = 4, edges = [[3, 2, 3], [1, 1, 2], [2, 3, 4]]
# 输出：-1
# 解释：在当前图中，Alice无法从其他节点到达节点4 。类似地，Bob也不能达到节点1 。因此，图无法完全遍历。
#
# 提示：
# 1 <= n <= 10 ^ 5
# 1 <= edges.length <= min(10 ^ 5, 3 * n * (n - 1) / 2)
# edges[i].length == 3
# 1 <= edges[i][0] <= 3
# 1 <= edges[i][1] < edges[i][2] <= n
# 所有元组(typei, ui, vi)互不相同

# 并查集模板
class UnionFind:  # 知道用并查集 不知道怎么删除边，实际上应该是统计多余边的数量
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n

    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufa, ufb = UnionFind(n), UnionFind(n)
        ans = 0

        # 节点编号改为从 0 开始
        for edge in edges:
            edge[1] -= 1
            edge[2] -= 1

        # 公共边
        for t, u, v in edges:
            if t == 3:
                if not ufa.unite(u, v):
                    ans += 1
                else:
                    ufb.unite(u, v)

        # 独占边
        for t, u, v in edges:
            if t == 1:
                # Alice 独占边
                if not ufa.unite(u, v):
                    ans += 1
            elif t == 2:
                # Bob 独占边
                if not ufb.unite(u, v):
                    ans += 1

        if ufa.setCount != 1 or ufb.setCount != 1:
            return -1
        return ans


# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / remove - max - number - of - edges - to - keep - graph - fully - traversable / solution / bao - zheng - tu - ke - wan - quan - bian - li - by - leet - mtrw /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

