# 381. O(1) 时间插入、删除和获取随机元素 - 允许重复
#
# 设计一个支持在平均 时间复杂度 O(1) 下， 执行以下操作的数据结构。
#
# 注意: 允许出现重复元素。
#
#     insert(val)：向集合中插入元素 val。
#     remove(val)：当 val 存在时，从集合中移除一个 val。
#     getRandom：从现有集合中随机获取一个元素。每个元素被返回的概率应该与其在集合中的数量呈线性相关。
from random import random


class RandomizedCollection:
    def __init__(self):
        self.vals=[]
        self.index={}
    def insert(self, val: int) -> bool:
        self.vals.append(val)
        if val in self.index:
            self.index[val].add(len(self.vals)-1)
            return False
        else:
            self.index[val] = {len(self.vals)-1}
            return True
    def remove(self,val):
        if val not in self.index:
            return False
        last = len(self.vals)-1
        idx = self.index[val].pop()
        if len(self.index[val])==0:
            del self.index[val]
        if idx!=last:
            self.vals[idx] = self.vals[last]
            self.index[self.vals[idx]].remove(last)
            self.index[self.vals[idx]].add(idx)
        self.vals.pop()
        return True
    def getRandom(self) -> int:
        if self.vals:
            return self.vals[random.randint(0,len(self.vals)-1)]