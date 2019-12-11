import numpy as np
from math import acos
from math import sqrt
from math import pi

class AstroidMap():

    def __init__(self, map_input):
        self.map_input = map_input
        self.astroid_map = []
        self.detect_angles = dict()
        self.best_location = []
        self.num_astroids = 0
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
                    self.num_astroids += 1
                    
            self.astroid_map.append(map_row)
        self.astroid_map = np.array(self.astroid_map)
        self.astroid_map = np.moveaxis(self.astroid_map, 0, 1)
        print(self.astroid_map, self.num_astroids)

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

    def __angle_between(self, p1, p2):
        ang1 = np.arctan2(*p1[::-1])
        ang2 = np.arctan2(*p2[::-1])
        angle = np.rad2deg((ang1 - ang2) % (2 * np.pi)) + 90
        angle = 360 - angle
        if angle >= 360:
            angle = angle % 360
        elif angle < 0:
            angle = angle + 360
        
        return angle

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
                        between['x'] = row2
                        between['y'] = col2

                        if ((between['x'] == astroid['x'] and between['y'] == astroid['y']) or (between['x'] == base['x'] and between['y'] == base['y'])):
                            continue

                        if self.astroid_map[between['x']][between['y']] == 0:
                            continue

                        if self.is_between(base, astroid, between):
                            in_the_way = True
                
                if not in_the_way:
                    angle = self.__angle_between((0, 0), (base['x'] - astroid['x'], base['y'] - astroid['y']))
                    self.detect_angles[angle] = [astroid['x'], astroid['y']]
                    detect_count += 1
                
        return detect_count
    
    def find_best_location(self):
        can_detect = []
        station_pos = []
        row = 0
        col = 0
        for row in range(len(self.astroid_map)):
           for col in range(len(self.astroid_map[row])):
                if self.astroid_map[row][col] == 0:
                   continue
                print(row, col)
                can_detect.append(self.__calc_detect_count([row, col]))
                station_pos.append((row, col))

        self.best_location = station_pos[can_detect.index(max(can_detect))]

        return max(can_detect), self.best_location

    def __vaporize_astroid(self, astroid):
        self.num_astroids -= 1
        self.astroid_map[astroid[0]][astroid[1]] = 0

    def vaporize_astroids(self, vaporize, station_pos = None):

        self.detect_angles = dict()

        if station_pos != None:
            self.best_location = station_pos

        angles = []
        angles.sort() # Order to vaporize
        vaporize_count = 0
        astroid = []

        while vaporize_count < vaporize:

            if len(angles) == 0 and self.num_astroids > 1:
                print("FILLING")
                self.__calc_detect_count(self.best_location)
                angles = [key for key, value in self.detect_angles.items()]
                angles.sort()

            if self.num_astroids == 1:
                print("No astroids left to vaporize")
                break

            angle = angles.pop(0)
            astroid = self.detect_angles[angle]
            self.detect_angles.pop(angle)

            vaporize_count += 1
            print(vaporize_count, "Astroid to vaporize at angle:", angle, astroid)
            self.__vaporize_astroid(astroid)

            if vaporize_count == vaporize:
                return astroid[0] * 100 + astroid[1]

astroid_map = AstroidMap('day10_input.txt')

# PART 1
#answer = astroid_map.find_best_location()
#print(answer[0], answer[1])

# PART 2
answer = astroid_map.vaporize_astroids(vaporize=200, station_pos = (19, 14))
print(answer)