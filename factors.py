#!/usr/bin/python3
from fac import fac
from opening import *
from lists_to_numbers import *
import sys
fi = sys.argv[1]
p = openings(fi)
k = nums(p)
print(k)
