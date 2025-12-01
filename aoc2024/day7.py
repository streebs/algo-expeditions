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
TEST_B_ANSWER = 11387
# 9160: 5 209 15 8 5

class Node:
    num = None
    children = []
    def accept():
        pass

class Visitor:
    def __init__(self):
        self.totals = []
        self.previous = None
        self.stack = []
    def store(self, node):
        self.totals.append(node.num)

class Node:
    def __init__(self, num, children):
        self.num = num
        self.children = children
    def root_accept(self, visitor):
        visitor.previous = self.num
        visitor.stack.append(self.num)
        if self.children:
            self.children[0].left_accept(visitor)
            self.children[1].right_accept(visitor)
        visitor.stack.pop()
        # visitor.previous = visitor.stack[-1]

    def left_accept(self, visitor):
        prev = visitor.previous
        visitor.previous = prev + self.num
        visitor.stack.append(visitor.previous)
        if self.children:
            self.children[0].left_accept(visitor)
            self.children[1].right_accept(visitor)
        else:
            visitor.totals.append(visitor.previous)
        visitor.stack.pop()
        visitor.previous = visitor.stack[-1]

    def right_accept(self, visitor):
        prev = visitor.previous
        visitor.previous = prev * self.num
        visitor.stack.append(visitor.previous)
        if self.children:
            self.children[0].left_accept(visitor)
            self.children[1].right_accept(visitor)
        else:
            visitor.totals.append(visitor.previous)
        visitor.stack.pop()
        visitor.previous = visitor.stack[-1]
    
    def __str__(self):
        return str(self.num)
    def __repr__(self):
        return str(self.num)

class NodeTri:
    def __init__(self, num, children):
        self.num = num
        self.children = children
    def root_accept(self, visitor):
        visitor.previous = self.num
        visitor.stack.append(self.num)
        if self.children:
            self.children[0].left_accept(visitor)
            self.children[1].mid_accept(visitor)
            self.children[2].right_accept(visitor)
        visitor.stack.pop()
        # visitor.previous = visitor.stack[-1]

    def left_accept(self, visitor):
        prev = visitor.previous
        visitor.previous = prev + self.num
        visitor.stack.append(visitor.previous)
        if self.children:
            self.children[0].left_accept(visitor)
            self.children[1].mid_accept(visitor)
            self.children[2].right_accept(visitor)
        else:
            visitor.totals.append(visitor.previous)
        visitor.stack.pop()
        visitor.previous = visitor.stack[-1]

    def mid_accept(self, visitor):
        prev = visitor.previous
        visitor.previous = int(str(prev) + str(self.num)) #prev + self.num
        visitor.stack.append(visitor.previous)
        if self.children:
            self.children[0].left_accept(visitor)
            self.children[1].mid_accept(visitor)
            self.children[2].right_accept(visitor)
        else:
            visitor.totals.append(visitor.previous)
        visitor.stack.pop()
        visitor.previous = visitor.stack[-1]

    def right_accept(self, visitor):
        prev = visitor.previous
        visitor.previous = prev * self.num
        visitor.stack.append(visitor.previous)
        if self.children:
            self.children[0].left_accept(visitor)
            self.children[1].mid_accept(visitor)
            self.children[2].right_accept(visitor)
        else:
            visitor.totals.append(visitor.previous)
        visitor.stack.pop()
        visitor.previous = visitor.stack[-1]
    
    def __str__(self):
        return str(self.num)
    def __repr__(self):
        return str(self.num)

def build_tree(data, i=0):
    if i > len(data)-2:
        return Node(data[i], [])
    return Node(data[i], [build_tree(data, i+1), build_tree(data, i+1)])

def build_tri_tree(data, i=0):
    if i > len(data)-2:
        return NodeTri(data[i], [])
    return NodeTri(data[i], [build_tri_tree(data, i+1), build_tri_tree(data, i+1), build_tri_tree(data, i+1)])



def part_a(data):
    # for each line of data
        # get the total and the list of numbers
        # build the tree out of numbers
        # visit the nodes in the tree
        # if total in visitor
            # add to list of correct calibrations
    # return sum of correct calibrations
    c_values = []
    for line in data:
        split_data = line.split(':')
        total = int(split_data[0])

        list_trimmed = split_data[1].strip()
        list_str = list_trimmed.split(' ')
        values = [int(x) for x in list_str]
        
        tree = build_tree(values)
        v = Visitor()
        tree.root_accept(v)

        if total in v.totals:
            c_values.append(total)
    
    return sum(c_values)



    # tree = build_tree(data)

    # visitor = Visitor()
    # tree.root_accept(visitor)

    # print(visitor.totals)
def part_b(data):

    c_values = []
    for line in data:
        split_data = line.split(':')
        total = int(split_data[0])

        list_trimmed = split_data[1].strip()
        list_str = list_trimmed.split(' ')
        values = [int(x) for x in list_str]
        
        tree = build_tri_tree(values)
        v = Visitor()
        tree.root_accept(v)

        if total in v.totals:
            c_values.append(total)
    
    return sum(c_values)


    # tree = build_tri_tree(data)
    # v = Visitor()
    # tree.root_accept(v)

    # print(v.totals)



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
        part_b([17,8,14])
        
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