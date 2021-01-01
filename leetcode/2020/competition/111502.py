
def closeStrings(word1, word2):
    from collections import Counter
    s1 = set(word1)
    s2 = set(word2)
    print(s1, s2)
    if len(s1 & s2) != len(s1):
        return False
    if len(word1) != len(word2) or len(set(word1)) != len(set(word2)):
        return False

    d1 = Counter(word1)
    d2 = Counter(word2)
    newd1 = sorted(d1.items(), key=lambda item: item[1])
    newd2 = sorted(d2.items(), key=lambda item: item[1])
    print(newd1,newd2)
    for i in range(len(newd1)):
        if newd1[i][1] != newd2[i][1]:
            return False
    return True

a = 'abc'
b = 'bca'
c = 'a'
d = 'aa'
word1 = "uua"
word2 = "ccd"
word3 = "cabbba"
word4 = "aabbss"
print(closeStrings(word1, word2))