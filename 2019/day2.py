
ADD = 1
MUL = 2
END = 99

def read_input(file):
    input = open(file, 'r')
    input = input.read().strip().split(',')
    input = list(map(int, input))
    return input

class IntComputer():

    def __init__(self, program):
        self.orig_program = program.copy()
        self.counter = 0
        self.program = program
        self.program[1] = 12
        self.program[2] = 2
        self.program_len = len(self.program)
        
    def add(self):
        op1 = self.program[self.counter + 1]
        op2 = self.program[self.counter + 2]
        op3 = self.program[self.counter + 3]
        self.program[op3] = self.program[op1] + self.program[op2]

    def mul(self):
        op1 = self.program[self.counter + 1]
        op2 = self.program[self.counter + 2]
        op3 = self.program[self.counter + 3]
        self.program[op3] = self.program[op1] * self.program[op2]

    def next_op(self):
        self.counter += 4

    def part1(self):
        finished = False
        while not finished:
            opcode = self.program[self.counter]
            if opcode == ADD:
                self.add()
            if opcode == MUL:
                self.mul()
            if opcode == END:
                finished = True
            self.next_op()
        return self.program[0]

    def __special_output(self, noun, verb):
        self.program[1] = noun
        self.program[2] = verb
        return self.part1()

    def part2(self, noun_range, verb_range, wanted_output):
        for noun in range(noun_range):
            for verb in range(verb_range):
                output = self.__special_output(noun, verb)
                if output == wanted_output:
                    return noun, verb
                self.__reset_input()
        return 0, 0
            
    def __reset_input(self):
        self.program = self.orig_program.copy()
        self.counter = 0

program = read_input('day2_input.txt')

# Part 1
comp = IntComputer(program)
ans = comp.part1()
print(ans)

# Part 2
program = read_input('day2_input.txt')
comp = IntComputer(program)
wanted_output = 19690720
noun, verb = comp.part2(100, 100, wanted_output)
print(100 * noun + verb)


