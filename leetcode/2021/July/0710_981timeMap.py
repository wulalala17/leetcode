# 981.基于时间的键值存储
#
# 创建一个基于时间的键值存储类TimeMap，它支持下面两个操作：
#
# 1.set(string key, string value, int timestamp)存储键key、值value，以及给定的时间戳timestamp。
# 2.get(string key, int timestamp)返回先前调用set(key, value, timestamp_prev)所存储的值，其中timestamp_prev <= timestamp。
# 如果有多个这样的值，则返回对应最大的timestamp_prev的那个值。如果没有值，则返回空字符串（""）。
#
# 示例1：
# 输入：inputs = ["TimeMap", "set", "get", "get", "set", "get", "get"], inputs = [[], ["foo", "bar", 1], ["foo", 1],
#                                                                              ["foo", 3], ["foo", "bar2", 4], ["foo", 4],
#                                                                              ["foo", 5]]
# 输出：[null, null, "bar", "bar", null, "bar2", "bar2"]
# 解释：
# TimeMap kv;
# kv.set("foo", "bar", 1); // 存储键"foo"和值"bar"以及时间戳timestamp = 1
# kv.get("foo", 1); // 输出"bar"
# kv.get("foo", 3); // 输出"bar"因为在时间戳3和时间戳2处没有对应"foo"的值，所以唯一的值位于时间戳1处（即"bar"）
# kv.set("foo", "bar2", 4);
# kv.get("foo", 4); // 输出"bar2"
# kv.get("foo", 5); // 输出"bar2"
#
# 示例2：
# 输入：inputs = ["TimeMap", "set", "set", "get", "get", "get", "get", "get"], inputs = [[], ["love", "high", 10],
#                                                                                     ["love", "low", 20], ["love", 5],
#                                                                                     ["love", 10], ["love", 15],
#                                                                                     ["love", 20], ["love", 25]]
# 输出：[null, null, null, "", "high", "high", "low", "low"]
#
# 提示：
# 所有的键 / 值字符串都是小写的。
# 所有的键 / 值字符串长度都在[1, 100]范围内。
# 所有TimeMap.set操作中的时间戳timestamps都是严格递增的。1 <= timestamp <= 10 ^ 7TimeMap.set和TimeMap.get函数在每个测试用例中将（组合）调用总计120000次。

class TimeMap(object):  # 暴力做法
    d = {}
    t = set()
    small = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = set()
        self.d = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.t:
            self.t.add(key)
            self.small[key] = timestamp
        self.d[(key, timestamp)] = value

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.t:  # 没有key
            return ""
        else:
            if self.small[key] > timestamp:
                return ""
            else:
                while (key, timestamp) not in self.d:
                    timestamp -= 1
                return self.d[(key, timestamp)]

# # Your TimeMap object will be instantiated and called as such:
# # obj = TimeMap()
# # obj.set(key,value,timestamp)
# # param_2 = obj.get(key,timestamp)