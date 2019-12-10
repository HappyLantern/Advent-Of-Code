from int_computer import IntComputer
from int_computer import read_input
import itertools

class Amplifier():

    def __init__(self, program):
        self.computer = IntComputer(program, interrupt=True)
        self.result   = 0
        self.phase    = -1

    def amplify(self, phase, inp):

        if self.phase == -1:
            self.phase = phase
            self.computer.add_load_value(phase)
        
        self.computer.add_load_value(inp)
        self.result = self.computer.run()

        return self.result
    
    def reset_amplifier(self):
        self.computer.reset()
        self.phase = -1

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
ans1 = series.part1(phases, init_input)

# PART 2
phases = [5, 6, 7, 8, 9]
ans2 = series.part2(phases, init_input)
print(ans1)
print(ans2)
