from rsa import power
from re import split
from os import system

print("Please enter the plaintext:")
m = int(input())
assert m != 1

print("Please enter the public key in the form of a tuple:")
sc = input()
li = split('[(, )]', sc.replace(' ', ''))
print(li)

e, n = int(li[1]),  int(li[2])
assert m < n
c = power(m, e, n)

print("The ciphertext encrypted is:")
print(c)

system("pause")
