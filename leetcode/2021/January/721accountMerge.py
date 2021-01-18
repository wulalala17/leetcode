# 721. 账户合并
# 给定一个列表accounts，每个元素accounts[i]是一个字符串列表，其中第一个元素accounts[i][0]是名称(name)，其余元素是emails表示该账户的邮箱地址。
# 现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
# 合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。账户本身可以以任意顺序返回。

# 示例1：
# 输入：
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
#             ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# 输出：
# [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ["John", "johnnybravo@mail.com"],
#  ["Mary", "mary@mail.com"]]
# 解释：第一个和第三个John是同一个人，因为他们有共同的邮箱地址"johnsmith@mail.com"。第二个John 和 Mary是不同的人，因为他们的邮箱地址没有被其他帐户使用。
# 可以以任何顺序返回这些列表，例如答案[['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
# ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']] 也是正确的。
# 提示：
# accounts的长度将在[1，1000]的范围内。
# accounts[i]的长度将在[1，10]的范围内。
# accounts[i][j] 的长度将在[1，30]的范围内。

class Solution(object):  # 又是不会并查集的一天 :(  就算知道怎么合并，后续的集合操作也不会
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        f = {}

        def find(x):
            f.setdefault(x, x)
            while f[x] != x:
                #x = f[x]
                f[x] = f[f[x]]
                x = f[x]
            return x

        def union(x, y):
            f[find(x)] = find(y)

        lookup = {}
        n = len(accounts)
        for idx, account in enumerate(accounts):
            name = account[0]
            email = account[1:]
            for e in email:
                if e in lookup:
                    union(idx, lookup[e])
                else:
                    lookup[e] = idx
        # print(f)
        disjointSet = defaultdict(set)
        for i in range(n):
            tmp = find(i)
            for es in accounts[i][1:]:
                disjointSet[tmp].add(es)
        # print(disjointSet)
        res = []
        for key, val in disjointSet.items():
            res.append([accounts[key][0]] + list(sorted(val)))
        return res