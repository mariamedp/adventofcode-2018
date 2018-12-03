import sys

try:
	fname = sys.argv[1]
except:
	fname = '../day03.txt'

with open(fname, 'r') as f:
	input = [str.strip() for str in f.readlines()]


occupied_once = set()
overlapped = set()
for claim in input:
	claim_fields = claim.split(' ')

	claim_start = claim_fields[2][:-1].split(',')
	claim_start = ( int(claim_start[0]), int(claim_start[1]) )

	claim_size = claim_fields[3].split('x')
	claim_size = ( int(claim_size[0]), int(claim_size[1]) )

	claim_sqinches = [(claim_start[0] + 1 + x, claim_start[1] + 1 + y) for x in range(claim_size[0]) for y in  range(claim_size[1])]
	claim_sqinches = set(claim_sqinches)

	overlapped = overlapped | (claim_sqinches & occupied_once)
	occupied_once = (occupied_once | claim_sqinches) - overlapped

print(len(overlapped))
