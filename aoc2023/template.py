import aocd
import unittest
import sys
from missing import *

# UPDATE DAY for 
DAY = 0


def part_a(data):
    raise NotImplementedError


def part_b(data):
    raise NotImplementedError



################# UNIT TESTS #################
test_data = None # update test data
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(part_a(test_data), 0)
        self.assertEqual(part_b(test_data), 0)


############### DATA RETRIEVAL ###############
if test_data == None or DAY == 0:
    raise MissingFieldsError("You have not updated either `DAY`, `test_data`, or both!")
data = aocd.get_data(day=DAY, year=2023)
data_as_list = data.split("\n")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        sys.argv = [sys.argv[0]] # unittest uses the system args to run so it has to be cleared :/
        unittest.main()
    else:
        aocd.submit(part_a(data_as_list), part='a', day=DAY, year=2023)
        aocd.submit(part_b(data_as_list), part='b', day=DAY, year=2023)

if __name__ == "__main__":
    main()