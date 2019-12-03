input = open('day3_input.txt', 'r')
wire_path_1 = input.readline().strip().split(',')
wire_path_2 = input.readline().strip().split(',')
paths = [wire_path_1, wire_path_2]

distances = [] # Answer for part 1
steps_to_intersection = [] # Answer for part 2

lines = [[], []]
lines_dir = [[], []]
steps = [[], []]

# Create all lines and the steps (size) of that line
for i in range(2): 
    start = [0, 0]

    for move in paths[i]:
        dir = move[0]
        step = int(move[1:])
        next = start.copy()
        if dir == 'R':
            next[0] += step
            dir = 'H'
        if dir == 'L':
            next[0] -= step
            dir = 'H'
        if dir == 'D':
            next[1] -= step
            dir = 'V'
        if dir == 'U':
            next[1] += step
            dir = 'V'

        x1 = start[0]
        y1 = start[1]
        x2 = next[0]
        y2 = next[1]

        start = next.copy()

        lines[i].append((x1, x2, y1, y2))
        lines_dir[i].append(dir)

        if len(steps[i]) == 0:
            steps[i].append(abs(x2 - x1) + abs(y2 - y1))
        else:
            steps[i].append(steps[i][-1] + abs(x2 - x1) + abs(y2 - y1))

# Look for intersections
i = 0
for line_1 in lines[0]:
    j = 0
    for line_2 in lines[1]:
        if (lines_dir[0][i] == 'H' and lines_dir[1][j] == 'V' and
                ((line_1[0] <= line_2[0] <= line_1[1]) or (line_1[0] >= line_2[0] >= line_1[1])) and
                ((line_2[2] <= line_1[2] <= line_2[3]) or line_2[2] >= line_1[2] >= line_2[3])):
                distances.append(line_2[0] + line_1[2])
                line_1_steps = steps[0][i-1] + abs(line_1[0] - line_2[0])
                line_2_steps = steps[1][j-1] + abs(line_2[2] - line_1[2])
                steps_to_intersection.append(line_1_steps + line_2_steps)

        if (lines_dir[0][i] == 'V' and lines_dir[1][j] == 'H' and
                ((line_2[0] <= line_1[0] <= line_2[1]) or (line_2[0] >= line_1[0] >= line_2[1])) and
                ((line_1[2] <= line_2[2] <= line_1[3]) or line_1[2] >= line_2[2] >= line_1[3])):
                distances.append(line_1[0] + line_2[2])
                line_1_steps = steps[0][i-1] + abs(line_1[2] - line_2[2])
                line_2_steps = steps[1][j-1] + abs(line_2[0] - line_1[0])
                steps_to_intersection.append(line_1_steps + line_2_steps)
            
        j += 1
    i += 1
 
print(min(distances)) # Part 1
print(min(steps_to_intersection)) # Part 2