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


def max_path():
    data = get_input()
    problem_tree = build_tree_rec(data)
    problem_visitor = AddVisitor()

    print('problem data ----------------------------')
    execute(problem_tree, problem_visitor, False)

max_path()

