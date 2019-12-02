# Advent of code day 7


# Part 1
# In what order should the steps in your instructions be completed?
input = open('d7_input.txt')
dependencies = input.read().strip().split('\n')

tasks = set()
for dependency in dependencies:
    tasks.add(dependency[5])
    tasks.add(dependency[36])

dependency_list = dict(list())
for k, v in [(dependency[36], dependency[5]) for dependency in dependencies]:
    if k in dependency_list:
        dependency_list[k].append(v)
    else:
        dependency_list[k] = [v]

# Add tasks with no dependencies to the dependency_list
for task in tasks:
    if task not in dependency_list:
        dependency_list[task] = []

# Run tasks
completed_tasks = dict(zip(tasks, [False] * len(tasks)))
run_order = ""
past_run = list()
finished = False

while not finished:

    ready_to_run = sorted([task for task in dependency_list if len(dependency_list[task]) is 0]) # Sorting fixes the run_order
    past_run += ready_to_run[0]
    run_order = ''.join(past_run)
    completed_tasks[ready_to_run[0]] = True

    for completed in completed_tasks:
        if completed_tasks[completed]:
            if completed in dependency_list:
                del dependency_list[completed]
            for dependency in dependency_list:
                if completed in dependency_list[dependency]:
                    dependency_list[dependency].remove(completed)

    finished = True
    for completed in completed_tasks:
        if completed_tasks[completed] is False:
            finished = False
            break
print(run_order) # Answer for part 1

# Part 2
# With 5 workers and the 60+ second step durations described above,
# how long will it take to complete all of the steps?
