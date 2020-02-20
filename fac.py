#!/usr/bin/python3
def fac(number):
	if number <= 128:	
		for i in range(2,100):
			for j in range (2,100):
				if i * j == number:
					k_list = []
					m_list = []
					k_list.append(i)
					m_list.append(j)
					k = max(k_list)
					m = min(m_list)			
		print("{:d} = {:d} * {:d}".format(number, k, m))
		k_list.clear()
		m_list.clear()

	
	elif number > 128 and number <= 1000:
		for x in range(128, 1000):
			for y in range(128, 1000):
				if x * y == number:
					i_list = []
					j_list = []
					i_list.append(x)
					j_list.append(y)
					p = max(i_list)
					o = min(j_list)
		print("{:d} = {:d} * {:d}".format(number, p, o))
		i_list.clear()
		j_list.clear()

