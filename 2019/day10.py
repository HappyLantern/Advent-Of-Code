
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
        detect_count = 0
        base    = {'x': station_location[0], 'y': station_location[1]} 
        astroid = {'x': 0, 'y': 0}
        between = {'x': 0, 'y': 0}

        for row in range(len(self.astroid_map)):
            for col in range(len(self.astroid_map[row])):

                astroid['x'] = row
                astroid['y'] = col

                if base['x'] == astroid['x'] and base['y'] == astroid['y']:
                    continue

                if self.astroid_map[astroid['x']][astroid['y']] == 0:
                    continue

                # Check if anything in the way of astroid and station
                in_the_way = False
                for row2 in range(len(self.astroid_map)):
                    for col2 in range(len(self.astroid_map[row2])):
                        between['x'] = col2
                        between['y'] = row2

                        if ((between['x'] == astroid['x'] and between['y'] == astroid['y']) or (between['x'] == base['x'] and between['y'] == base['y'])):
                            continue

                        if self.astroid_map[between['x']][between['y']] == 0:
                            continue

                        if self.is_between(base, astroid, between):
                            in_the_way = True
                
                if not in_the_way:
                    detect_count += 1
        return detect_count

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
        can_detect = []
        row = 0
        col = 0
        for row in range(len(self.astroid_map)):
           for col in range(len(self.astroid_map[row])):
                if self.astroid_map[row][col] == 0:
                   continue
                print(row, col)
                can_detect.append(self.__calc_detect_count([row, col]))

        return max(can_detect)


astroid_map = AstroidMap('day10_input.txt')
answer = astroid_map.find_best_location()
print(answer)