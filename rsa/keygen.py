from rsa import randomPrime, inverse
from random import randint
from math import gcd
from os import system

p, q, e = 1, 1, 2  # 预定义p,q,e以模拟实现do-while结构
while True:
    p, q = randomPrime(), randomPrime()
    if gcd(p-1, q-1) < 2**4:  # 使gcd(p-1,q-1)尽可能小
        break

n, r = p*q, (p-1)*(q-1)  # r为偶数

while True:  # 提高算法的安全性
    while gcd(e, r) != 1:
        e = randint(65537, r-1)
    d = inverse(e, r)
    if (d > n**0.25):
        break


print('''
-----BEGIN RSA PUBLIC KEY-----
({:d},{:d})
-----END RSA PUBLIC KEY-----

-----BEGIN RSA PRIVATE KEY-----
({:d},{:d})
-----END RSA PRIVATE KEY-----
'''.format(e, n, d, n))

system("pause")
