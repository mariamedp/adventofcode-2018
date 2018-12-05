import sys

try:
	fname = sys.argv[1]
except:
	fname = '../day05.txt'

with open(fname, 'r') as f:
	input = f.read()


input = list(input)
polymer_lengths = {}

for unit in set(u.lower() for u in input):

	input_nounit = [u for u in input if u != unit and u != unit.upper()]
	
	i = 0
	while i < len(input_nounit) - 1:

		if input_nounit[i].islower() and input_nounit[i].upper() == input_nounit[i+1] or \
		   input_nounit[i].isupper() and input_nounit[i].lower() == input_nounit[i+1]:
			
			del input_nounit[i:i+2]
			
			i -= 1
			
		else:
			i += 1

	polymer_lengths[unit] = len(input_nounit)


print(min(polymer_lengths.values()))
