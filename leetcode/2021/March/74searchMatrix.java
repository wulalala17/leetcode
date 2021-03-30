/*
74. 搜索二维矩阵

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
    每行中的整数从左到右按升序排列。
    每行的第一个整数大于前一行的最后一个整数。

示例 1：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

示例 2：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false

提示：
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104
*/

class Solution {  // 评论区的 O(m+n) 解法，从右上角出发每次排除一行
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix[0].length, n = matrix.length;
        int i = 0, j = m - 1;
        while(i < n && j >=0){
            if (matrix[i][j] < target)
                i++;
            else if(matrix[i][j] > target)
                j--;
            else
                return true;
        }
        return false;
    }
}

class Solution {//二维转一维的二分写法
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0)
            return false;
        int begin, mid, end;
        begin = mid = 0;
        int len1 = matrix.length, len2 = matrix[0].length;
        end = len1 * len2 - 1;
        while (begin < end) {
            mid = (begin + end) / 2;
            if (matrix[mid / len2][mid % len2] < target)
                begin = mid + 1;
            else
                end = mid;
        }
        return matrix[begin / len2][begin % len2] == target;
    }
}