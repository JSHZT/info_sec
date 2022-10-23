import random
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

    