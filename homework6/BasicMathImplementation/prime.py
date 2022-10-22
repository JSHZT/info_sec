from random import randrange

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