import aocd
import unittest
import sys
from missing import *
import copy

# UPDATE THESE BASED ON DAY AND DATA FROM ADVENT OF CODE 
DAY = 6
YEAR = 2024
TEST_DATA = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#...",
]
TEST_A_ANSWER = 41
TEST_B_ANSWER = 6

class Map:
    def __init__(self, data):
        self.barriers = {}
        self.map = data
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == "#":
                    self.barriers[(i,j)] = True
                else:
                    self.barriers[(i,j)] = False
        self.x_limit = len(data)
        self.y_limit = len(data[0])

    def is_barrier(self, coords:tuple):
        if (coords[0] >= self.x_limit) or (coords[0] < 0) or (coords[1] >= self.y_limit) or (coords[1] < 0):
            return False
        if self.barriers[coords]:
            return True
        else:
            return False
        
    def get_player_position(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == "^":
                    return (i,j)


class Player:
    def __init__(self, pos:tuple):
        self.direction = 0 # 0: north, 1: east, 2: south, 3: west
        self.position = pos # should be a tuple
        self.past_locations = [] # list of position tuples
        self.num_moves = 0

    def get_next_pos(self):
        x = self.position[0]
        y = self.position[1]
        next_pos = None
        match self.direction:
            case 0: # north
                x -= 1
                next_pos = (x,y)
            case 1: # east
                y += 1
                next_pos = (x,y)
            case 2: # south
                x += 1
                next_pos = (x,y)
            case 3: # west
                y -= 1
                next_pos = (x,y)
        return next_pos


    def move(self):
        x = self.position[0]
        y = self.position[1]
        self.num_moves += 1
        match self.direction:
            case 0: # north
                x -= 1
                self.position = (x,y)
            case 1: # east
                y += 1
                self.position = (x,y)
            case 2: # south
                x += 1
                self.position = (x,y)
            case 3: # west
                y -= 1
                self.position = (x,y)
        if self.num_moves > 10000: # this probably means its in a loop ¯\_(ツ)_/¯
            self.position = (10000,10000)
            # print("loop detected")
            return True

    def turn_right(self):
        self.direction = (self.direction + 1) % 4

    

def part_a(data):
    map = Map(data)
    p1 = Player(map.get_player_position())

    while p1.position[0] <= map.x_limit and p1.position[1] <= map.y_limit:
        # record the players current position
        if p1.position not in p1.past_locations:
            p1.past_locations.append(p1.position)
        if map.is_barrier(p1.get_next_pos()):
            p1.turn_right()
        else:
            p1.move()
    cnt = len(p1.past_locations) - 1 # the past locations includes the space outside the map
    print(cnt)
    return cnt




def part_b(data):
    
    cnt = 0
    # go through every iteration
    for i in range(len(data)):
        for j in range(len(data[0])):
            new_data = copy.deepcopy(data)
            if new_data[i][j] == '^':
                continue
            if new_data[i][j] != '#':
                new_data[i] = new_data[i][:j] + '#' + new_data[i][j+1:]
            map = Map(new_data)
            p1 = Player(map.get_player_position())

            while p1.position[0] <= map.x_limit and p1.position[0] >= 0 and p1.position[1] <= map.y_limit and p1.position[1] >= 0:
                # record the players current position
                if p1.position not in p1.past_locations:
                    p1.past_locations.append(p1.position)
                if map.is_barrier(p1.get_next_pos()):
                    p1.turn_right()
                else:
                    l = p1.move()
                    if l:
                        cnt += 1

    return cnt
            



################# UNIT TESTS #################
class Test(unittest.TestCase):
    def testA(self):
        self.assertEqual(part_a(TEST_DATA), TEST_A_ANSWER)

    def testB(self):
        self.assertEqual(part_b(TEST_DATA), TEST_B_ANSWER)


############### DATA RETRIEVAL ###############
if TEST_DATA == None or DAY == None:
    raise MissingFieldsError("Missing puzzle data! make sure you have updated the following: `DAY`, `TEST_DATA`, `TEST_A_DATA`, `TEST_B_DATA`")
data = aocd.get_data(day=DAY, year=2024)
data_as_list = data.split("\n")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        sys.argv = [sys.argv[0]] # unittest uses the system args to run so it has to be cleared :/
        unittest.main()
    elif len(sys.argv) > 1 and sys.argv[1] == '-ta':
        suite = unittest.TestLoader().loadTestsFromName("day" + str(DAY) + ".Test.testA")
        unittest.TextTestRunner().run(suite)
    elif len(sys.argv) > 1 and sys.argv[1] == '-tb':
        suite = unittest.TestLoader().loadTestsFromName("day" + str(DAY) + ".Test.testB")
        unittest.TextTestRunner().run(suite)
    elif len(sys.argv) > 1 and sys.argv[1] == '-s':
        aocd.submit(part_a(data_as_list), part='a', day=DAY, year=YEAR)
        aocd.submit(part_b(data_as_list), part='b', day=DAY, year=YEAR)
    elif len(sys.argv) > 1 and sys.argv[1] == '-sa':
        aocd.submit(part_a(data_as_list), part='a', day=DAY, year=YEAR)
    elif len(sys.argv) > 1 and sys.argv[1] == '-sb':
        aocd.submit(part_b(data_as_list), part='b', day=DAY, year=YEAR)
    elif len(sys.argv) > 1 and sys.argv[1] == '-d':
        print("-------BEGIN DEBUGGING MODE-------")
        print()

        # do any debugging code here :)
        part_b(TEST_DATA)
        
        print()
        print("----------END DEBUGGING-----------")
    else:
        print("Missing or in correct arguments! Usage:")
        print("python aoc2023/day_.py -t  -- for testing both parts a & b")
        print("python aoc2023/day_.py -ta -- for testing only part a")
        print("python aoc2023/day_.py -tb -- for testing only part b")
        print("python aoc2023/day_.py -s  -- submit both parts a & b")
        print("python aoc2023/day_.py -sa -- submit only part a")
        print("python aoc2023/day_.py -sb -- submit only part b")

if __name__ == "__main__":
    main()