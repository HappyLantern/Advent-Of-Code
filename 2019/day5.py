
from int_computer import IntComputer

def read_input(file):
    input = open(file, 'r')
    input = input.read().strip().split(',')
    input = list(map(int, input))
    return input

# PART 1 and PART 2
program = read_input('day5_input.txt')
computer = IntComputer(program)
computer.run()