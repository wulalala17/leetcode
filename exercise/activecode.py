
import random
import hashlib
def generate_code(n):
    a = [chr(i) for i in range(65, 91)]
    b = [chr(i) for i in range(97, 123)]
    c = [i for i in range(10)]
    s = a + b + c
    print(s)
    ss = ''
    for _ in range (n):
        ss += str(s[random.randint(0, 61)])
    return ss

md5 = hashlib.md5()
md5.update('hello world!'.encode('utf-8'))
print(md5.hexdigest())
print(generate_code(10))