class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.string = ["" for _ in range(n)]
        self.ptr = 0


    def insert(self, id, value):
        """
        :type id: int
        :type value: str
        :rtype: List[str]
        """
        self.string[id-1] = value
        res = []
        if id-1 == self.ptr:
            while self.ptr < len(self.string):
                if self.string[self.ptr] != "":
                    res.append(self.string[self.ptr])
                    self.ptr += 1
                else:
                    return res
                    break
        return res
os = OrderedStream(5)
print(os.insert(3, "ccc"))
print(os.insert(1, "caa"))
print(os.insert(2, "bbb"))
print(os.insert(5, "eee"))
print(os.insert(4, "ddd"))




# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)