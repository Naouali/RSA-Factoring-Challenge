#!/usr/bin/python3
def openings(f):
	numbers = list(open(f))
	numbers = [item.replace('\n', '') for item in numbers]
	return [int(x) for x in numbers]
