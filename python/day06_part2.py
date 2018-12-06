import sys

try:
	fname = sys.argv[1]
	MAX_DIST = int(sys.argv[2])
except:
	fname = '../day06.txt'
	MAX_DIST = 10000

x_coord = []
y_coord = []
with open(fname, 'r') as f:
	for l in f.readlines():
		coords = l.strip().split(', ')
		x_coord.append(int(coords[0]))
		y_coord.append(int(coords[1]))

x_min, x_max = min(x_coord), max(x_coord)
y_min, y_max = min(y_coord), max(y_coord)

all_places = [[x_coord[i], y_coord[i]] for i in range(len(x_coord))]
grid = [[x, y] for x in range(x_min, x_max) for y in range(y_min, y_max)]


def manhattan(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


size_region = 0
for point in grid:
	
	total_dist = sum([manhattan(point, place) for place in all_places])
	if total_dist < MAX_DIST:
		size_region += 1

print(size_region)

