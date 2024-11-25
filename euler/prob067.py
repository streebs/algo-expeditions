import os


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
    
def build_tree_rec(data, i=0, j=0):
    if i > len(data) - 2:
        return Node(data[i][j], [])
    return Node(data[i][j], [build_tree_rec(data, i+1,j), build_tree_rec(data, i+1,j+1)])

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
    
ex2 = [
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

def execute(tree: Node, visitor: AddVisitor, accept=True):
    if accept:
        tree.accept(visitor)
        print(f"path: {visitor.nums}")
        print(f"total: {visitor.getSum()}")
    else:
        tree.look_ahead_accept(visitor)
        print(f"path: {visitor.nums}")
        print(f"total: {visitor.getSum()}")
    

def get_input():
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname('euler/inputs/67_triangle.txt')))
    # print(path)
    with open(os.path.join(path, '67_triangle.txt'), 'r') as data:
        list_of_strings = data.readlines()
        for i in range(len(list_of_strings)):
            list_of_strings[i] = [x.strip() for x in list_of_strings[i].split()]
            list_of_strings[i] = [int(x) for x in list_of_strings[i]]

    return list_of_strings

# does not work for a large triangle. as there are so many options
def look_ahead(data: list, i=0, j=0, path:list=[]):
    path.append(data[i][j])

    if i == len(data) - 1: # this is on the last row
        return
    
    elif i == len(data) - 2: # no grand children
        options = {}
        options['l'] = data[i+1][j]
        options['r'] = data[i+1][j+1]

        m = max(options, key=options.get)

        if m == 'l':
            look_ahead(data, i+1, j, path)
        if m == 'r':
            look_ahead(data, i+1, j+1, path)    
    # if i == len(data) - 3: # this is the last row that has grand children
        # ...
    else:
        options = {}
        options['ll'] = data[i+1][j] + data[i+2][j]
        options['lr'] = data[i+1][j] + data[i+2][j+1]
        options['rl'] = data[i+1][j+1] + data[i+2][j+1]
        options['rr'] = data[i+1][j+1] + data[i+2][j+2]

        m = max(options, key=options.get)

        if m == 'll' or m == 'lr':
            look_ahead(data, i+1, j, path)
        if m == 'rl' or m == 'rr':
            look_ahead(data, i+1, j+1, path)

    return path
        


def max_path():
    data = get_input()
    path = look_ahead(data)
    print(f"path: {path}")
    print(f"sum: {sum(path)}")


max_path()

