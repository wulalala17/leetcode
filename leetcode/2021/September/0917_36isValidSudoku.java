/*36. 有效的数独

请你判断一个 9x9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

    数字 1-9 在每一行只能出现一次。
    数字 1-9 在每一列只能出现一次。
    数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）

数独部分空格内已填入了数字，空白格用 '.' 表示。

注意：

    一个有效的数独（部分已被填充）不一定是可解的。
    只需要根据以上规则，验证已经填入的数字是否有效即可。



示例 1：

输入：board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：true

示例 2：

输入：board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：false
解释：除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。



提示：

    board.length == 9
    board[i].length == 9
    board[i][j] 是一位数字或者 '.'
*/
class Solution {//看完评论才知道可以用二维数组存每一行/列/九宫格出现的数字，一次遍历就够了
    public boolean isValidSquare(char[][] b){
        for(int i = 0; i < 9; i++){
            int x = i / 3 * 3;
            int y = i % 3 * 3;
            Set<Character> set = new HashSet<>();
            for(int j = x; j < x + 3; j ++){
                for(int k = y; k < y + 3; k++){
                    if(b[j][k] == '.')
                        continue;
                    else{
                        if(set.contains(b[j][k]))
                            return false;
                        else
                            set.add(b[j][k]);
                    }
                }
            }
        }
        return true;
    }
    public boolean isValidRow(char[] b){
        Set<Character> set = new HashSet<>();
        for(int i = 0; i < b.length; i++){
            if(b[i] == '.')
                continue;
            else{
                if(set.contains(b[i]))
                    return false;
                else
                    set.add(b[i]);
            }
        }
        return true;
    }
    public boolean isValidCol(char[][] b){
        for(int i = 0; i < 9; i++){//遍历列
            Set<Character> set = new HashSet<>();
            for(int j = 0; j < 9; j++){
                if(b[j][i] == '.')
                    continue;
                else{
                    if(set.contains(b[j][i]))
                        return false;
                    else
                        set.add(b[j][i]);
                }
            }
        }
        return true;
    }
    public boolean isValidSudoku(char[][] board) {
        for(int i = 0; i < board.length; i++){
            if(!isValidRow(board[i]))
                return false;
        }
        if(!isValidCol(board))
            return false;
        if(!isValidSquare(board))
            return false;
        return true;
    }
}