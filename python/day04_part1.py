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
			guard_log[guard_id] = { 'mins_asleep': 0, 'entries': [] }
		
	elif message == 'falls asleep':
		min_fall = int(input[i][15:17])
		min_wakeup = int(input[i+1][15:17])
		
		guard_log[guard_id]['mins_asleep'] += (min_wakeup - min_fall)
		guard_log[guard_id]['entries'].append( (min_fall, min_wakeup) )
		
		i += 1 # wake up entry

	else:
		raise Exception(message)

	i += 1


guard_max = max(guard_log.keys(), key=lambda k: guard_log[k]['mins_asleep'])

mins_sel = [m for entry in guard_log[guard_max]['entries'] for m in range(entry[0], entry[1])]
mins_max = max(set(mins_sel), key=lambda m: mins_sel.count(m))

print(guard_max * mins_max)
