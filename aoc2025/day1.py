import aocd
import unittest
import sys
from missing import *

# UPDATE THESE BASED ON DAY AND DATA FROM ADVENT OF CODE 
DAY = 1
YEAR = 2025
TEST_DATA = [
    'L68',
    'L30',
    'R48',
    'L5',
    'R60',
    'L55',
    'L1',
    'L99',
    'R14',
    'L82',
]
TEST_A_ANSWER = 3
TEST_B_ANSWER = 6



def part_a(data):
    current_number = 50
    total_zero = 0
    for inst in data:
        op = '+'
        direction = inst[0]
        value = int(inst[1:])

        if direction == 'L':
            op = '-'
        elif direction == 'R':
            op = '+'
        else:
            raise Exception(f'could not parse direction | {inst}')
        
        if op == '-':
            current_number = (current_number - value) % 100
        if op == '+':
            current_number = (current_number + value) % 100

        if current_number == 0:
            total_zero += 1

    return total_zero

def part_b(data):
    current_number = 50
    total_zero = 0
    for inst in data:

        direction = inst[0]
        value = int(inst[1:])
        
        if direction == 'L':
            counter = 0
            while True:
                if current_number == 0:
                    total_zero += 1

                current_number -= 1
                counter += 1
                if current_number < 0:
                    current_number = 99
                    # total_zero += 1
                if counter == value:
                    break
        elif direction == 'R':               
            counter = 0
            while True:
                if current_number == 0:
                    total_zero += 1
                    
                current_number += 1
                counter += 1
                if current_number > 99:
                    current_number = 0
                    # total_zero += 1
                if counter == value:
                    break
        else:
            raise Exception(f'error parsing direction | {inst}')

    return total_zero



################# UNIT TESTS #################
class Test(unittest.TestCase):
    def testA(self):
        self.assertEqual(part_a(TEST_DATA), TEST_A_ANSWER)

    def testB(self):
        self.assertEqual(part_b(TEST_DATA), TEST_B_ANSWER)


############### DATA RETRIEVAL ###############
if TEST_DATA == None or DAY == None:
    raise MissingFieldsError("Missing puzzle data! make sure you have updated the following: `DAY`, `TEST_DATA`, `TEST_A_DATA`, `TEST_B_DATA`")
data = aocd.get_data(day=DAY, year=YEAR)
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

        print(part_b(data_as_list))
        
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