input = '165432-707912'
input = input.split('-')
input = list(map(int, input))

import itertools

def has_group_andor_double(pwd):
    groups = []
    has_group = False
    has_double = False
    for key, group in itertools.groupby(pwd):
        groups.append(list(group))

    for group in groups:
        if len(group) > 2:
            has_group = True
        if len(group) == 2:
            has_double = True

    return has_double, has_group

def non_decreasing(pwd):
    return all(j <= l for j, l in zip(pwd, pwd[1:]))
    
def part1():
    possible_passwords = 0
    for i in range(input[0], input[1] + 1):
        curr_pwd = str(i)
        has_double, has_group = has_group_andor_double(curr_pwd)

        if non_decreasing(curr_pwd) and (has_double or has_group):
            possible_passwords += 1

    return possible_passwords

def part2():
    possible_passwords = 0
    for i in range(input[0], input[1] + 1):
        curr_pwd = str(i)

        has_double, has_group = has_group_andor_double(curr_pwd)

        if non_decreasing(curr_pwd) and has_double:
            possible_passwords += 1
    return possible_passwords

print(part2())