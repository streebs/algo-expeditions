import aocd
import unittest
import sys
from missing import *

# UPDATE THESE BASED ON DAY AND DATA FROM ADVENT OF CODE 
DAY = 2
YEAR = 2024
TEST_DATA = [
    "7 6 4 2 1",
    "1 2 7 8 9",
    "9 7 6 2 1",
    "1 3 2 4 5",
    "8 6 4 4 1",
    "1 3 6 7 9",
]
TEST_A_ANSWER = 2
TEST_B_ANSWER = 4

def is_easing(levels):
    # ensure that the numbers in levels are either increasing or decreasing
    if sorted(levels) == levels or sorted(levels, reverse=True) == levels:
        return True
    else:
        return False
    

def is_nominal(levels):
    # make sure that the numbers in levels are at least 1 and at most 3 apart.
    for i in range(1, len(levels)):
        diff = abs(levels[i] - levels[i-1])
        if diff >= 1 and diff <= 3:
            continue
        else:
            return False
        
    return True

def dampener(levels: list):
    # this will check if the levels are safe by removing one of the inputs (for all inputs)

    current_removed_index = 0
    for i in range(len(levels)):
        removed_value = levels.pop(current_removed_index)
        if is_easing(levels) and is_nominal(levels):
            return True
        else:
            levels.insert(current_removed_index, removed_value)
            current_removed_index += 1
            continue

    return False


def part_a(data):

    tests = []
    
    for line in data:
        levels = [int(i) for i in line.split()]
        if is_easing(levels) and is_nominal(levels):
            tests.append(1)
        else:
            tests.append(0)

    return tests.count(1)
        


def part_b(data):
    tests = []
    
    for line in data:
        levels = [int(i) for i in line.split()]
        if is_easing(levels) and is_nominal(levels):
            tests.append(1)
        else:
            if dampener(levels):
                tests.append(1)
            else:
                tests.append(0)

    return tests.count(1)



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
        print(part_b(TEST_DATA))
        
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