# Advent of code day 4


# Part 1
# What is the ID of the guard you chose multiplied by the minute you chose?
input = open('d4_input.txt')
sorted_input = open('d4_sorted_input.txt', 'w')
notes = dict()
total_sleeptime = dict()
total_sleeptime_by_minute = dict(list())
for note in input:
    time = note[1:5] + note[6:8] + note[9:11] + note[12:14] + note[15:17]
    time = int(''.join(time))
    notes[time] = note[19:]

for key in sorted(notes.keys()):
    sorted_input.write(str(key) + " " + notes[key])
sorted_input.close()

# Calculate minutes of sleeping
sorted_input = open('d4_sorted_input.txt') # Open for reading
guard_id   = "" # Init value
sleep_time = -1 # Init value
wake_time  = -1 # Init value

for note in sorted_input:
    if "Guard" in note:
        guard_id = note[20:24]
    if "falls asleep" in note:
        sleep_time = int(note[10:12])
    if "wakes up" in note:
        wake_time = int(note[10:12])

        if guard_id in total_sleeptime:
            total_sleeptime[guard_id] += wake_time - sleep_time
        else:
            total_sleeptime[guard_id] = wake_time - sleep_time

        # Add sleeptime per minute
        if guard_id in total_sleeptime_by_minute:
            for i in range(sleep_time, wake_time):
                total_sleeptime_by_minute[guard_id][i] += 1
        else:
            total_sleeptime_by_minute[guard_id] = [0] * 60
            for i in range(sleep_time, wake_time):
                total_sleeptime_by_minute[guard_id][i] = 1

# Get guard with most minutes slept
sleepy_guard  = -1 # Init value
minutes_slept = 0  # Init value
for guard_id in total_sleeptime:
    if minutes_slept < total_sleeptime[guard_id]:
        sleepy_guard = guard_id
        minutes_slept = total_sleeptime[guard_id]

#Get the minute where the guard slept the most
index     = -1 # Init value
sleeptime = 0  # Init value
for i in range(60):
    sleep_per_minute = total_sleeptime_by_minute[sleepy_guard]
    if sleep_per_minute[i] > sleeptime:
        sleeptime = sleep_per_minute[i]
        index = i
print(int(sleepy_guard) * index) # Answer for part 1


# Part 2
# What is the ID of the guard you chose multiplied by the minute you chose?
frequent_guard    = -1 # Init value
minute_most_slept = -1 # Init value
minute_most_slept_time = 0 # For comparing
for guard_id in total_sleeptime_by_minute:
    minutes_slept = total_sleeptime_by_minute[guard_id]
    for minute in range(60):
        if minutes_slept[minute] > minute_most_slept_time:
            frequent_guard = guard_id
            minute_most_slept = minute
            minute_most_slept_time = minutes_slept[minute]
print(int(frequent_guard) * minute_most_slept) # Answer for part 2
