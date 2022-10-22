from BasicMathImplementation.Math import Prime

class DH:
	def __init__(self, p=1999):
		self.privatePrime = Prime.rand_prime(p)
		self.sharedPrime = Prime.rand_prime(p)
		self.base = Prime.get_g(p)
		self.key = int()


	def calcPublicSecret(self):
		return (self.base ** self.privatePrime) % self.sharedPrime

	def calcSharedSecret(self, privSecret):
		self.key = (privSecret ** self.privatePrime) % self.sharedPrime