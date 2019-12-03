from shapely.geometry import LineString
input = open('day3_input.txt', 'r')
wire_path_1 = input.readline().strip().split(',')
wire_path_2 = input.readline().strip().split(',')

wire_paths = [wire_path_1, wire_path_2]
wire1 = [0, 0]
wire2 = [0, 0]
wires = [wire1, wire2]
path_hist_1 = []
path_hist_2 = []
path_hist = [path_hist_1, path_hist_2]


k = 0
for i in range(len(wire_paths)):
    for step in wire_paths[i]:
        step_type = step[0]
        step_dist= int(step[1:])
    
        if step_type == 'R':
            wires[i][0] += step_dist
        elif step_type == 'U':
            wires[i][1] += step_dist
        elif step_type == 'L':
            wires[i][0] -= step_dist
        else:
            wires[i][1] -= step_dist

        curr_path = wires[i].copy()
        path_hist[i].append(curr_path)
 

distances = []

for i in range(1, len(path_hist[0])):
    for i in range(1, len(path_hist[1])):
        x1 = path_hist[0][i-1][0]
        y1 = path_hist[0][i-1][1]
        x2 = path_hist[0][i][0]
        y2 = path_hist[0][i][1]
        
        x3 = path_hist[1][i-1][0]
        y3 = path_hist[1][i-1][1]
        x4 = path_hist[1][i][0]
        y4 = path_hist[1][i][1]

        line1 = LineString([(x1, y1), (x2, y2)])
        line2 = LineString([(x3, y3), (x4, y4)])
        print(line1.intersection(line2))


print(distances)
# Two wirres connected to a central port and extend outward on a grid.
# One wire per line of text, path of wire
# Find intersection point closest to central port
# Use manhattan distance

