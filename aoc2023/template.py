import aocd
import unittest
import sys
from missing import *

# UPDATE THESE BASED ON DAY AND DATA FROM ADVENT OF CODE 
DAY = 0
TEST_DATA = None
TEST_A_ANSWER = None
TEST_B_ANSWER = None



def part_a(data):
    ### *** your code here *** ###
    raise NotImplementedError


def part_b(data):
    ### *** your code here *** ###
    raise NotImplementedError



################# UNIT TESTS #################
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(part_a(TEST_DATA), 0)
        self.assertEqual(part_b(TEST_DATA), 0)


############### DATA RETRIEVAL ###############
if TEST_DATA == None or TEST_A_ANSWER == None or TEST_A_ANSWER == None or DAY == 0:
    raise MissingFieldsError("Missing puzzle data! make sure you have updated the following: `DAY`, `TEST_DATA`, `TEST_A_DATA`, `TEST_B_DATA`")
data = aocd.get_data(day=DAY, year=2023)
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
        aocd.submit(part_a(data_as_list), part='a', day=DAY, year=2023)
        aocd.submit(part_b(data_as_list), part='b', day=DAY, year=2023)
    elif len(sys.argv) > 1 and sys.argv[1] == '-sa':
        aocd.submit(part_a(data_as_list), part='a', day=DAY, year=2023)
    elif len(sys.argv) > 1 and sys.argv[1] == '-sb':
        aocd.submit(part_b(data_as_list), part='b', day=DAY, year=2023)
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