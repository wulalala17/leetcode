/*
897. 递增顺序搜索树

给你一棵二叉搜索树，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。

示例 1：

输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

示例 2：

输入：root = [5,1,7]
输出：[1,null,5,null,7]



提示：

    树中节点数的取值范围是 [1, 100]
    0 <= Node.val <= 1000
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
class Solution { //暴力，在地铁上没做出来
    TreeNode dummy = new TreeNode(0);
    TreeNode pre = dummy;
    List<Integer> l = new ArrayList<>();
    void inorder(TreeNode r){
        if(r == null)
            return;
        inorder(r.left);
        l.add(r.val);
        //pre.left = null;
        //pre.right = r;
        //pre = pre.right;
        inorder(r.right);
    }
    public TreeNode increasingBST(TreeNode root) {
        inorder(root);
        for(int i = 0; i < l.size(); i++){
            TreeNode cur = new TreeNode(l.get(i), null, null);
            pre.right = cur;
            pre = pre.right;
        }
        return dummy.right;
    }
}