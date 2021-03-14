# 706. 设计哈希映射
# 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
# 实现MyHashMap类：
# MyHashMap() 用空映射初始化对象
# void put(int key, int value) 向 HashMap 插入一个键值对(key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
# int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 - 1 。
# void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
#
# 示例：
# 输入：
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# 输出：
# [null, null, null, 1, -1, null, 1, null, -1]
# 解释：
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // myHashMap 现在为[[1, 1]]
# myHashMap.put(2, 2); // myHashMap 现在为[[1, 1], [2, 2]]
# myHashMap.get(1); // 返回 1 ，myHashMap 现在为[[1, 1], [2, 2]]
# myHashMap.get(3); // 返回 - 1（未找到），myHashMap 现在为[[1, 1], [2, 2]]
# myHashMap.put(2, 1); // myHashMap 现在为[[1, 1], [2, 1]]（更新已有的值）
# myHashMap.get(2); // 返回 1 ，myHashMap 现在为[[1, 1], [2, 1]]
# myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为[[1, 1]]
# myHashMap.get(2); // 返回 - 1（未找到），myHashMap 现在为[[1, 1]]
#
# 提示：
# 0 <= key, value <= 106
# 最多调用 10^4 次 put、get 和 remove 方法
#
# 进阶：你能否不使用内置的 HashMap 库解决此问题？
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.n = set()
        self.kv = []


    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.n:
            for k in self.kv:
                if k[0] == key:
                    k[1] = value
        else:
            self.n.add(key)
            self.kv.append([key,value])


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if key in self.n:
            for k in self.kv:
                if k[0] == key:
                    return k[1]
        else:
            return -1


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        if key in self.n:
            self.n.remove(key)
            for k in self.kv:
                if k[0] == key:
                    self.kv.remove(k)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)