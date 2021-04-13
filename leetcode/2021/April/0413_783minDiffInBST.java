/*
783. 二叉搜索树节点最小距离

给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
注意：本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/ 相同

示例 1：
输入：root = [4,2,6,1,3]
输出：1

示例 2：
输入：root = [1,0,48,null,null,12,49]
输出：1

提示：

    树中节点数目在范围 [2, 100] 内
    0 <= Node.val <= 105
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
class Solution {//不用排序的，忘记是搜索树了
    public int minDiffInBST(TreeNode root) {
        int res = 10000;
        Deque<Object> stack = new LinkedList<>();
        List<Integer> v = new ArrayList<>();
        stack.add(root);
        while(stack.size() != 0){
            Object o = stack.pop();
            if(o instanceof Integer){//遍历过
                Integer i = (Integer)o;
                v.add(i);
            }
            else{
                TreeNode t = (TreeNode)o;
                stack.push(t.val);
                if(t.left != null)
                    stack.push(t.left);
                if(t.right != null)
                    stack.push(t.right);
            }
        }
        Collections.sort(v);
        for(int i = 1; i < v.size(); i++){
            res = Math.min(v.get(i) - v.get(i-1), res);
        }
        return res;
    }
}

//官方题解
/*class Solution {
    int pre;
    int ans;

    public int minDiffInBST(TreeNode root) {
        ans = Integer.MAX_VALUE;
        pre = -1;
        dfs(root);
        return ans;
    }

    public void dfs(TreeNode root) {
        if (root == null) {
            return;
        }
        dfs(root.left);
        if (pre == -1) {
            pre = root.val;
        } else {
            ans = Math.min(ans, root.val - pre);
            pre = root.val;
        }
        dfs(root.right);
    }
}

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/solution/er-cha-sou-suo-shu-jie-dian-zui-xiao-ju-8u87w/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。*/