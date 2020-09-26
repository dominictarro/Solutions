'''
Problem:

Although Smilecat couldn't submit a valid solution for this weekly challenge, he learned that
"A number which has only 2 divisors is called a prime number." Smilecat came up with a new
theory that "A number which has only 3 divisors will be called T-prime number."

Take an integer as input. Return True if the number has only 3 divisors otherwise return False.
_______________________________________________________________________________________________


Solution:

The only number than has only three divisors is the square of a number with only two divisors,
a prime. Ergo, we can simplfiy the problem to: is the square root of x a prime?

To implement, we can eliminate most numbers by taking their root and checking if it is an
integer. From there, we know all primes are odd so we can skip all evens (except 2). With

r = x^0.5

To check if r is prime, we can take the modulo of all odd numbers less than r's square root
(since numbers greater than its root will have their coproduct already checked).


'''


def solution(x: int) -> bool:
	r = x**0.5
	if r.is_integer():
		if r < 3:
			return r > 1
		elif r % 2 == 0:
			return False

		for i in range(3, int(r**0.5)+1, 2):
			if r % i == 0:
				return False
		return True
	return False
