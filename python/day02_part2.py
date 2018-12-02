import sys

try:
	fname = sys.argv[1]
except:
	fname = '../day2.txt'

with open(fname, 'r') as f:
	input = [str.strip() for str in f.readlines()]


for i in range(len(input)):
	word1 = input[i]
	
	for j in range(i+1, len(input)):
		word2 = input[j]
		
		result = ''
		skipped = 0
		for k in range(len(word1)):
			
			if word1[k] == word2[k]:
				result += word1[k]
			else:
				if not skipped:
					skipped = 1
				else:
					skipped = 2
					break
		
		if skipped <= 1:
			break

	if skipped <= 1:
		break

print(result)
