from int_computer import IntComputer
from int_computer import read_input
import numpy as np
import matplotlib.pyplot


BLACK = 0
WHITE = 1
LEFT = 0
RIGHT = 1

# AT LOAD INSTRUCTION
# LOAD 0 IF ON BLACK PANEL
# LOAD 1 IF ON WHITE PANEL

# AT PRINT INSTRUCTION 1
# PRINTS 0 IF PAINT BLACK
# PRINTS 1 IF PAINT WHITE

# AT PRINT INSTRUCTION 2
# PRINTS 0 IF LEFT 90 DEGREES
# PRINTS 1 IF RIGHT 90 DEGREES

# AFTER ROBOT TURNS -> MOVE 1 STEP FORWARD

class PaintRobot():

    def __init__(self, program):
        print("SETTING UP ROBOT")
        self.computer = IntComputer(program, interrupt=True)
        self.panel = np.zeros((100, 100))
        self.unique_locations = dict()

    def paint_panel(self):

        robot = [len(self.panel) // 2, len(self.panel) // 2]
        robot_direction = 'UP'
        self.unique_locations[repr(robot)] = 1
        
        print("STARTING ROBOT", robot)
        start_color = WHITE
        self.computer.add_load_value(WHITE)
        print(robot, robot_direction)
        while not self.computer.finished:

            color = self.computer.run()
            turn = self.computer.run()
            self.panel[robot[0]][robot[1]] = color

            if turn == RIGHT:
                if robot_direction == 'UP':
                    robot[0] += 1
                    robot_direction = 'RIGHT'
                elif robot_direction == 'DOWN':
                    robot[0] -= 1
                    robot_direction = 'LEFT'
                elif robot_direction == 'RIGHT':
                    robot[1] -= 1
                    robot_direction = 'DOWN'
                elif robot_direction == 'LEFT':
                    robot[1] += 1
                    robot_direction = 'UP'
            
            elif turn == LEFT:
                if robot_direction == 'UP':
                    robot[0] -= 1
                    robot_direction = 'LEFT'
                elif robot_direction == 'DOWN':
                    robot[0] += 1
                    robot_direction = 'RIGHT'
                elif robot_direction == 'RIGHT':
                    robot[1] += 1
                    robot_direction = 'UP'
                elif robot_direction == 'LEFT':
                    robot[1] -= 1
                    robot_direction = 'DOWN'

            curr_color = self.panel[robot[0]][robot[1]]
            self.computer.add_load_value(curr_color)

            print("Current panel color:", curr_color)
            print("Paint:", color, "Turn: ", ('LEFT' if turn == 0 else 'RIGHT'))
            print(robot, robot_direction)

            if repr(robot) not in self.unique_locations:
                self.unique_locations[repr(robot)] = 1

        keys = [key for key, value in self.unique_locations.items()]
        return len(keys)

    def save_panel(self):
        matplotlib.pyplot.imsave('day11_message.png', self.panel)
program = read_input('day11_input.txt')
program.extend([0] * 100000) # Lengthen for more memory

robot = PaintRobot(program)
unique_locations = robot.paint_panel()
robot.save_panel()
print(unique_locations)