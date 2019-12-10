from int_computer import IntComputer
from int_computer import read_input

program = read_input('day9_input.txt')
program.extend([0] * 100000) # Lengthen for more memory
computer = IntComputer(program)
computer.run()