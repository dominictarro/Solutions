'''
As practice and as a challenge your math teacher decides to send messages to the class in an encrypted way.
Each letter of the alphabet is assigned a prime number in ascending consecutive order
(for example: a=2 b=3 c=5 d=7 e=11). You're given the upper bound of the prime corresponding to z (z cannot
be greater than this value). The message is encrypted by multiplying the primes of the adjacent characters.
All letters in the alphabet are used at least once.

Given the number and the list, decrypt the message and return all the letters in order without spaces in
between them.


Encryption:
primes = {'A': 2, 'B': 3, 'C': 5, 'D', 7, 'E': 11, ...}
message = 'EABCDE...'
prime_products = [primes('E')*primes('A'), primes('A')*primes('B'), primes('B')*primes('C'), ...]
 = [22, 6, 15, 35, 77, ...]


Solution:
The given 'zmax' is deceptive, and never needs to be used. By finding the greatest common denominator of
each first two prime products, we can continuously divide all subsequent values and create a list of the
middle values. We can then reverse compute the primes for the first and last values and insert them into the
first and last positions of our newly parsed list.

Because we know the primes and letters ascend in parallel, we can create a sorted list the unique primes and
pair them with their complementary letter.

With this decryption dictionary, we can translate each prime in our parsed list and return the string.
'''


def solution(zmax: int, message: (list, tuple)) -> str:
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	def gcd(a, b):
		# Euclidean gcd algorithm
		while b:
			a, b = b, a%b
		return a

	prior = 0
	i = 0
	# Sometimes the first two values will be the same. If they are, our first divisor will be 1 and our 
	# decryption will fail
	while prior == 0:
		if message[i] != message[i+1]:
			# Get the smaller value
			low = min(message[i], message[i+1])
			# Get the lower value
			high = max(message[i], message[i+1])
			# Use Euclid's GCD to find their shared denominator
			prior = gcd(high, low)
		i += 1

	# Take note of the first divisor. We will need this for inserting the second character's prime and
	# reverse computing the first character's prime
	start = prior
	# For each prime product, divide it by the prior prime and set the prior to this new value
	primes = [prior := val//prior for val in message[1:]]
	primes.insert(0, start)
	primes.insert(0, message[0]//start)

	# Create decryption
	decrypt = {p: alphabet[i] for i, p in enumerate(sorted(set(primes)))}

	# Decode each prime in our parsed list
	return "".join([decrypt[p] for p in primes])

