'''
This problem is really cool! I am going to make a binary tree and fill it will all the numbers
then all I need to do is find the child with the maximum value and visit it!
using the visitor pattern baby!
'''
# for type hinting
class Node:
    num = None
    children = []
    def accept():
        pass
    def look_ahead_accept():
        pass

class Visitor:
    def getVal(self, node):
        pass

class AddVisitor(Visitor):
    def __init__(self):
        self.nums = []
    def getVal(self, node):
        return self.nums.append(node.num)
    def getSum(self):
        return sum(self.nums)
    
class Node:
    def __init__(self, num, children: list[Node]=[]):
        self.num = num
        self.children = children
    def accept(self, visitor: Visitor):
        visitor.getVal(self)
        # print(self.num)
        if self.children and (self.children[0].num > self.children[1].num):
            self.children[0].accept(visitor)
        if self.children and (self.children[0].num < self.children[1].num):
            self.children[1].accept(visitor)

    def look_ahead_accept(self, visitor: Visitor):
        visitor.getVal(self)
        if self.children and self.children[0].children:
            ll = self.children[0].num + self.children[0].children[0].num
            lr = self.children[0].num + self.children[0].children[1].num
            rl = self.children[1].num + self.children[1].children[0].num
            rr = self.children[1].num + self.children[1].children[1].num

            options = {"ll":ll, "lr":lr, "rl":rl, "rr":rr}

            m = max(options, key=options.get)

            if m == "ll" or m =="lr":
                self.children[0].look_ahead_accept(visitor)
            if m == "rl" or m == "rr":
                self.children[1].look_ahead_accept(visitor)
        if self.children and self.children[0].children == []:
            if self.children and (self.children[0].num > self.children[1].num):
                self.children[0].accept(visitor)
            if self.children and (self.children[0].num < self.children[1].num):
                self.children[1].accept(visitor)
            
    def __str__(self):
        return str(self.num)
    def __repr__(self):
        return str(self.num)

test_data = [
    [3],
    [7,4],
    [2,4,6],
    [8,5,9,3]
]

ex1 = [
    [3],
    [7,4],
    [2,4,8],
    [8,5,9,3]
]
    
data = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62,98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

def build_tree(data, i=0, j=0):
    if i > len(data) - 2:
        return Node(data[i][j], [])
    return Node(data[i][j], [build_tree(data, i+1,j), build_tree(data, i+1,j+1)])
    

def execute(tree: Node, visitor: AddVisitor, accept=True):
    if accept:
        tree.accept(visitor)
        print(f"path: {visitor.nums}")
        print(f"total: {visitor.getSum()}")
    else:
        tree.look_ahead_accept(visitor)
        print(f"path: {visitor.nums}")
        print(f"total: {visitor.getSum()}")


def max_path():
    
    test_visitor = AddVisitor()
    ex1_visitor = AddVisitor()
    problem_visitor = AddVisitor()

    test_tree = build_tree(test_data)
    ex1_tree = build_tree(ex1)
    problem_tree = build_tree(data)

    print('test data -------------')
    execute(test_tree, test_visitor, False)

    print('ex1 data  -------------')
    execute(ex1_tree, ex1_visitor, False)

    print('problem data ----------')
    execute(problem_tree, problem_visitor, False)

max_path()

