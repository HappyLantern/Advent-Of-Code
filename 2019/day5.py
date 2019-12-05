
ADD1 = '1'
ADD2 = '01'
MUL1 = '2'
MUL2 = '02'
LOAD = '3'
PRINT = '4'
PRINT2 = '04'
END = '99'

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
    
    def load(self):
        val = int(input())
        op1 = self.program[self.counter + 1]
        #print(op1)
        self.program[op1] = val
        return 2

    def print(self, params):
        val = self.program[self.counter + 1]
        if len(params) == 0:
            val = self.program[val] # Output value
        print("PRINT: " + str(val))
        return 2

    def __get_ops(self, params):
        address = self.program[self.counter + 1]
        address2 = self.program[self.counter + 2]
        address3 = self.program[self.counter + 3]

        op1 = address
        op2 = address2

        if len(params) == 0:
            print("both positional")
            op1 = self.program[address]
            op2 = self.program[address2]

        if len(params) == 1:
            print("2nd positional")
            op2 = self.program[address2]

        if len(params) == 2:

            if params[1] == '0':
                print("1st positional")
                op1 = self.program[address]
            else:
                print("both immidiate")
        
        return op1, op2, address3

    def add(self, params):
        ops = self.__get_ops(params)

        self.program[ops[2]] = ops[0] + ops[1]
       # print("ADD")
       # print("Res address: " + str(ops[2]))
       # print(self.program[ops[2]], ops[0], ops[1])
        return 4

    def mul(self, params):
        ops = self.__get_ops(params)

        
        self.program[ops[2]] = ops[0] * ops[1]
      #  print("MUL")
       # print("Res address: " + str(ops[2]))
       # print(self.program[ops[2]], ops[0], ops[1])
        return 4

    def __next_op(self, inc_counter):
        self.counter += inc_counter

    def part1(self):
        finished = False
        while not finished:
            opcode = str(self.program[self.counter])
            params = []
            if len(opcode) > 1:
                params = opcode[:-2]
                opcode = opcode[-2:]
            inc_counter = 0
            print(opcode, params)
            if opcode == ADD1 or opcode == ADD2:
                inc_counter = self.add(params)
            elif opcode == MUL1 or opcode == MUL2:
                inc_counter = self.mul(params)
            elif opcode == LOAD:
                inc_counter = self.load()
            elif opcode == PRINT or opcode == PRINT2:
                inc_counter = self.print(params)
            elif opcode == END:
                finished = True
            else:
                print("No op")
            self.__next_op(inc_counter)

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


# PART 1
prg = read_input('day5_input.txt')
comp = IntComputer(prg)
comp.part1()