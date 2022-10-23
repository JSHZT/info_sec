import random
from random import randint
import math

def fastExpMod(b, e, m):
    result = 1
    e = int(e)
    while e != 0:
        if e % 2 != 0: 
            e -= 1
            result = (result * b) % m
            continue
        e >>= 1
        b = (b * b) % m
    return result

def quickPowMod(a,b,m):
    ret =1
    while b:
        if b&1:
            ret =fastExpMod(ret,a,m)
        b//=2
        a = fastExpMod(a,a,m)
    return ret

def is_prime(number):
        if 0 <= number <= 2:
            return False
        primes = []
        for i in range(number + 1):
            primes.append(True)
        primes[0] = False
        primes[1] = False
        for i in range(number + 1):
            if primes[i] is True:
                j = 2 * i
                while j <= number:
                    primes[j] = False
                    j += i
        return primes[number] is True

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def factor(n):
    '''pollard's rho algorithm'''
    if n==1: return []
    if is_prime(n):return [n]
    fact=1
    cycle_size=2
    x = x_fixed = 2
    c = randint(1,n)
    while fact==1:
        for i in range(cycle_size):
            if fact>1:break
            x=(x*x+c)%n
            if x==x_fixed:
                c = randint(1,n)
                continue
            fact = gcd(x-x_fixed,n)
        cycle_size *=2
        x_fixed = x
    return factor(fact)+factor(n//fact)

class rsa_tool(object):
    def miller_rabin_test(self, n):
        p = n - 1
        r = 0
        while p % 2 == 0:
            r += 1
            p /= 2
        b = random.randint(2, n - 2) 
        if fastExpMod(b, int(p), n) == 1:
            return True
        for i in range(0,7):
            if fastExpMod(b, (2 ** i) * p, n) == n - 1:
                return True 
        return False 

    def create_prime_num(self, keylength): 
        while True:
            n = random.randint(0, keylength)
            if n % 2 != 0:
                found = True
                for i in range(0, 10):
                    if self.miller_rabin_test(n):
                        pass
                    else:
                        found = False
                        break
                if found:
                    return n

    def create_keys(self, keylength):
        p = self.create_prime_num(keylength / 2)
        q = self.create_prime_num(keylength / 2)
        n = p * q
        fn = (p - 1)*(q - 1)
        e = self.selectE(fn, keylength / 2)
        d = self.match_d(e, fn)
        return (n, e, d)

    def selectE(self, fn, halfkeyLength):
        while True:
            e = random.randint(0, fn)
            if math.gcd(e, fn) == 1:
                return e

    def match_d(self, e, fn):
        d = 0
        while True:
            if (e * d) % fn == 1:
                return d
            d += 1

    def encrypt(self, M, e, n):
        return fastExpMod(M, e, n)

    def decrypt(self, C, d, m):
        return fastExpMod(C, d, m) 

    def encrypt_file(self):
        f = open('./rsa.txt', "r")
        mess = f.read()
        f.close()
        n, e, d = self.create_keys(1024)
        print("请妥善保管私钥（解密时需要用到）：（n:",n," ,d:",d,")")
        s = ''
        print(mess)
        for ch in mess:
            c = chr(self.encrypt(ord(ch), e, n))
            s += c
        f = open("./pass.txt", "w", encoding='utf-8')
        f.write(str(s))
        print("Encrypt Done!")

    def decrypt_file(self):
        f = open('./pass.txt', 'rb')
        mess = f.read().decode('utf-8')
        f.close()
        n,d= map(int, input("输入您的私钥（n,d）:").split())
        s = ''
        for ch in mess:
            c = chr(self.decrypt(ord(ch), d, n))
            s += c
        f = open("rsa-2.txt", "w", encoding='utf-8')
        f.write(str(s))
        print("Decrypt Done!")
        
