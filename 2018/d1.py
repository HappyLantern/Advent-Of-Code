# Advent of code day 1


# PART 1
# Starting with a frequency of zero, what is the resulting frequency after
# all of the changes in frequency have been applied?
frequencies = open('d1_input.txt')
freq_sum = sum([int(freq) for freq in frequencies])
print(freq_sum) # Answer for part 1


# PART 2
# What is the first frequency your device reaches twice?
frequencies.seek(0)
freq_current = 0
freq_answer = 0
freq_dict = dict()
finished = False
while not finished :
    for freq in frequencies:
        freq_current += int(freq)
        if freq_current in freq_dict:
            freq_answer = freq_current
            finished = True
            break
        else:
            freq_dict[freq_current] = 1
    frequencies.seek(0)
print(freq_answer) # Answer for part 2
