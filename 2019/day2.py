from int_computer import IntComputer

def read_input(file):
    input = open(file, 'r')
    input = input.read().strip().split(',')
    input = list(map(int, input))
    return input

program = read_input('day2_input.txt')

# Part 1
comp = IntComputer(program)
comp.set_value_at_index(1, 12)
comp.set_value_at_index(2, 2)
comp.run()
print(comp.get_value_at_index(0))

# Part 2
program = read_input('day2_input.txt')
comp = IntComputer(program)
wanted_output = 19690720
answer = 0
for noun in range(100):
    for verb in range(100):
        comp.set_value_at_index(1, noun)
        comp.set_value_at_index(2, verb)
        comp.run()
        output = comp.get_value_at_index(0)
        if output == wanted_output:
            answer = 100 * noun + verb
        comp.reset()
print(answer)
        