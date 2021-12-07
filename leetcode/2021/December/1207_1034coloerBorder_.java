/*
1034. 边界着色

给你一个大小为 m x n 的整数矩阵 grid ，表示一个网格。另给你三个整数 row、col 和 color 。网格中的每个值表示该位置处的网格块的颜色。

当两个网格块的颜色相同，而且在四个方向中任意一个方向上相邻时，它们属于同一 连通分量 。

连通分量的边界 是指连通分量中的所有与不在分量中的网格块相邻（四个方向上）的所有网格块，或者在网格的边界上（第一行/列或最后一行/列）的所有网格块。

请你使用指定颜色 color 为所有包含网格块 grid[row][col] 的 连通分量的边界 进行着色，并返回最终的网格 grid 。



示例 1：

输入：grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
输出：[[3,3],[3,2]]

示例 2：

输入：grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
输出：[[1,3,3],[2,3,3]]

示例 3：

输入：grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
输出：[[2,2,2],[2,1,2],[2,2,2]]



提示：

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    1 <= grid[i][j], color <= 1000
    0 <= row < m
    0 <= col < n
*/
class Solution {//DFS
    private int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    private boolean[][] visited;

    public int[][] colorBorder(int[][] grid, int row, int col, int color) {
        int m = grid.length, n = grid[0].length;
        visited = new boolean[m][n];
        dfs(grid, row, col);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] < 0) {
                    grid[i][j] = color;
                }
            }
        }
        return grid;
    }

    public void dfs(int[][] grid, int row, int col) {
        visited[row][col] = true;
        int cnt = 0;
        for (int i = 0; i < 4; i++) {
            int x = row + directions[i][0];
            int y = col + directions[i][1];
            if (x < 0 || x >= grid.length || y < 0 || y >= grid[0].length || Math.abs(grid[row][col]) != Math.abs(grid[x][y])) {
                continue;
            }
            cnt++;
            if (!visited[x][y]) {
                dfs(grid, x, y);
            }
        }
        if (cnt != 4) {
            grid[row][col] = -grid[row][col];   // 如果grid[x][y]处需要换色，则先将该处颜色设为相反数
        }
    }
}