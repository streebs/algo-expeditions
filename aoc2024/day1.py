import aocd
import unittest
import sys
from missing import *

# UPDATE THESE BASED ON DAY AND DATA FROM ADVENT OF CODE 
DAY = 1
YEAR = 2024
TEST_DATA = [
    "3   4",
    "4   3",
    "2   5",
    "1   3",
    "3   9",
    "3   3"
]
TEST_A_ANSWER = 11
TEST_B_ANSWER = 31



def part_a(data):
    left_list = []
    right_list = []

    for line in data:
        entry_pair = line.split()
        left_list.append(entry_pair[0].strip())
        right_list.append(entry_pair[1].strip())

    left_list = sorted(left_list)
    right_list = sorted(right_list)

    distances = [abs(int(right_list[i]) - int(left_list[i])) for i in range(len(left_list))]

    return sum(distances)



def part_b(data):
    left_list = []
    right_list = []

    for line in data:
        entry_pair = line.split()
        left_list.append(int(entry_pair[0].strip()))
        right_list.append(int(entry_pair[1].strip()))

    similarity_list = []
    for i in range(len(left_list)):
        count = right_list.count(left_list[i])
        similarity_list.append(left_list[i] * count)

    return sum(similarity_list)



################# UNIT TESTS #################
class Test(unittest.TestCase):
    def testA(self):
        self.assertEqual(part_a(TEST_DATA), TEST_A_ANSWER)

    def testB(self):
        self.assertEqual(part_b(TEST_DATA), TEST_B_ANSWER)


############### DATA RETRIEVAL ###############
if TEST_DATA == None or DAY == 0:
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