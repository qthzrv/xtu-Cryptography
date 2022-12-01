from random import randint


def randomPrime(nbit=512):  # 随机生成nbit的素数
    while True:
        num = randint(2**(nbit - 1), 2**nbit - 1)
        if isPrime(num):
            return num


def isPrime(n: int) -> bool:
    if n <= 3:
        return n == 2 or n == 3
    if n % 2 == 0:
        return False

    d = n - 1
    while d & 1 == 0:  # 分解n-1为2^s * d
        d >>= 1  # s可以通过n-1和d求出来

    for i in range(16):  # 16轮检验
        if miillerTest(d, n) == False:
            return False
    return True


def miillerTest(d, n: int) -> bool:  # 米勒拉宾素性检验
    a = randint(2, n - 2)
    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = power(x, 2, n)
        d <<= 1
        if x == n - 1:  # 得到-1，后续序列均为1
            return True
        if x == 1:  # 得到1，却没得到-1
            return False
    return False


def power(m, n, p):  # 快速幂求（m^n）%p
    res = 1
    while n:
        if n & 1:
            res = (res * m) % p
        m = (m * m) % p
        n = n >> 1
    return (res % p + p) % p  # 保证结果大于0


def exgcd(a, b):  # 扩展欧几里得算法
    if a == 0 and b == 0:
        return None
    else:
        x1, y1, x2, y2 = 1, 0, 0, 1
        while b:
            q, r = a // b, a % b
            a, b = b, r
            x1, y1, x2, y2 = x2, y2, x1 - q * x2, y1 - q * y2
        return (a, x1, y1)


def inverse(n, p):  # 扩展欧几里得算法求逆元
    gcd, inv, _ = exgcd(n, p)
    assert gcd == 1
    return (inv % p + p) % p  # 保证逆元>0
