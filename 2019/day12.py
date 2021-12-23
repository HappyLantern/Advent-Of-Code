import re
import itertools
class MoonTracker():

    def __init__(self, inp):
        self.moon_positions = []
        self.__init_moons(inp)
        self.moon_velocities = [(0 , 0, 0) for i in range(len(self.moon_positions))]
        self.moon_pairs = list(itertools.combinations([i for i in range(len(self.moon_positions))], 2))
        print(self.moon_positions)
        print(self.moon_velocities)
        print(self.moon_pairs)

    def __init_moons(self, inp):

        for line in inp:
            x, y, z = re.findall('-?\d+', line)
            moon = (x, y, z)
            self.moon_positions.append(moon)

        print(self.moon_positions)

    def __time_step(self):

        for moon_pair in self.moon_pairs:
            moon1 = moon_pair[0]
            moon2 = moon_pair[1]

            if self.moon_positions[moon1][0] > self.moon_positions[moon2][0]:
                self.moon_velocities[moon1][0] += 1
                self.moon_velocities[moon2][0] -= 1
            else:
                self.moon_velocities[moon1][0] -= 1
                self.moon_velocities[moon2][0] += 1

            if self.moon_positions[moon1][1] > self.moon_positions[moon2][1]:
                self.moon_velocities[moon1][1] += 1
                self.moon_velocities[moon2][1] -= 1
            else:
                self.moon_velocities[moon1][1] -= 1
                self.moon_velocities[moon2][1] += 1

            if self.moon_positions[moon1][2] > self.moon_positions[moon2][2]:
                self.moon_velocities[moon1][2] += 1
                self.moon_velocities[moon2][2] -= 1
            else:
                self.moon_velocities[moon1][2] -= 1
                self.moon_velocities[moon2][2] += 1
            
        for moon in range(len(self.moon_positions)):
            self.moon_positions[moon][0] += self.moon_velocities[moon][0]
            self.moon_positions[moon][1] += self.moon_velocities[moon][1]
            self.moon_positions[moon][2] += self.moon_velocities[moon][2]


inp = open('day12_input.txt', 'r')
moon_tracker = MoonTracker(inp)



