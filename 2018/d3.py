# Advent of code day 3


# Part 1
# How many square inches of fabric are between two or more claims?
import re
input = open('d3_input.txt')
data = [re.findall('\d+', claim) for claim in input]

claim_count = dict()

for claim in data:
    id = int(claim[0])
    start_x = int(claim[1])
    start_y = int(claim[2])
    width_x = int(claim[3])
    height_y = int(claim[4])
    for x in range(start_x, start_x + width_x):
        for y in range(start_y, start_y + height_y):
            if (x, y) in claim_count:
                claim_count[(x, y)] += 1
            else:
                claim_count[(x, y)] = 1

count = 0
for inch in claim_count:
    if claim_count[inch] >= 2:
        count += 1
print(count) # Answer for part 1


# Part 2
# What is the ID of the one claim that doesn't overlap?
overlaps = dict()
id = -1
for claim in data:
    temp_id = int(claim[0])
    overlaps[temp_id] = False
    start_x = int(claim[1])
    start_y = int(claim[2])
    width_x = int(claim[3])
    height_y = int(claim[4])
    for x in range(start_x, start_x + width_x): # Iterate each inch and look at count
        for y in range(start_y, start_y + height_y):
            if claim_count[(x, y)] > 1:
                overlaps[temp_id] = True
                continue
    if overlaps[temp_id] is False:
        id = temp_id
        break
print(id) # Answer for part 2
