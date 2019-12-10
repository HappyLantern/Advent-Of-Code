
class AstroidMap():

    def __init__(self, map_input):
        self.map_input = map_input
        self.astroid_map = []
        self.__create_map()

    def __create_map(self):
        inp = open(self.map_input, 'r')
        for row in inp:
            map_row = []
            for pos in row:

                if pos == '.':
                    map_row.append(0)
                elif pos == '#':
                    map_row.append(1)
            self.astroid_map.append(map_row)

    def __calc_detect_count(self, station_location):
        station_location = [3, 4]
        detect_count = 0
        base    = {'x': station_location[0], 'y': station_location[1]} 
        astroid = {'x': 0, 'y': 0}
        between = {'x': 0, 'y': 0}

        for row in range(len(self.astroid_map)):
            for col in range(len(self.astroid_map[row])):

                if row == a['x'] and a['y'] == col:
                    continue
                astroid['x'] = row
                astroid['y'] = col

            for row2 in range(len(self.astroid_map)):
                for col2 in range(len(self.astroid_map[row2])):
                    if (row2 == rol and col2 == col) or row2 == base['x'] and col2 == base['y']:
                        continue

                        detect_count += 1

        print(detect_count)

    def is_between(self, a, b, c):
        crossproduct = (c['y'] - a['y']) * (b['x']- a['x']) - (c['x'] - a['x']) * (b['y'] - a['y'])

        if abs(crossproduct) != 0:
            return False

        dotproduct = (c['x'] - a['x']) * (b['x'] - a['x']) + (c['y'] - a['y'])*(b['y'] - a['y'])
        if dotproduct < 0:
            return False

        squaredlengthba = (b['x'] - a['x'])*(b['x'] - a['x']) + (b['y'] - a['y'])*(b['y'] - a['y'])
        if dotproduct > squaredlengthba:
            return False

        return True
    
    def find_best_location(self):
        can_detect = dict()
        row = 0
        col = 0
        #for row in range(len(self.astroid_map)):
           # for col in range(len(self.astroid_map[row])):
        can_detect[(row, col)] = self.__calc_detect_count([row, col])

        print(self.astroid_map)

astroid_map = AstroidMap('day10_input.txt')
astroid_map.find_best_location()
        

