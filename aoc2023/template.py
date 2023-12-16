import aocd
import unittest
import sys

def part_a(data):
    raise NotImplementedError


def part_b(data):
    raise NotImplementedError



################# UNIT TESTS #################
test_data = None # update test data
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(part_a(test_data, 0)) # make sure to update tests
        # self.assertEqual(part_b(test_data), 0)


############### DATA RETRIEVAL ###############
data = aocd.get_data(day=1, year=2023)
data_as_list = data.split("\n")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        sys.argv = [sys.argv[0]] # unittest uses the system args to run so it has to be cleared :/
        unittest.main()
    else:
        aocd.submit(part_a(data_as_list), part='a', day=1, year=2023)
        #aocd.submit(part_b(data_as_list), part='b', day=1, year=2023)

if __name__ == "__main__":
    main()