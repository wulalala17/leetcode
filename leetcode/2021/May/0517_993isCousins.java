/*
993. 二叉树的堂兄弟节点

在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。

我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。

只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。



示例 1：

输入：root = [1,2,3,4], x = 4, y = 3
输出：false

示例 2：

输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
输出：true

示例 3：

输入：root = [1,2,3,null,4], x = 2, y = 3
输出：false



提示：

    二叉树的节点数介于 2 到 100 之间。
    每个节点的值都是唯一的、范围为 1 到 100 的整数。
*/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {//层次遍历，时间超过100%，感觉比评论里的DFS快
    public boolean isCousins(TreeNode root, int x, int y) {
        if(root.val == x || root.val == y)
            return false;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        int dx = -1, dy = -2, d = 0;//深度
        int fx = -1, fy = -2;//父节点
        int n = 0;//队列长度
        while(!queue.isEmpty()){
            n = queue.size();
            d += 1;
            for(int i = 0; i < n; i++){
                TreeNode t = queue.poll();
                if(t.left != null){
                    if (t.left.val == x){
                        dx = d + 1;
                        fx = t.val;
                    }
                    else if (t.left.val == y){
                        dy = d + 1;
                        fy = t.val;
                    }
                    queue.add(t.left);
                }
                if(t.right != null){
                    if (t.right.val == x){
                        dx = d + 1;
                        fx = t.val;
                    }
                    else if (t.right.val == y){
                        dy = d + 1;
                        fy = t.val;
                    }
                    queue.add(t.right);
                }
            }
            if(dx != -1 || dy != -2)
                return dx == dy && fx != fy;
        }
        return dx == dy && fx != fy;

    }
}