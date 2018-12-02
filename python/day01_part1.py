import sys

try:
	fname = sys.argv[1]
except:
	fname = '../day1.txt'

with open(fname, 'r') as f:
	input = (int(n.strip()) for n in f.readlines())

freq = 0
for n in input:
	freq += n

print(freq)
