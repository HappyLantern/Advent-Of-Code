# OPS
ADD   = 1
MUL   = 2
LOAD  = 3
PRINT = 4
JIT   = 5
JIF   = 6
LESS  = 7
EQUAL = 8
UREL   = 9
END   = 99

#MODES
POS = 0
IM  = 1
REL = 2

def read_input(file):
    input = open(file, 'r')
    input = input.read().strip().split(',')
    input = list(map(int, input))
    return input

class IntComputer():

    def __init__(self, program, interrupt=False):
        self.orig_program = program.copy()
        self.counter = 0
        self.relative = 0
        self.output = 0
        self.load_values = []
        self.program = program
        self.interrupt=interrupt
        self.program_len = len(self.program)
        self.finished = False
    
    def update_relative(self, params):

        if params[0] == POS:
            value = self.program[self.program[self.counter + 1]]
        elif params[0] == REL:
            value = self.program[self.program[self.counter + 1] + self.relative]
        elif params[0] == IM:
            value = self.program[self.counter + 1]
            
        self.relative += value
        self.__update_pointer(self.counter + 2)

    def load(self, params):

        if len(self.load_values) == 0:
            value = int(input())
        else:
            value = self.load_values.pop(0)

        if params[0] == POS:
            self.program[self.program[self.counter + 1]] = value
        elif params[0] == REL:
            self.program[self.program[self.counter + 1] + self.relative] = value
        elif params[0] == IM:
            self.program[self.counter + 1] = value

        self.__update_pointer(self.counter + 2)

    def print(self, params):
        if params[0] == POS:
            self.output = self.program[self.program[self.counter + 1]]
        elif params[0] == IM:
            self.output = self.program[self.counter + 1]
        elif params[0] == REL:
            self.output = self.program[self.program[self.counter + 1] + self.relative]

        #print("PRINT: " + str(self.output))
        self.__update_pointer(self.counter + 2)

    def add(self, params):
        op1, op2, op3 = self.__get_ops(params)
        self.program[op3] = op1 + op2
        self.__update_pointer(self.counter + 4)

    def mul(self, params):
        op1, op2, op3 = self.__get_ops(params)
        self.program[op3] = op1 * op2
        self.__update_pointer(self.counter + 4)

    def equals(self, params):
        op1, op2, op3 = self.__get_ops(params)
        self.program[op3] = (1 if op1 == op2 else 0)
        self.__update_pointer(self.counter + 4)

    def less(self, params):
        op1, op2, op3 = self.__get_ops(params)
        self.program[op3] = (1 if op1 < op2 else 0)
        self.__update_pointer(self.counter + 4)

    def jump_true(self, params):
        condition, pointer, _ = self.__get_ops(params)
        pointer = (pointer if condition != 0 else self.counter + 3)
        self.__update_pointer(pointer)

    def jump_false(self, params):
        condition, pointer, _ = self.__get_ops(params)
        pointer = (pointer if condition == 0 else self.counter + 3)
        self.__update_pointer(pointer)

    def __get_ops(self, params):
        
        if params[0] == POS:
            op1 = self.program[self.program[self.counter + 1]]
        elif params[0] == REL:
            op1 = self.program[self.program[self.counter + 1] + self.relative]
        elif params[0] == IM:
            op1 = self.program[self.counter + 1]

        if params[1] == POS:
            op2 = self.program[self.program[self.counter + 2]]
        elif params[1] == REL:
            op2 = self.program[self.program[self.counter + 2] + self.relative]
        elif params[1] == IM:
            op2 = self.program[self.counter + 2]
        
        if params[2] == POS:
            op3 = self.program[self.counter + 3]
        elif params[2] == REL:
            op3 = self.program[self.counter + 3] + self.relative
        elif params[2] == IM:
            op3 = self.counter + 3

        return op1, op2, op3

    def __update_pointer(self, pointer):
        self.counter = pointer

    def run(self):
        while not self.finished:
            opcode, params = self.__instruction()
            if opcode == ADD:
                self.add(params)
            elif opcode == MUL:
                self.mul(params)
            elif opcode == LOAD:
                self.load(params)
            elif opcode == PRINT:
                self.print(params)
                if self.interrupt:
                    break
            elif opcode == JIT:
                self.jump_true(params)
            elif opcode == JIF:
                self.jump_false(params)
            elif opcode == EQUAL:
                self.equals(params)
            elif opcode == LESS:
                self.less(params)
            elif opcode == UREL:
                self.update_relative(params)
            elif opcode == END:
                self.finished = True
            
        return self.output
    
    def __instruction(self):
        opcode = self.program[self.counter]
        params = [0]*3
        if opcode == 99:
            return opcode, params

        operation = opcode % 10
        opcode = opcode // 100

        params[0] = opcode % 10
        opcode = opcode // 10

        params[1] = opcode % 10
        opcode = opcode // 10

        params[2] = opcode % 10
        opcode = opcode // 10

        return operation, params

    def set_value_at_index(self, index, value):
        self.program[index] = value

    def get_value_at_index(self, index):
        return self.program[index]

    def add_load_value(self, load_value):
        self.load_values.append(load_value)

    def reset(self):
        self.program = self.orig_program.copy()
        self.finished = False
        self.counter = 0
        self.output = 0
        self.load_values = []
