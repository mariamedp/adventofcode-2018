import sys

try:
	fname = sys.argv[1]
except:
	fname = '../day04.txt'

with open(fname, 'r') as f:
	input = [str.strip() for str in f.readlines()]


input = sorted(input)


guard_log = {}
guard_id = None

i = 0
while i < len(input):

	message = input[i][19:]
		
	if message.startswith('Guard'):
		guard_id = int(message.split(' ')[1][1:])
		if guard_id not in guard_log.keys():
			guard_log[guard_id] = {}
		
	elif message == 'falls asleep':
		min_fall = int(input[i][15:17])
		min_wakeup = int(input[i+1][15:17])
		
		for m in range(min_fall, min_wakeup):
			count = guard_log[guard_id].setdefault(m, 0)
			guard_log[guard_id][m] = count + 1
		
		i += 1 # wake up entry

	else:
		raise Exception(message)

	i += 1


guard_max = None
mins_max = None
count_max = 0
for guard_id in guard_log.keys():
	for m in guard_log[guard_id].keys():
		if guard_log[guard_id][m] > count_max:
			guard_max = guard_id
			mins_max = m
			count_max = guard_log[guard_id][m]

print(guard_max * mins_max)
