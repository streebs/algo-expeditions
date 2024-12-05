import aocd
import unittest
import sys
from missing import *

# UPDATE THESE BASED ON DAY AND DATA FROM ADVENT OF CODE 
DAY = 4
YEAR = 2024
TEST_DATA = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
]
TEST_A_ANSWER = 18
TEST_B_ANSWER = 0



def part_a(data):
    for i in range(len(data)):
        data[i] = [c for c in data[i]]

    possibles = ["XMAS", "SAMX"]

    horizontal_2 = ''
    horizontal_3 = ''
    horizontal_4 = ''
    vertical_2 = ''
    vertical_3 = ''
    vertical_4 = ''

    cnt = 0
    for i in range(0,len(data)-3):
        for j in range(0,len(data[i])-3):

        

            horizontal_1 = data[i][j]+data[i][j+1]+data[i][j+2]+data[i][j+3]
            vertical_1 = data[i][j]+data[i+1][j]+data[i+2][j]+data[i+3][j]

            if j == len(data[i]) - 4:
                horizontal_2 = data[i+1][j]+data[i+1][j+1]+data[i+1][j+2]+data[i+1][j+3]
                horizontal_3 = data[i+2][j]+data[i+2][j+1]+data[i+2][j+2]+data[i+2][j+3]
                horizontal_4 = data[i+3][j]+data[i+3][j+1]+data[i+3][j+2]+data[i+3][j+3]

                vertical_2 = data[i][j+1]+data[i+1][j+1]+data[i+2][j+1]+data[i+3][j+1]
                vertical_3 = data[i][j+2]+data[i+1][j+2]+data[i+2][j+2]+data[i+3][j+2]
                vertical_4 = data[i][j+3]+data[i+1][j+3]+data[i+2][j+3]+data[i+3][j+3]

            lr_diagonal = data[i][j]+data[i+1][j+1]+data[i+2][j+2]+data[i+3][j+3]
            rl_diagonal = data[i][j+3]+data[i+1][j+2]+data[i+2][j+1]+data[i+3][j]

            if horizontal_1 in possibles:
                cnt += 1
            if horizontal_2 in possibles:
                horizontal_2 = ''
                cnt += 1
            if horizontal_3 in possibles:
                horizontal_3 = ''
                cnt += 1
            if horizontal_4 in possibles:
                horizontal_4 = ''
                cnt += 1

            if vertical_1 in possibles:
                cnt +=1
            if vertical_2 in possibles:
                vertical_2 = ''
                cnt +=1
            if vertical_3 in possibles:
                vertical_3 = ''
                cnt +=1
            if vertical_4 in possibles:
                vertical_4 = ''
                cnt +=1

            if lr_diagonal in possibles:
                cnt += 1
            if rl_diagonal in possibles:
                cnt += 1
    return cnt


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