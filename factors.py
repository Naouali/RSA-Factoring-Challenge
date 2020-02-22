#!/usr/bin/python3
from fac import fac
from lists_to_numbers import *
import sys
fi = sys.argv[1]
fil = open(fi, 'r')
values = []
for x in fil:
	values.append(int(x))
print(values)
k = nums(values)
print(k)
