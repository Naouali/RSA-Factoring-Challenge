#!/usr/bin/python3
def fac(number):	
	for i in range(2,number):
		for j in range (2,number):
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

