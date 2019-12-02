# Advent of code day 2


# Part 1
# What is the checksum for your list of box IDs?
def char_frequency(str):
    dict = {}
    for s in str:
        if s in dict:
            dict[s] += 1
        else:
            dict[s] = 1
    dict.pop('\n') # Not needed
    return dict

box_list = open('d2_input.txt')
two_count = 0
three_count = 0
word_list = []

for box_id in box_list:
    word_freq = char_frequency(box_id)
    word_list.append(list(box_id.strip())) # For part 2
    if 2 in word_freq.values():
        two_count = two_count + 1
    if 3 in word_freq.values():
        three_count = three_count + 1

checksum = two_count * three_count
print(checksum) # Answer for part 1


# Part 2
# What letters are common between the two correct box IDs?
def word_diff(one, two):
    temp = "".join(one)
    difference = 0
    for i in range(len(one)):
        if one[i] != two[i]:
            difference = difference + 1
            temp = temp.replace(one[i], '')
    if difference is 1: # If only one char removed, answer found.
        return temp
    else:
        return ""

common_letters = ""

for word_one in word_list:
    for word_two in word_list:
        if word_one == word_two:
            continue
        common_letters = word_diff(word_one, word_two)
        if common_letters is not "":
            break
    if common_letters is not "":
        break
print("Common letters: " + common_letters) # Answer for part 2
