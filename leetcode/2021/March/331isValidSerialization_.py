# 331. 验证二叉树的前序序列化
# 序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。
#      _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
#
# 例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。
# 给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。
# 每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。
# 你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。
#
# 示例 1:
# 输入: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# 输出: true
#
# 示例 2:
# 输入: "1,#"
# 输出: false
#
# 示例 3:
# 输入: "9,#,#,1"
# 输出: false


def isValidSerialization(preorder):  # 思路是对的，但是有个问题，把节点的值当做是唯一的，当出现重复值的时候就会出错，不知道怎么解决
    """
    :type preorder: str
    :rtype: bool
    """
    i = 0
    l = {}
    r = {}
    d = {}
    stack = []
    for j in range(48, 58):
        d[chr(j)] = 0
    num = 0
    while i < len(preorder):
        c = preorder[i]
        if c in d:  # 是数字
            num = num * 10 + int(c)
            while i + 1 < len(preorder) and preorder[i + 1] in d:
                num = num * 10 + int(preorder[i + 1])
                i += 1
            i += 1
            l[num] = 0
            r[num] = 0
            if len(stack) > 0:  # 栈非空
                x = stack[-1]
                if l[x] == 0:  # 左子树还没确定
                    l[x] = 1
                    stack.append(num)
                else:  # 左子树确定
                    if r[x] == 0:  # 右子树还没确定
                        r[x] = 1
                        stack.pop()
                        stack.append(num)
            else:
                stack.append(num)
            num = 0
        elif c == ',':
            i += 1
            continue
        elif c == '#':
            i += 1
            if len(stack) > 0:  # 栈非空
                x = stack[-1]
                if l[x] == 0:  # 左子树还没确定
                    l[x] = 1
                else:  # 左子树确定
                    if r[x] == 0:  # 右子树还没确定
                        r[x] = 1
                        stack.pop()
            else:
                return False
    if len(stack) > 0:

        return False
    return True


a = "9,3,4,#,#,1,#,#,2,#,6,#,#"
b = "1,#"

c = "9,#,#,1"
f = "9,9,#,#,9,#,#"
print(isValidSerialization(f))


# 不需要栈，用已有的string就行，时间复杂度O（n）,空间复杂度O（1），执行4ms。
# string从后遍历，用num记录#的个数，当遇到正常节点时，#的个数-2，并将该节点转化成#，num+1，，整体即为num-1;
# # 当出现num的个数不足2时，即false，最终也须保证num为1。
class Solution:  # 别人的简单写法
    def isValidSerialization(self, preorder: str) -> bool:
        n = len(preorder) - 1
        num = 0
        i = n
        while i >= 0:
            if preorder[i] == ',':
                i -= 1
                continue
            if preorder[i] == '#':
                i -= 1
                num += 1
            else:
                while i>=0 and preorder[i]!=',':
                    i -= 1
                if num >= 2:
                    num -= 1
                else:
                    return False
        if num != 1:
            return False
        return True

