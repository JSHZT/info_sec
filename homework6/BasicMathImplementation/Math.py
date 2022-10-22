from random import randrange
    
def multinv(modulus, value):
    x, lastx = 0, 1
    a, b = modulus, value
    while b:
        a, q, b = b, a // b, a % b
        x, lastx = lastx - q * x, x
    result = (1 - lastx * modulus) // value
    if result < 0:
        result += modulus
    assert 0 <= result < modulus and value * result % modulus == 1
    return result

def multimod(a,k,n): 
    ans=1
    while(k!=0):
        if k%2: 
            ans=(ans%n)*(a%n)%n
        a=(a%n)*(a%n)%n
        k=k//2 
    return ans

class Prime(object):
    def is_prime(self, number):
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

    def rand_prime(self, size):
        prime = 1
        while not self.is_prime(prime):
            prime = randrange(size)
        return prime
    
    def get_g(self, n):
        k=(n-1)//2
        for i in range(2,n-1):
            if multimod(i,k,n)!=1:
                return i