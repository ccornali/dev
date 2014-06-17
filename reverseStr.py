import sys

lines = sys.stdin.readlines()

for line in lines[::-1]:
	line = line[:-1]
	print line[::-1]
	
