# 685. 冗余连接 II
# 在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。
# 输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
# 结果图是一个以边组成的二维数组。 每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u 和顶点 v 的边，其中 u 是 v 的一个父节点。
# 返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。
# 示例 1:
# 输入: [[1,2], [1,3], [2,3]]
# 输出: [2,3]
# 解释: 给定的有向图如下:
#   1
#  / \
# v   v
# 2-->3
# 示例 2:
# 输入: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# 输出: [4,1]
# 解释: 给定的有向图如下:
# 5 <- 1 -> 2
#      ^    |
#      |    v
#      4 <- 3
# 注意:
#
#     二维数组大小的在3到1000范围内。
#     二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。



def findRedundantDirectedConnection(edges):
    def findcircle(G):
        node_set = set()
        r = len(G)
        have_in_zero = True
        while have_in_zero:
            have_in_zero = False
            for i in range(r):
                if i not in node_set and not any([row[i] for row in G]):
                    node_set.add(i)
                    G[i] = [0] * r
                    have_in_zero = True
                    break
        return False if len(node_set) == r else True

    def yougenshu(ed):   # 判断是否是有根树 输入一个表示图的二维数组
        # print("传进来的数组：", ed)
        l = len(ed)
        setlist = []  # 用来初始化set
        setofpoint = set(setlist)
        k = 0  # 计算边数
        for i in range(1, l):
            ss = 0  # 每一列的和
            for j in range(1, l):
                if ed[j][i] == 1:  # 顶点添加到集合中
                    setofpoint.add(j)
                    setofpoint.add(i)
                ss += ed[j][i]
                if ss > 1:
                    return False
            k += ss
        numofpoint = len(setofpoint)
        if k != numofpoint-1:
            return False
        return True


    ma = len(edges)
    flag = [[0 for _ in range(ma+1)] for _ in range(ma+1)]
    # print(flag)
    setlist = []  #用来初始化set
    for li in edges:
        i = li[0]
        j = li[1]
        setlist.append(i)
        setlist.append(j)
        flag[i][j] = 1
    set_input = set(setlist)

    #print('顶点集合：', set_input)
    #print('边集合：', flag)
    for newli in edges[::-1]:
        i = newli[0]
        j = newli[1]
        flag[i][j] = 0
        if yougenshu(flag) and not findcircle(flag):
            return newli
        else:
            flag[i][j] = 1



e = [[1,2], [1,3], [2,3]]
e2 = [[1,2], [2,3], [3,4], [4,1], [1,5]]
e3 = [[4,2],[1,5],[5,2],[5,3],[2,4]]

print(findRedundantDirectedConnection(e3))
# 超时了 不会写，告辞
# CV的题解 ：   https://leetcode-cn.com/problems/redundant-connection-ii/solution/python-jian-ji-dai-ma-bing-cha-ji-de-yun-yong-by-y/
