/*剑指 Offer 37. 序列化二叉树

请实现两个函数，分别用来序列化和反序列化二叉树。

你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。



示例：

输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]



注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
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
public class Codec {//没想到递归，其实也不难


    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null){
            return "null,";
        }
        String res = root.val + ",";
        res += serialize(root.left);
        res += serialize(root.right);
        return res;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] arr = data.split(",");
        Queue<String> queue = new LinkedList<String>();
        for(int i = 0; i < arr.length; i++){
            queue.offer(arr[i]);
        }
        return help(queue);
    }
    public TreeNode help(Queue<String> queue){
        String val = queue.poll();
        if(val.equals("null")){
            return null;
        }
        TreeNode r = new TreeNode(Integer.valueOf(val));
        root.left = help(queue);
        root.right = help(queue);
        return r;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));