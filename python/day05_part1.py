import sys

try:
	fname = sys.argv[1]
except:
	fname = '../day05.txt'

with open(fname, 'r') as f:
	input = f.read()


input = list(input)

i = 0
while i < len(input) - 1:

	if input[i].islower() and input[i].upper() == input[i+1] or \
	   input[i].isupper() and input[i].lower() == input[i+1]:
		
		del input[i:i+2]
		
		i -= 1
		
	else:
		i += 1

print(len(input))
