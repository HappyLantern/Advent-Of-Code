def read_input(file):
    input = open(file, 'r')
    input = input.read().strip().split('\n')
    return input

class Orbit():
    def __init__(self, name, orbit):
        self.name = name
        self.orbit = orbit
        self.path_to = []
    
    def add_path(self, orbit):
        self.path_to.append(orbit)

class OrbitMap():
    def __init__(self, input):
        self.orbit_map = dict()
        self.input = input
        self.orbit_sum = 0
        self.santa_path = 0

    def __add_orbits_to_map(self, name, orbit):

        if name not in self.orbit_map:
            self.orbit_map[name] = Orbit(name, orbit)
        else:
            self.orbit_map[name].orbit = orbit
        if orbit not in self.orbit_map:
            self.orbit_map[orbit] = Orbit(orbit, '')
        self.orbit_map[orbit].add_path(name)
        
    def build_orbit_map(self):
        for orbit in self.input:
            orbit = orbit.split(')')
            self.__add_orbits_to_map(orbit[1], orbit[0])            

    def part1(self):
        for obj in self.orbit_map:
            #print(self.orbit_map[obj].path_to)
            while obj != 'COM':
                self.orbit_sum += 1
                obj = self.orbit_map[obj].orbit

    def find_matching_index(self, list1, list2):

        inverse_index = { element: index for index, element in enumerate(list1) }

        return [(index, inverse_index[element])
            for index, element in enumerate(list2) if element in inverse_index]
    
    def part2(self):
        path_1 = []
        path_2 = []

        start = self.orbit_map['YOU']
        goal  = self.orbit_map['SAN']

        while start.name != 'COM':
            start = self.orbit_map[start.orbit]
            path_1.append(start.name)
        
        while goal.name != 'COM':
            goal = self.orbit_map[goal.orbit]
            path_2.append(goal.name)

        matches = self.find_matching_index(path_1, path_2)
        travel_dist = matches[0][0] + matches[0][1]
        return travel_dist
        
orbit_map = read_input('day6_input.txt')
orbit_map = OrbitMap(orbit_map)
orbit_map.build_orbit_map()
orbit_map.part1()
print(orbit_map.orbit_sum)
ans = orbit_map.part2()
print(ans)






    

