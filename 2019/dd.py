HORIZONTAL = 1
VERTICAL = 2

def getFileContent(fileName, returnNumber, individualChars, firstSplit="", secondSplit=""):
    #   Converts file into lists of strings or integers
    #   IndividualChars can only be combined with returnNumber or firstSplit, not both and not secondSplit (lazy patch)
    #   Load file
    inputFile = open(fileName, "r")
    content = inputFile.read()
    inputFile.close()

    #   Replace characters if splits is list
    if not isinstance(firstSplit, str):
        for letter in firstSplit:
            content = content.replace(letter, firstSplit[0])
        firstSplit = firstSplit[0]
    if not isinstance(secondSplit, str):
        for letter in secondSplit:
            content = content.replace(letter, secondSplit[0])
        secondSplit = secondSplit[0]

    #   If "individualChars" split the string into chars
    if individualChars:
        ret = list(content)
        if firstSplit != "":
            content = list(filter(None, content.split(firstSplit)))
            ret = []
            for row in content:
                ret.append(list(row))
            return ret
        if returnNumber:
            ret = list(map(int, list(filter(filterNumbers, ret))))
        return ret

    #   Split the string by "firstSplit" if defined
    if firstSplit != "":
        if returnNumber and secondSplit == "":
            content = list(map(int, list(filter(filterNumbers, content.split(firstSplit)))))
        else:
            content = list(filter(None, content.split(firstSplit)))

    #   Split each string by "secondSplit" if defined
    if secondSplit != "":
        ret = []
        for row in content:
            if returnNumber:
                ret.append(list(map(int, list(filter(filterNumbers, row.split(secondSplit))))))
            else:
                ret.append(list(filter(None, row.split(secondSplit))))
    else:
        ret = content
    return ret

class Line:
    def __init__(self, x1, x2, y1, y2, steps):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.steps = steps
        if x1 == x2:
            self.direction = VERTICAL
        else:
            self.direction = HORIZONTAL

    def stepsAtEnd(self):
        return self.steps + abs(self.x2 - self.x1) + abs(self.y2 - self.y1)


class BentLine:
    def __init__(self):
        self.lines = []
        self.x = 0
        self.y = 0
        self.steps = 0

    def addLine(self, command):
        direction = [command[:1], command[1:]]
        newX = self.x
        newY = self.y
        if direction[0] == "R":
            newX += int(direction[1])
        if direction[0] == "L":
            newX -= int(direction[1])
        if direction[0] == "D":
            newY += int(direction[1])
        if direction[0] == "U":
            newY -= int(direction[1])
        self.lines.append(Line(self.x, newX, self.y, newY, self.steps))
        self.x = newX
        self.y = newY
        self.steps = self.lines[len(self.lines)-1].stepsAtEnd()

    def print(self):
        for line in self.lines:
            print("({}, {})-({}, {})".format(line.x1, line.y1, line.x2, line.y2))

    def collision(self, other):
        collisions = []
        for l1 in self.lines:
           # self.print()
            for l2 in other.lines:
                if (l1.direction == HORIZONTAL and l2.direction == VERTICAL and
                        ((l1.x1 <= l2.x1 <= l1.x2) or (l1.x1 >= l2.x1 >= l1.x2)) and
                        ((l2.y1 <= l1.y1 <= l2.y2) or (l2.y1 >= l1.y1 >= l2.y2))):
                    l1Dist = l1.steps + abs(l1.x1 - l2.x1)
                    l2Dist = l2.steps + abs(l2.y1 - l1.y1)
                    collisions.append([l2.x1, l1.y1, l1Dist + l2Dist])
                if (l1.direction == VERTICAL and l2.direction == HORIZONTAL and
                        ((l2.x1 <= l1.x1 <= l2.x2) or (l2.x1 >= l1.x1 >= l2.x2)) and
                        ((l1.y1 <= l2.y1 <= l1.y2) or (l1.y1 >= l2.y1 >= l1.y2))):
                    l1Dist = l1.steps + abs(l1.y1 - l2.y1)
                    l2Dist = l2.steps + abs(l2.x1 - l1.x1)
                    collisions.append([l1.x1, l2.y1, l1Dist + l2Dist])
        return collisions


def part1():
    fileInput = getFileContent("day3_input.txt", False, False, "\n", ",")
    directions = []
    line = [BentLine(), BentLine()]
    for d in range(2):
        directions.append([])
        for point in range(len(fileInput[d])):
            line[d].addLine(fileInput[d][point])
    col = line[0].collision(line[1])
    minDist = 99999999999
    for c in col:
        minDist = min(minDist, abs(c[0]) + abs(c[1]))
    print("Part 1: Closest distance is {}".format(minDist))


def part2():
    fileInput = getFileContent("day3_input.txt", False, False, "\n", ",")
    directions = []
    line = [BentLine(), BentLine()]
    for d in range(2):
        directions.append([])
        for point in range(len(fileInput[d])):
            line[d].addLine(fileInput[d][point])
    col = line[0].collision(line[1])
    minDist = 99999999999
    for c in col:
        minDist = min(minDist, c[2])
    print("Part 2: Closest distance is {}".format(minDist))

part1()
part2()