import sys

try:
	fname = sys.argv[1]
except:
	fname = '../day2.txt'

with open(fname, 'r') as f:
	input = (str.strip() for str in f.readlines())


n_two_letters = 0
n_three_letters = 0
for str in input:

	two_letters = False
	three_letters = False
	for l in set(str):
		n_letters = str.count(l)
		
		if n_letters == 2:
			two_letters = True
		elif n_letters == 3:
			three_letters = True

	n_two_letters += two_letters
	n_three_letters += three_letters


print(n_two_letters * n_three_letters)
