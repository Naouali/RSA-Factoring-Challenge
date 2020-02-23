#!/usr/bin/python3
from prime import *
def fact2(number):
		for i in range(2,number):
			if number % i == 0 and isprime(i) == True:
				break
			
		j = int(number / i)
		print("{:d}={:d}*{:d}".format(number, j, i))
