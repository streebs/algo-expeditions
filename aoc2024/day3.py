import aocd
import unittest
import sys
from missing import *

import re
# UPDATE THESE BASED ON DAY AND DATA FROM ADVENT OF CODE 
DAY = 3
YEAR = 2024
TEST_DATA = [
    "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
]
TEST_DATA_B = [
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
]
TEST_A_ANSWER = 161
TEST_B_ANSWER = 48


def part_a(data):
    pattern = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
    products = []
    for line in data:
        valid_muls = re.findall(pattern, line)
        for mul in valid_muls:
            mul = mul[4:]
            mul = mul[:-1]
            nums = mul.split(',')
            products.append(int(nums[0]) * int(nums[1]))
    
    return sum(products)


def part_b(data):
    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"
    products = []
    state = True
    for line in data:
        valid_muls = re.findall(pattern, line)
        for mul in valid_muls:
            if mul == 'do()':
                state = True
            if mul == "don't()":
                state = False
            if mul != 'do()' and mul != "don't()" and state:
                mul = mul[4:]
                mul = mul[:-1]
                nums = mul.split(',')
                products.append(int(nums[0]) * int(nums[1]))
    
    return sum(products)




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
        print(part_b(TEST_DATA_B))
        
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