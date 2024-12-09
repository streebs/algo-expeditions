import aocd
import unittest
import sys
from missing import *

# UPDATE THESE BASED ON DAY AND DATA FROM ADVENT OF CODE 
DAY = 5
YEAR = 2024
TEST_DATA = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",

    "75,47,61,53,29",
    "97,61,53,29,13",
    "75,29,13",
    "75,97,47,61,53",
    "61,13,29",
    "97,13,75,29,47",
]
TEST_A_ANSWER = 143
TEST_B_ANSWER = 0

class Manual:
    def __init__(self, input: list[str]):
        self.rules = []
        self.pages = []
        self.incorrect = []

        for line in input:
            if line == '':
                continue
            if '|' in line:
                values = line.split('|')
                self.rules.append((int(values[0]), int(values[1])))
            else:
                values = line.split(',')
                values = [int(i) for i in values]
                self.pages.append(values)

    def check_rules(self, line: list[int]):
        for rule in self.rules:
            before = rule[0]
            after = rule[1]
            if before in line and after in line and line.index(before) < line.index(after):
                continue
            elif before not in line or after not in line:
                continue
            else:
                return False
        return True

    def get_sum_of_passed_tests(self):
        passed = []
        for line in self.pages:
            if self.check_rules(line):
                passed.append(line[len(line)//2])
        return sum(passed)
    
    def fix_incorrect(self, line:list[int]):
        for rule in self.rules:
            before = rule[0]
            after = rule[1]
            if before in line and after in line and line.index(before) < line.index(after):
                continue
            elif before not in line or after not in line:
                continue
            else:
                before_index = line.index(before)
                after_index = line.index(after)

                line[before_index], line[after_index] = line[after_index], line[before_index]
                self.incorrect.append(line[len(line)//2])
                return

    
    def sum_of_incorrect(self):
        passed = []
        for line in self.pages:
            self.fix_incorrect(line)

        return sum(self.incorrect)


def part_a(data):
    man = Manual(data)

    s = man.get_sum_of_passed_tests()

    return s


def part_b(data):
    man = Manual(data)

    s = man.sum_of_incorrect()

    print(s)

    return s




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