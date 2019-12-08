ADD1 = '1'
ADD2 = '01'
MUL1 = '2'
MUL2 = '02'
LOAD = '3'
PRINT1 = '4'
PRINT2 = '04'
END = '99'
JIT1 = '5'
JIT2 = '05'
JIF1 = '6'
JIF2 = '06'
LT1 = '7'
LT2 = '07'
EQ1 = '8'
EQ2 = '08'

import itertools

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
        self.program_len = len(self.program)
        self.finished = False
    
    def load(self, load_val):
        address = self.program[self.counter + 1]
        self.program[address] = (load_val[0] if self.counter == 0 else load_val[1])
        self.__update_pointer(self.counter + 2)

    def print(self, params):
        val = self.program[self.counter + 1]
        if len(params) == 0:
            val = self.program[val]
        self.output = val
        self.__update_pointer(self.counter + 2)

    def add(self, params):
        ops = self.__get_ops_3(params)
        self.program[ops[2]] = ops[0] + ops[1]
        self.__update_pointer(self.counter + 4)

    def mul(self, params):
        ops = self.__get_ops_3(params)
        self.program[ops[2]] = ops[0] * ops[1]
        self.__update_pointer(self.counter + 4)

    def equals(self, params):
        ops = self.__get_ops_3(params)
        self.program[ops[2]] = (1 if ops[0] == ops[1] else 0)
        self.__update_pointer(self.counter + 4)

    def less(self, params):
        ops = self.__get_ops_3(params)
        self.program[ops[2]] = (1 if ops[0] < ops[1] else 0)
        self.__update_pointer(self.counter + 4)

    def jump_true(self, params):
        condition, pointer, _ = self.__get_ops_3(params)
        pointer = (pointer if condition != 0 else self.counter + 3)
        self.__update_pointer(pointer)

    def jump_false(self, params):
        condition, pointer, _ = self.__get_ops_3(params)
        pointer = (pointer if condition == 0 else self.counter + 3)
        self.__update_pointer(pointer)

    def __get_ops_3(self, params):
        value_one   = self.program[self.counter + 1]
        value_two   = self.program[self.counter + 2]
        res_address = self.program[self.counter + 3]

        op1 = value_one
        op2 = value_two

        if len(params) == 0:
            op1 = self.program[value_one]
            op2 = self.program[value_two]

        if len(params) == 1:
            op2 = self.program[value_two]

        if len(params) == 2 and params[1] == '0':
            op1 = self.program[value_one]

        return op1, op2, res_address

    def __update_pointer(self, pointer):
        self.counter = pointer

    def run(self, phase, inp):
        load_vals = [phase, inp]
        while not self.finished:
            opcode, params = self.__instruction()
            if opcode == ADD1 or opcode == ADD2:
                self.add(params)
            elif opcode == MUL1 or opcode == MUL2:
                self.mul(params)
            elif opcode == LOAD:
                self.load(load_vals)
            elif opcode == PRINT1 or opcode == PRINT2:
                self.print(params)
                break
            elif opcode == JIT1 or opcode == JIT2:
                self.jump_true(params)
            elif opcode == JIF1 or opcode == JIF2:
                self.jump_false(params)
            elif opcode == EQ1 or opcode == EQ2:
                self.equals(params)
            elif opcode == LT1 or opcode == LT2:
                self.less(params)
            elif opcode == END:
                self.finished = True
            else:
                print("No op")

        return self.output
    
    def __instruction(self):
        opcode = str(self.program[self.counter])
        params = []
        if len(opcode) > 1:
            params = opcode[:-2]
            opcode = opcode[-2:]
        return opcode, params
             
    def reset(self):
        self.program = self.orig_program.copy()
        self.finished = False
        self.counter = 0
        
class Amplifier():

    def __init__(self, program):
        self.computer = IntComputer(program)
        self.result   = 0

    def amplify(self, phase, inp):
        self.result = self.computer.run(phase, inp)
        return self.result
    
    def reset_amplifier(self):
        self.computer.reset()

    def finished(self):
        return self.computer.finished

class AmplifierSeries():

    def __init__(self, n_amp, program):
        self.n_amp = n_amp
        self.program = program
        self.amplifiers = []
        for i in range(n_amp):
            self.amplifiers.append(Amplifier(program.copy()))
        
    def part1(self, phase_base, inp):
        phase_permutations = list(itertools.permutations(phase_base))

        output = []
        for phases in phase_permutations:
            output.append(self.__part1(phases, inp))
            self.__reset_amplifiers()

        return max(output)

    def __part1(self, phases, inp):
        for i in range(self.n_amp):
            inp = self.amplifiers[i].amplify(phases[i], inp)
        return inp

    def part2(self, phase_base, inp):
        phase_permutations = list(itertools.permutations(phase_base))
        output = []

        for phases in phase_permutations:
            output.append(self.__part2(phases, inp))
            self.__reset_amplifiers()

        return max(output)
    def __part2(self, phase, inp):

        while not all(amplifier.finished() for amplifier in self.amplifiers):
            for i in range(self.n_amp):
                inp = self.amplifiers[i].amplify(phase[i], inp)

        return inp
    
    def __reset_amplifiers(self):
        for amplifier in self.amplifiers:
            amplifier.reset_amplifier()

program = read_input('day7_input.txt')
init_input = 0
number_amplifiers = 5
series = AmplifierSeries(number_amplifiers, program)

# PART 1
phases = [0, 1, 2, 3, 4]
ans = series.part1(phases, init_input)
print(ans)

# PART 2
phases = [5, 6, 7, 8, 9]
ans = series.part2(phases, init_input)
print(ans)
