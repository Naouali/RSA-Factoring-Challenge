#!/usr/bin/python3
def fac(number):
	for i in range(2,number):
		if number % i == 0:
			break
	j = int(number / i)
	print("{:d}={:d}*{:d}".format(number, j, i))
