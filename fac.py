#!/usr/bin/python3
def fac(number):
	i_list = []
	for i in range(2,number):
		if number % i == 0:
			break
			i_list.append(i)
	j = int(number / i)
	print("{:d}={:d}*{:d}".format(number, j, i))
	i_list.clear()
