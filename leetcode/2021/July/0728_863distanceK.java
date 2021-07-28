/*
863. 二叉树中所有距离为 K 的结点

给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。



示例 1：

输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
输出：[7,4,1]
解释：
所求结点为与目标结点（值为 5）距离为 2 的结点，
值分别为 7，4，以及 1



注意，输入的 "root" 和 "target" 实际上是树上的结点。
上面的输入仅仅是对这些对象进行了序列化描述。



提示：

    给定的树是非空的。
    树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
    目标结点 target 是树上的结点。
    0 <= K <= 1000.
*/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {//BFS 挺暴力的，竟然没超时
    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        Map<TreeNode, HashSet<TreeNode>> map = new HashMap<>();//存距离为1的结点（父节点和两个直接子节点）
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        HashSet<TreeNode> set, set1, set2;
        while(!q.isEmpty()){//层序遍历，map存储每个点距离为1的结点
            TreeNode t = q.poll();
            set = map.getOrDefault(t, new HashSet<TreeNode>());
            if(t.left!=null){
                set.add(t.left);
                set1 = map.getOrDefault(t.left, new HashSet<TreeNode>());//添加父节点
                set1.add(t);
                map.put(t.left, set1);
                q.offer(t.left);
            }
            if(t.right!=null){
                set.add(t.right);
                set2 = map.getOrDefault(t.right, new HashSet<TreeNode>());
                set2.add(t);
                map.put(t.right, set2);
                q.offer(t.right);
            }
            map.put(t, set);
        }
        HashSet<TreeNode> visited = new HashSet<>();
        visited.add(target);
        Queue<TreeNode> q1 = new LinkedList<>();
        q1.offer(target);
        for(int i = 0; i < k; i++){//BFS
            int n = q1.size();
            if(n == 0)
                break;
            for(int j = 0; j < n; j++){
                TreeNode t = q1.poll();
                HashSet<TreeNode> h = map.get(t);
                for(TreeNode tt: h){
                    if(visited.contains(tt))
                        continue;
                    else{
                        q1.offer(tt);
                        visited.add(tt);
                    }
                }
            }
        }
        List<Integer> res = new ArrayList<>();
        while(!q1.isEmpty()){
            res.add(q1.poll().val);
        }
        return res;
    }
}
