import aocd
import unittest
import sys
from missing import *
import math

# UPDATE THESE BASED ON DAY AND DATA FROM ADVENT OF CODE 
DAY = 2
YEAR = 2025
TEST_RAW = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
TEST_DATA_RANGES = TEST_RAW.split(",")
TEST_DATA = [(int(value.split("-")[0]), int(value.split("-")[1])) for value in TEST_DATA_RANGES]
TEST_A_ANSWER = 1227775554
TEST_B_ANSWER = 4174379265

digits_and_divisors = {2:11, 4:101, 6:1_001, 8:10_001, 10:100_001, 12:1_000_001}
composite_odds_and_divisors = {9:1_001_001, 15:1_001_001_001_001}
small_primes = [2,3,5,7,11,13]

def part_a(data):
    ### *** your code here *** ###
    total = 0
    for interval in data:
        start = interval[0]
        end = interval[1]
        for i in range(start, end+1):
            if (len(str(i)) % 2 != 0):
                continue
            if (i % digits_and_divisors[len(str(i))] == 0):
                total += i
    return total


def part_b(data):
    total = 0
    for interval in data:
        start = interval[0]
        end = interval[1]
        for i in range(start, end+1):
            num_digits = len(str(i))
            if num_digits in small_primes and str(i) == str(i)[0]*num_digits:
                total += 1
                continue
            if (num_digits == 9 or num_digits == 15) and (i % composite_odds_and_divisors[num_digits] == 0): # composite odd numbers (should only need 9 and 15 for current dataset)
                total += 1
                continue
            if num_digits % 2 == 0 and i % digits_and_divisors[num_digits]:
                total += 1

    return total




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
ranges_as_list = data.split(",")
data_as_list = [(int(value.split("-")[0]), int(value.split("-")[1])) for value in ranges_as_list]


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

        print(data_as_list)
        
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