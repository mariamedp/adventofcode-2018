import sys

try:
	fname = sys.argv[1]
except:
	fname = '../day1.txt'

with open(fname, 'r') as f:
	input = [int(n.strip()) for n in f.readlines()]


i = 0
freq = 0
freqs_seen = set()

while freq not in freqs_seen:
	
	freqs_seen.add(freq)
	freq += input[i]
	
	i = (i + 1) % len(input)


print(freq)
