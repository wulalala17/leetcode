
# import numpy as np
# a = [[0, 5], [2, 4], [3, 6], [4, 0]]
# a.sort(reverse=True)
# print(a)
# c = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
# d = c[:, -1]
# print(d)

# a = [1, 2, 3]
# b = [[1,2,3],[4,5]]
# print(a[-3])

#  测试删除
a = [[-1, -1], [0, 1], [-1, -1]]
del a[1:-1]
# a.remove([-1, -1])
print(a)


d = {}
d[5] = 'sad'
d['sd'] = 6
print(5 in d)
print(6 in d)
print('sad' in d)
print('sd' in d)

from collections import Counter
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
c = Counter(colors)
print(c)

class CA(object):
    def b(self):
        print("b")

    def a(self):
        self.b()

class CB(CA):
    def b(self):
        print("b+")


x1 = CA()
x1.a()
x2 = CB()
x2.a()
ss = ['a','b','c']
print('a' in ss)
print('d' not in ss)
print('a' not in ss)
print(ord('a') - 97)
li = [1,2,3,4,5,6]
print(li.index(5,0,5))


