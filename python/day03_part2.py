import sys

try:
	fname = sys.argv[1]
except:
	fname = '../day03.txt'

with open(fname, 'r') as f:
	input = [str.strip() for str in f.readlines()]


occupied = set()
candidates = {}
for claim in input:
	claim_fields = claim.split(' ')

	claim_start = claim_fields[2][:-1].split(',')
	claim_start = ( int(claim_start[0]), int(claim_start[1]) )

	claim_size = claim_fields[3].split('x')
	claim_size = ( int(claim_size[0]), int(claim_size[1]) )

	claim_sqinches = [(claim_start[0] + 1 + x, claim_start[1] + 1 + y) for x in range(claim_size[0]) for y in  range(claim_size[1])]
	claim_sqinches = set(claim_sqinches)

	cand_overlapped = False
	for cand_id, cand_sqinches in candidates.items():
		overlapped = claim_sqinches & cand_sqinches
		if len(overlapped) > 0:
			occupied = occupied | cand_sqinches
			del candidates[cand_id]
			cand_overlapped = True

	overlapped = claim_sqinches & occupied
	if cand_overlapped | len(overlapped) > 0:
		occupied = occupied | claim_sqinches
	else:
		claim_id = claim_fields[0][1:]
		candidates[claim_id] = claim_sqinches
	
print(candidates.keys())	
