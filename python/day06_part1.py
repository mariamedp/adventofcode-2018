import sys

try:
	fname = sys.argv[1]
except:
	fname = '../day06.txt'

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

def any_closest_place(point, place):
	return any(manhattan(r, point) <= manhattan(place, point)
			   for r in all_places if r != place) 


places_finite = []
for place in all_places:
	
	border_proj = [(x_min, place[1]), (x_max, place[1]), 
	               (place[0], y_min), (place[0], y_max)]
	
	finite_place = True
	for bp in set(border_proj):
		finite_place &= any_closest_place(bp, place)
	
	if finite_place:
		places_finite.append(place)
	

largest_area = 0
for place in places_finite:
	
	place_area = 0
	for point in grid:
		if not any_closest_place(point, place):
			place_area += 1
	
	if place_area > largest_area:
		largest_area = place_area
	

print(largest_area)

