import aocd
import unittest
import sys

# instead of looking for edge cases in the input (i.e. numbers that occur on the edges) lets pad the edges
# this function adds an array of periods to the top and bottom and the left and righ columns
# remember that i will be adding 2 periods to the front and back of each row which means the top and
# bottom rows will need 2 additional periods.
def addPadding(array):
    new_array = array
    # create the top/bottom row dont put them in the array till the end
    row = '.' * (len(array[0]) + 2)
    topBottomRow =  [*row]

    # add periods to the sides
    for lst in new_array:
        lst.insert(0, '.')
        lst.append('.')

    # add periods to the top and bottom
    new_array.insert(0, topBottomRow)
    new_array.append(topBottomRow)

    return new_array

    

def findNeighbors(lastDigitI, lastDigitJ, numType, array):
    neighbors = []
    if numType == 1:
        for i in range(lastDigitI-1, lastDigitI+2):
            for j in range(lastDigitJ-1, lastDigitJ+2):
                neighbors.append(array[i][j]) 
    if numType == 2:
        for i in range(lastDigitI-1, lastDigitI+2):
            for j in range(lastDigitJ-2, lastDigitJ+2):
                neighbors.append(array[i][j]) 
    if numType == 3:
        for i in range(lastDigitI-1, lastDigitI+2):
            for j in range(lastDigitJ-3, lastDigitJ+2):
                # print(f"i: {i}")
                # print(f"j: {j}")
                neighbors.append(array[i][j])

    for neighbor in neighbors:
        if neighbor != '.' and not neighbor.isdigit():
            return True
    return False 

# functions takes a 2-d array
def part_a(data_as_list):
    
    engineParts = []

    numStack = []
    numType = 0

    for i in range(0, len(data_as_list)):
        for j in range(0, len(data_as_list[i])):
            if data_as_list[i][j].isdigit():
                numStack.append(data_as_list[i][j])
                numType += 1
            if not data_as_list[i][j].isdigit() and numType != 0 and numStack != []:
                num = int(''.join(numStack))
                if (findNeighbors(i, j-1, numType, data_as_list)):
                    engineParts.append(num)
                numStack = []
                numType = 0

    return sum(engineParts)

class Gear:
    def __init__(self, position : tuple):
        self.position = position
        self.neighbors = []
        self.ratio = 0
    
    def compute(self):
        if len(self.neighbors) >= 2:
            return self.neighbors[0] * self.neighbors[1]
        else:
            return 0

def findGearNeighbor(lastDigitI, lastDigitJ, numType, array):
    gearNeighborLocation = ''
    if numType == 1:
        for i in range(lastDigitI-1, lastDigitI+2):
            for j in range(lastDigitJ-1, lastDigitJ+2):
                if array[i][j] == "*":
                    gearNeighborLocation = (i,j)
    if numType == 2:
        for i in range(lastDigitI-1, lastDigitI+2):
            for j in range(lastDigitJ-2, lastDigitJ+2):
                if array[i][j] == "*":
                    gearNeighborLocation = (i,j) 
    if numType == 3:
        for i in range(lastDigitI-1, lastDigitI+2):
            for j in range(lastDigitJ-3, lastDigitJ+2):
                if array[i][j] == "*":
                    gearNeighborLocation = (i,j)
    
    return gearNeighborLocation
def part_b(data):

    # create and fill gearTable
    gearTable = {}
    gearRatios = []

    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            if data[i][j] == '*':
                gearTable[(i,j)] = Gear((i,j))

    #find numbers in the array and look for gear neighbors
    numStack = []
    numType = 0
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            if data[i][j].isdigit():
                numStack.append(data[i][j])
                numType += 1
            if not data[i][j].isdigit() and numType != 0 and numStack != []:
                num = int(''.join(numStack))
                if findGearNeighbor(i, j-1, numType, data) != '':
                    gearTable[findGearNeighbor(i, j-1, numType, data)].neighbors.append(num)
                numStack = []
                numType = 0

    # compute gear ratios and put them in a list
    for gear in gearTable:
        gearRatios.append(gearTable[gear].compute()) 

    return sum(gearRatios) 




################# UNIT TESTS #################
test_data = [
    list("467..114.."),
    list("...*......"),
    list("..35..633."),
    list("......#..."),
    list("617*......"),
    list(".....+.58."),
    list("..592a...."),
    list(".....a755."),
    list("...$.*...."),
    list(".664.598..")
]

test_data = addPadding(test_data)

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(part_a(test_data), 4361)
        self.assertEqual(part_b(test_data), 467835)
        


############### DATA RETRIEVAL ###############
data = aocd.get_data(day=3, year=2023)
data_as_list = data.split("\n")
#put data in 2-d array
engine = []
for line in data_as_list:
    engine.append([*line])
engine = addPadding(engine)

# print(engine)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        sys.argv = [sys.argv[0]] # unittest uses the system args to run so it has to be cleared :/
        unittest.main()
    else:
        aocd.submit(part_a(engine), part='a', day=3, year=2023)
        aocd.submit(part_b(engine), part='b', day=3, year=2023)

if __name__ == "__main__":
    main()