import aocd
import unittest
import sys
from missing import *

# UPDATE THESE BASED ON DAY AND DATA FROM ADVENT OF CODE 
DAY = 7
YEAR = 2024
TEST_DATA = [
    "190: 10 19",
    "3267: 81 40 27",
    "83: 17 5",
    "156: 15 6",
    "7290: 6 8 6 15",
    "161011: 16 10 13",
    "192: 17 8 14",
    "21037: 9 7 18 13",
    "292: 11 6 16 20"
]
TEST_A_ANSWER = 3749
TEST_B_ANSWER = 0
# 9160: 5 209 15 8 5

def perm(total, l:list, index=0):
    if l[len(l)-1] == l[index] and l[index] == total:
        return l[index]

    v1 = l[index]
    v2 = l[index]

    if l[index] * perm(total, l, index+1) == total:
        return l[index]
    if l[index] + perm(total, l, index+1) == total:
        return l[index]

    return perm(total, l, index+1)


def part_a(data):
    total = 292
    nums = [11, 6, 16, 20]

    print(perm(total, nums))




def part_b(data):
    ### *** your code here *** ###
    raise NotImplementedError



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
        part_a(TEST_DATA)
        
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