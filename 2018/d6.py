# Advent of code day 6


# Part 1
# What is the size of the largest area that isn't infinite?
def get_border(destinations):
    x_dests, y_dests = map(list, zip(*destinations))
    min_x, max_x = min(x_dests), max(x_dests)
    min_y, max_y = min(y_dests), max(y_dests)
    return min_x, max_x, min_y, max_y

def get_infinite_destinations(destinations):
    min_x, max_x, min_y, max_y = get_border(destinations)
    outer_dests = [tuple(dest) for dest in destinations if dest[0] == min_x
                    or dest[0] == max_x or dest[1] == min_y or dest[1] == max_y]
    return outer_dests

input = open('d6_input.txt')
destinations = [[int(x), int(y)] for destination in input
                for x, y in [destination.strip().split(", ")]]
inf_area_dest = get_infinite_destinations(destinations)
min_x, max_x, min_y, max_y = get_border(destinations)

# Iterate coordinates within border. Calculate the destination
# closest to each coordinate.
# Answer is destination with biggest area that does not belong to inf_area_dest
shortest_distance = dict()
for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        distance = -1
        destination = []
        for dest in destinations:
            temp_distance =  abs(x - dest[0]) + abs(y - dest[1])
            if distance is -1:
                distance = temp_distance
                destination = dest
                continue
            if distance > temp_distance:
                distance = temp_distance
                destination = dest
                continue
            if distance is temp_distance:
                destination = [-1, -1]
        shortest_distance[(x, y)] = tuple(destination)

area = dict()
for coordinate in shortest_distance:
    if shortest_distance[coordinate] in area:
        area[shortest_distance[coordinate]] = area[shortest_distance[coordinate]] + 1
    else:
        area[shortest_distance[coordinate]] = 1

for k in inf_area_dest: # Remove infinite area destinations
    area.pop(k, None)
    area.pop((-1, -1), None)
max_area = max(area.values())
print(max_area) # Answer for part 1


# Part 2
# What is the size of the region containing all locations which
# have a total distance to all given coordinates of less than 10000?
max_distance = 10000
size = 0
for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        total_distance = sum([abs(x - dest[0]) + abs(y - dest[1]) for dest in destinations])
        if total_distance < max_distance:
            size += 1
print(size) # Answer for part 2
