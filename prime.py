#!/usr/bin/python3
def isprime(n):
	if n > 1:
		for j in range(2, n):
			if (n % j) == 0:
				return False
			else:
				return True
