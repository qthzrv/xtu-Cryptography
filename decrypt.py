from rsa import power
from re import split
from os import system

print("Please enter the ciphertext:")
c = int(input())
assert c != 1

print("Please enter the private key in the form of a tuple:")
sc = input()
li = split('[(, )]', sc.replace(' ', ''))

d, n = int(li[1]),  int(li[2])
assert c < n
m = power(c, d, n)

print("The plaintext decrypted is:")
print(m)

system("pause")
