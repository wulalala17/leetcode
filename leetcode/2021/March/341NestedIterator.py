# 341. 扁平化嵌套列表迭代器
# 给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
# 列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。
#
# 示例 1:
# 输入: [[1, 1], 2, [1, 1]]
# 输出: [1, 1, 2, 1, 1]
# 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1, 1, 2, 1, 1]。
#
# 示例2:
# 输入: [1, [4, [6]]]
# 输出: [1, 4, 6] 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1, 4, 6]。

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):  # 怎么还有隐藏的NestedInteger(object)类啊，我还以为是要自己写的方法。讨厌设计题
    res = []
    index = -1
    length = 0

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

        self.res = self.add(nestedList)
        self.length = len(self.res)

    def add(self, n):
        r = []
        for x in n:
            if x.isInteger():
                r.append(x.getInteger())
            else:
                r += self.add(x.getList())
        return r

    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        if self.index < self.length:
            return self.res[self.index]
        else:
            return None

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index + 1 < self.length

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
