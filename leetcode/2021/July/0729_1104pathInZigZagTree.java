/*
1104. 二叉树寻路

在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。

如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；

而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。

给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。



示例 1：

输入：label = 14
输出：[1,3,4,14]

示例 2：

输入：label = 26
输出：[1,2,6,10,26]



提示：

    1 <= label <= 10^6
*/
class Solution {//二分
    int findRow(int label){
        int n = 20;
        int l = 1, r = 20;
        while(l < r){
            int m = (l + r) / 2;
            int left = (int)Math.pow(2, l) - 1, right = (int)Math.pow(2, r) - 1, mid = (int)Math.pow(2, m) - 1;
            if(label <= mid){
                r = m;
            }
            else{
                l = m + 1;
            }
        }
        return l;
    }
    public List<Integer> pathInZigZagTree(int label) {
        int n = findRow(label);//找到lebel的层数
        int[] order = new int[n];//记录节点顺序，是每一行的第几个
        order[n - 1] = label - (int)Math.pow(2, n - 1);
        for(int i = n - 2; i >= 0; i--){
            order[i] = order[i + 1] / 2;
        }
        for(int i = n - 2; i >= 0; i-=2){//与最后一行的顺序不一样，要反转
            order[i] = (int)Math.pow(2, i) - 1 - order[i];
        }
        for(int i = 0; i < n; i++){
            order[i] = (int)Math.pow(2, i) + order[i];
        }
        List<Integer> res = new ArrayList<>();
        for(int i = 0; i < n; i++)
            res.add(order[i]);
        return res;
    }
}